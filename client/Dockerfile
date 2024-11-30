# ベースイメージを指定
FROM ubuntu:24.04

# 必要な環境変数を設定
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    software-properties-common \
    python3 \
    python3-pip \
    nodejs \
    npm \
    default-mysql-client \
    python3.12-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# MongoDB Shellをインストール
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && apt-get install -y mongodb-org-shell && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /home/work

# 必要なスクリプトやアプリケーションをコピー（必要に応じて）
# COPY ./your_script.py ./  # 必要ならPythonスクリプトをコピー
# COPY ./your_app.js ./    # 必要ならNode.jsアプリをコピー

# Python依存パッケージをインストール（必要に応じて）
# RUN pip3 install -r requirements.txt

# Node.js依存パッケージをインストール（必要に応じて）
# RUN npm install

# 初期コマンドを設定（必要に応じて変更）
CMD ["bash"]
