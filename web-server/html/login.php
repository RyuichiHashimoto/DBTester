<?php
// login.php（フォームの上または別ファイルで処理）
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $db_host = getenv('DB_HOST');
    $db_name = getenv('DB_NAME');
    $db_user = getenv('DB_USER');
    $db_password = getenv('DB_PASSWORD');

    
    $dsn = "mysql:host=$db_host;dbname=$db_name;charset=utf8mb4";
    
    try {
        $pdo = new PDO($dsn, $db_user, $db_password);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        echo 'データベース接続に失敗しました: ' . $e->getMessage();
        exit();
    }

    // $query = "SELECT * FROM users WHERE username = '" . $username . "'";
    $query = "SELECT * FROM users WHERE username = '" . $username . "' and password = '" . $password . "'";
    $result = $pdo->query($query);
    $user = $result->fetch();

    if ($user) {
        // echo 'ログインに成功しました。';        
        echo '<script>locatoin = alert(4)</script>';
        
        // リダイレクト処理
        header("Location: $url");

        // 必須: スクリプトを終了
        exit();
    } else {
        echo 'ログインに失敗しました。';
    }
}
?>