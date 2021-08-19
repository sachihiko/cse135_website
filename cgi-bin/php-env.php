<html>
    <?php  
    header("Cache-Control: no-cache\n");
    header("Content-type: text/html\n\n");
    ?>
    <head>
        <title>Environment Variables</title>
    </head>
    <body>
        <h1 align="center">Environment Variables</h1>
        <?php 
        $vars = array('a' => 'A', 'b' => 'B');
        foreach ($vars as $key => $value) {
            echo "<b>$key:</b> $value<br/>\n";
        }
        ?>
    </body>
</html>