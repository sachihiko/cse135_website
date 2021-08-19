<html>
    <?php
    header("Cache-Control: no-cache\n");
    header("Content-type: text/html\n\n");
    ?>
    <head>
        <title>GET Request Echo</title>
    </head>
    <body>
        <h1 align="center">GET Request Echo</h1>
    <?php
    if ($_ENV['QUERY_STRING']){
        $buffer = $_ENV['QUERY_STRING']
        parse_str($buffer, $params);
        foreach($params as $key => $value){
            echo"<b>$key</b>: $value<br/>";
        }
    }
    ?>
    </body>
</html>