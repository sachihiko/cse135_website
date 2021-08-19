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
        foreach ($_ENV as $key => $value) {
            echo "<b>{$key}:</b> {$value}<br/>\n ";
        }
        ?>
    </body>
</html>