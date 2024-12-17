FROM python:3.9-slim

WORKDIR /app

# Flaskのインストール
RUN pip install --no-cache-dir flask

# CMDでFlaskアプリを起動。app.py はVolumeでマウントされる前提。
CMD ["python", "app.py"]
