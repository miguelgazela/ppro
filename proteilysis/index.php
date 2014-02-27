<?php
    ini_set('display_errors', 'On');

    require 'libs/Slim/Slim.php';
    \Slim\Slim::registerAutoloader();

    $app = new \Slim\Slim(array(
        'debug' => true
    ));

    // ROUTES

    $app->get('/', function () {
        echo "<h1>Welcome to Proteilysis!</h1>";
    });

    $app->get('/hello/:name', function ($name) {
        echo "Hello, $name";
    });

    $app->run();
?>