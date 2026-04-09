import os
from google import genai
from google.genai import types
from github import Github, Auth

# 환경 변수
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
COMMIT_SHA = os.getenv("COMMIT_SHA")

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_commit():
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN이 없습니다.")
        return

    # GitHub 인증
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    
    repo = g.get_repo(REPO_NAME)
    commit = repo.get_commit(sha=COMMIT_SHA)
    
    print(f"Commit 분석 시작: {COMMIT_SHA}")
    
    processed_count = 0
    for file in commit.files:
        if file.filename.endswith(".md") and file.status == "added":
            print(f"🔍 새로운 TIL 발견: {file.filename}")
            try:
                content = repo.get_contents(file.filename, ref=COMMIT_SHA).decoded_content.decode("utf-8")
                review_content = ask_gemini(content)
                create_github_issue(repo, file.filename, review_content)
                processed_count += 1
            except Exception as e:
                print(f"❌ 파일 처리 중 오류 ({file.filename}): {e}")

    if processed_count == 0:
        print("리뷰를 작성할 새 .md 파일이 없습니다.")
    else:
        print(f"총 {processed_count}개 파일에 대한 리뷰 리포트 작성 완료")

def ask_gemini(content):
    prompt = f"""
    당신은 Senior Software Engineer 입니다.
    새로 작성된 아래의 학습 내용을 읽고, 학습에 대한 리뷰 리포트를 작성해주세요.
    
    [요청 사항]
    - 피드백은 다음의 4개 단락으로 구성하세요. 각 단락을 markdown의 h3 태그로 나타내세요.
        1. 요약 및 총평
        2. 중요한 부분
        3. 틀렸거나 부족한 부분
        4. 추가적으로 학습하면 좋을 것들
    - 주어진 4개의 단락을 제외하고는 추가적인 문장을 포함하지 마세요.
    ---
    [학습 내용]
    {content}
    """
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=1.0,
            top_p=0.95,
            top_k=64,
            max_output_tokens=8192,
            response_mime_type="text/plain",
        )
    )
    
    return response.text

def create_github_issue(repo, filename, body):
    title = f"📝 AI Review: {filename}"
    issue = repo.create_issue(title=title, body=body)
    print(f"✅ 이슈 생성 완료: {title} (#{issue.number})")

if __name__ == "__main__":
    analyze_commit()
