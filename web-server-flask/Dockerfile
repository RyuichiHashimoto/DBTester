# Dockerfile

# PHPとApacheを含む公式のPHPイメージを使用
FROM php:8.0-apache

# 必要なPHP拡張モジュールをインストール（例: pdo_mysql）
RUN docker-php-ext-install pdo_mysql

# Apacheのmod_rewriteを有効化（必要に応じて）
RUN a2enmod rewrite

# 作業ディレクトリを設定
WORKDIR /var/www/html

EXPOSE 80