-- init.sql

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


-- サンプルデータの挿入
INSERT INTO users (username, password) VALUES
('admin', '12345678'),
('user1',   'password'),
('user2', 'password');