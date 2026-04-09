import os
import smtplib
import json
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from google import genai
from google.genai import types
from github import Github, Auth

# 환경 변수
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

client = genai.Client(api_key=GEMINI_API_KEY)

# HTML 템플릿 정의
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Pretendard', 'Malgun Gothic', sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #eee; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        h1 {{ color: #2E865F; margin: 0; font-size: 24px; }}
        .date-range {{ font-size: 14px; color: #666; margin-top: 5px; }}
        h3 {{ color: #2c3e50; border-left: 4px solid #2E865F; padding-left: 10px; margin-top: 30px; font-size: 18px; }}
        .quiz-box {{ background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
        ul {{ padding-left: 20px; margin: 0; }}
        li {{ margin-bottom: 12px; }}
        li:last-child {{ margin-bottom: 0; }}
        .footer {{ margin-top: 40px; font-size: 12px; color: #999; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 주간 TIL 퀴즈</h1>
            <div class="date-range">{date_range}</div>
        </div>
        
        {content}

        <div class="footer">
            배운 내용을 인출하는 것이 최고의 학습입니다. 🧐<br>
            GitHub TIL Repository
        </div>
    </div>
</body>
</html>
"""

def get_target_files():
    if not GITHUB_TOKEN or not REPO_NAME:
        print("Error: GitHub configuration missing.")
        return [], None, None, None

    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    repo = g.get_repo(REPO_NAME)

    # KST (UTC+9) 기준 지난 주 월요일 ~ 일요일 계산
    kst = timezone(timedelta(hours=9))
    now_kst = datetime.now(kst)
    
    # 오늘이 월요일(0)이라고 가정하고 스케줄링됨.
    # 지난 주 월요일 = 오늘 - 7일
    days_to_subtract = now_kst.weekday() + 7
    start_date = now_kst - timedelta(days=days_to_subtract)
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    # 지난 주 일요일 = 시작일 + 6일
    end_date = start_date + timedelta(days=6)
    end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    print(f"Searching commits between {start_date} and {end_date} (KST)")
    
    # PyGithub의 get_commits는 timezone-aware datetime을 잘 처리함 (UTC로 변환하여 요청)
    commits = repo.get_commits(since=start_date, until=end_date)
    
    target_files = set()
    
    for commit in commits:
        for file in commit.files:
            # .md 파일이면서 README/SUMMARY 제외
            if file.filename.endswith(".md") and file.filename not in ["README.md", "SUMMARY.md"]:
                 target_files.add(file.filename)

    return list(target_files), repo, start_date, end_date

def generate_quiz(content, filename):
    prompt = f"""
    당신은 유능한 Software Engineer이자 멘토입니다. 아래의 학습 내용(Markdown)을 바탕으로 
    학습한 내용을 점검할 수 있는 퀴즈 3개를 만들어주세요.

    [학습 내용]
    {content}

    [요청 사항]
    - 반드시 Python의 리스트 형태(JSON)로 반환해주세요.
    - 예시: ["질문 1 내용?", "질문 2 내용?", "질문 3 내용?"]
    - 마크다운 포맷팅(```json 등) 없이 순수 JSON 문자열만 반환하세요.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error generating quiz for {filename}: {e}")
        return []

def send_email(subject, body_html):
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not RECIPIENT_EMAIL:
        print("Error: Email configuration missing.")
        return

    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = Header(subject, 'utf-8')
    
    msg.attach(MIMEText(body_html, 'html', 'utf-8'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    print("Starting Weekly Quiz Script...")
    files, repo, start_date, end_date = get_target_files()
    
    if not files:
        print("No modified TIL files found for the target period.")
        return

    print(f"Found {len(files)} files: {files}")

    email_content = ""
    
    has_content = False
    for filepath in files:
        try:
            print(f"Processing {filepath}...")
            # 파일 내용 가져오기
            content = repo.get_contents(filepath).decoded_content.decode("utf-8")
            
            quizzes = generate_quiz(content, filepath)
            
            if not quizzes or len(quizzes) == 0:
                print(f"No quizzes generated for {filepath}")
                continue
                
            filename_clean = filepath.split("/")[-1].replace("_", " ").replace(".md", "")
            
            email_content += f"<h3>{filename_clean}</h3>"
            email_content += "<div class='quiz-box'><ul>"
            for i, quiz in enumerate(quizzes, 1):
                email_content += f"<li><strong>Q{i}.</strong> {quiz}</li>"
            email_content += "</ul></div>"
            
            has_content = True
            
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            
    if has_content:
        date_range_str = f"{start_date.strftime('%Y.%m.%d')} ~ {end_date.strftime('%Y.%m.%d')}"
        final_html = HTML_TEMPLATE.format(date_range=date_range_str, content=email_content)
        send_email("주간 TIL 퀴즈", final_html)
    else:
        print("No content to email.")

if __name__ == "__main__":
    main()