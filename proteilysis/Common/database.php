<?php
    // Connect to the Database
	try {
	    $db = new PDO('mysql:host=127.0.0.1;dbname=proteilysis', 'root', 'BKsrUgn6');
	    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	    $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
	} catch(PDOException $e) {
		echo "Error!: " . $e->getMessage() . "<br/>";
		die();
	}
?>