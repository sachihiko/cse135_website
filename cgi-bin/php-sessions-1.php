<html>
    <?php
    header("Cache-Control: no-cache\n");
    header("Content-type: text/html\n\n");
    ?>
    <head>
    <title>PHP Sessions</title>
    </head>
    <body>
        <h1>PHP Sessions</h1>
        <?php
        $name = 'sachi';
        #$name = $_POST['username'];
        setcookie("username", $name);
        echo $_SERVER["HTTP_COOKIE"];

        ?>
    </body>
</html>
