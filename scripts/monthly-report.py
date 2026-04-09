import os
import smtplib
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

def get_monthly_stats():
    if not GITHUB_TOKEN or not REPO_NAME:
        print("Error: GitHub configuration missing.")
        return None, None

    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    repo = g.get_repo(REPO_NAME)

    # KST 기준 지난 달 1일 ~ 말일 계산
    kst = timezone(timedelta(hours=9))
    now_kst = datetime.now(kst)
    
    # 이번 달 1일
    this_month_first = now_kst.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    # 지난 달 말일 (이번 달 1일 - 1초)
    last_month_end = this_month_first - timedelta(seconds=1)
    # 지난 달 1일
    last_month_start = last_month_end.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    print(f"Analyzing stats between {last_month_start} and {last_month_end} (KST)")
    
    commits = repo.get_commits(since=last_month_start, until=last_month_end)
    
    added_files = set()
    modified_files = set()
    
    for commit in commits:
        for file in commit.files:
            if file.filename.endswith(".md") and file.filename not in ["README.md", "SUMMARY.md"]:
                if file.status == "added":
                    added_files.add(file.filename)
                elif file.status == "modified":
                    modified_files.add(file.filename)

    return {
        "month": last_month_start.strftime("%Y년 %m월"),
        "total_commits": commits.totalCount,
        "new_tils": list(added_files),
        "modified_tils": list(modified_files)
    }

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
        .stats {{ display: flex; justify-content: space-around; background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 25px; }}
        .stat-item {{ text-align: center; }}
        .stat-value {{ display: block; font-size: 20px; font-weight: bold; color: #2E865F; }}
        .stat-label {{ font-size: 12px; color: #666; }}
        h3 {{ color: #2c3e50; border-left: 4px solid #2E865F; padding-left: 10px; margin-top: 25px; }}
        ul {{ padding-left: 20px; }}
        li {{ margin-bottom: 8px; }}
        .footer {{ margin-top: 40px; font-size: 12px; color: #999; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📅 {month} 월간 리포트</h1>
        </div>
        
        <div class="stats">
            <div class="stat-item">
                <span class="stat-value">{new_count}</span>
                <span class="stat-label">새로운 학습</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">{modified_count}</span>
                <span class="stat-label">보완한 내용</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">{total_commits}</span>
                <span class="stat-label">커밋 활동</span>
            </div>
        </div>

        {content}

        <div class="footer">
            꾸준함이 재능을 이깁니다. 다음 달도 파이팅! 🚀<br>
            GitHub TIL Repository
        </div>
    </div>
</body>
</html>
"""

def generate_report_content(stats):
    prompt = f"""
    당신은 학습 멘토입니다. 학생이 지난 달 동안 학습한 내용을 바탕으로 
    동기부여가 되고 성취감을 느낄 수 있는 리포트 본문을 작성해주세요.

    [통계 정보]
    - 기간: {stats['month']}
    - 새로 작성한 문서 수: {len(stats['new_tils'])}개
    - 수정/보완한 문서 수: {len(stats['modified_tils'])}개

    [새로 학습한 주제들]
    {', '.join([f.split('/')[-1].replace('.md', '') for f in stats['new_tils']])}

    [보완한 주제들]
    {', '.join([f.split('/')[-1].replace('.md', '') for f in stats['modified_tils']])}

    [요청 사항]
    - **순수 HTML 태그만** 사용하여 작성하세요 (html, head, body 태그 제외).
    - `<h3>` 태그로 소제목을 달고, `<p>`, `<ul>`, `<li>` 등으로 내용을 구성하세요.
    - 다음 3가지 섹션으로 구성하세요:
        1. <h3>이달의 요약</h3>: 성과 칭찬 및 요약
        2. <h3>학습 하이라이트</h3>: 학습 내용의 깊이나 다양성 언급
        3. <h3>다음 달을 위한 조언</h3>: 짧은 격려
    - 별도의 스타일(CSS)이나 마크다운 문법을 사용하지 마세요.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.8,
            )
        )
        # 템플릿에 적용
        return HTML_TEMPLATE.format(
            month=stats['month'],
            new_count=len(stats['new_tils']),
            modified_count=len(stats['modified_tils']),
            total_commits=stats['total_commits'],
            content=response.text
        )
    except Exception as e:
        print(f"Error generating report: {e}")
        return "리포트 생성 중 오류가 발생했습니다."

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
    print("Starting Monthly Report Script...")
    stats = get_monthly_stats()
    
    if not stats:
        print("Failed to retrieve stats.")
        return

    if stats['total_commits'] == 0 and len(stats['new_tils']) == 0 and len(stats['modified_tils']) == 0:
        print("No activity last month.")
        # 활동이 없어도 리포트를 보낼지 여부는 선택사항이나, 여기서는 스킵하거나 간단한 격려 메일을 보낼 수도 있음.
        # 일단은 스킵.
        return

    send_email(f"{stats['month']} 월간 TIL 리포트", generate_report_content(stats))

if __name__ == "__main__":
    main()
