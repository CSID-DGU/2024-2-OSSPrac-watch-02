# Dockerfile

# 베이스 이미지 지정 : Flask 애플리케이션을 실행하는 데 필요한 모듈이 이미 포함된 이미지
FROM tiangolo/uwsgi-nginx-flask:python3.9

# 현재 디렉토리의 ./SubjectA2-3-1 폴더(앱 폴더)를 컨테이너의 /app 폴더로 복사
COPY ./SubjectA2-3-1 /app