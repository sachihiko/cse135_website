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
        $name = $_POST["username"]
        echo "Your Name: $name";
        setcookie("username", $name);
        echo $_SERVER["HTTP_COOKIE"];

        ?>
        <br/><br/>
        <a href="/cgi-bin/php-sessions-2.php">Session Page 2</a><br/>
        <a href="/php-cgiform.html">PHP CGI Form</a><br />
        <form style="margin-top:30px" action="/cgi-bin/php-destroy-session.php" method="get">
        <button type="submit">Destroy Session</button>
        </form>

    </body>
</html>
