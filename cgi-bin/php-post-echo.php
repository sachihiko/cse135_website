<html>
    <?php
    header("Cache-Control: no-cache\n");
    header("Content-type: text/html\n\n");
    ?>
    <head>
        <title>POST Request Echo</title>
    </head>
    <body>
        <h1 align="center">POST Request Echo</h1>
<?php
        echo "Message Body:<br/>";
        if ($_POST){
        foreach($_POST as $key => $value){
           echo"<b>$key</b>: $value<br/>";
        }
    }
    ?>
    </body>
</html>
