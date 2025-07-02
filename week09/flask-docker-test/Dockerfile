# Python 3.9 기반 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 앱 코드 복사
COPY app.py .

# 포트 5000 노출
EXPOSE 5000

# 앱 실행
CMD ["python", "app.py"]