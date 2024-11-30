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
        echo 'fail to connect to database: ' . $e->getMessage();
        exit();
    }

    
    try{
        $query = "SELECT * FROM users WHERE username = '" . $username . "' and password = '" . $password . "'";
        $result = $pdo->query($query);
        $user = $result->fetch();

        if ($user) {
            echo '<h2>successfully login</h2>';
            echo '<br><br><h2>sql query</h2>';
            echo $query;
            // echo '<script>locatoin = alert(4)</script>';                               
        } else {
            echo '<h2>login failure</h2>';
            echo '<br><br><h2>sql query</h2>';
            echo $query;
        }
    } catch (PDOException $e) {
        
        echo '<h2>followin error has occurred:</h2>' . $e->getMessage();
        echo '<br><br><h2>sql query</h2>';
        echo $query;
    }
    
}
?>