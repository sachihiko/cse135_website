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
    if ($_SERVER['QUERY_STRING']){
        $buffer = $_SERVER['QUERY_STRING'];
        echo "Query string: $buffer<br/>";
        echo "Parsed query string:<br/>";
        parse_str($buffer, $params);
        foreach($params as $key => $value){
           echo"<b>$key</b>: $value<br/>";
        }
    }
    ?>
    </body>
</html>