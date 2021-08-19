<html>
    <?php  
    header("Cache-Control: no-cache\n");
    header("Content-type: text/html\n\n");
    ?>

    <head>
        <title>Hello, PHP!</title>
    </head>
    <body>
        <h1>Sachi was here - Hello, PHP XD</h1>
        <p>This page was generated using PHP</p>
        <?php 
        $date = localtime();
        echo "<p>Current Time: $date</p>";
        $address = getenv("REMOTE_ADDR");
        echo "<p>Your IP Address: $address</p>"
        ?>
    </body>
</html>