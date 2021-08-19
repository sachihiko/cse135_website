<?php
$date = localtime();
$address = getenv("REMOTE_ADDR");
$data = array('title' => 'Hello, Perl!', 'heading' => 'Hello, Sachi!', 'message' => 'This page was generated with PHP', 'time' => $date, 'IP' => $address);
header('Content-Type: application/json');
echo json_encode($data);
?>

