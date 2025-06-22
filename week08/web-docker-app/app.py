from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🎆 승환님의 Docker 웹서버!</h1>
    <p>🐳 이 웹사이트는 Docker 컨테이너에서 실행되고 있어요!</p>
    <p>🚀 Day 37 Docker 실무 활용 성공!</p>
    <p>📅 2025-06-20 Week 8 진행 중</p>
    <hr>
    <a href="/info">📊 시스템 정보 보기</a>
    """

@app.route('/info')
def info():
    return """
    <h2>📊 시스템 정보</h2>
    <p><strong>컴퓨터:</strong> Docker 컨테이너</p>
    <p><strong>프로그램:</strong> Python + Flask</p>
    <p><strong>만든이:</strong> 승환님</p>
    <p><strong>날짜:</strong> 2025-06-20</p>
    <hr>
    <a href="/">🏠 홈으로 돌아가기</a>
    """

if __name__ == '__main__':
    print("🔥 GitHub Actions 자동 빌드 테스트!")
    app.run(host='0.0.0.0', port=5000, debug=True)