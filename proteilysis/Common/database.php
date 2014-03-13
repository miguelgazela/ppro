<?php
    // Connect to the Database
    $db = new PDO('mysql:host='.getenv('MYSQL_HOST').';dbname='.getenv('DBNAME'), getenv('MYSQL_USER'), getenv('MYSQL_PASS'));
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
?>