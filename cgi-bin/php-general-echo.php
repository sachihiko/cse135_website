<html>
    <?php
    header("Cache-Control: no-cache\n");
    header("Content-type: text/html\n\n");
    ?>
    <head>
        <title>General Request Echo</title>
    </head>
    <body>
        <h1 align="center">General Request Echo</h1>
<?php
        $protocol = $_SERVER['SERVER_PROTOCOL'];
        $method = $_SERVER['REQUEST_METHOD'];
        echo "<p><b>HTTP Protocol:</b> $protocol</p>";
        print "<p><b>HTTP Method:</b> $method</p>";
        echo "Message Body:<br/>";
        if ($method){
        foreach($method as $key => $value){
           echo"<b>$key</b>: $value<br/>";
        }
    }
    ?>
    </body>
</html>