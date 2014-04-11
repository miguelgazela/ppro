<?php
    ini_set('display_errors', 'On');

    require_once('Database/protein.php');

    require 'lib/Slim/Slim.php';
    \Slim\Slim::registerAutoloader();

    require 'lib/Twig/Autoloader.php';
    Twig_Autoloader::register();

    $app = new \Slim\Slim(array(
        'debug' => true,
        'view' => new \Slim\Views\Twig(),
        'templates.path' => 'templates'
    ));

    $view = $app->view();
    
    $view->parserOptions = array(
        'debug' => true,
        'cache' => dirname(__FILE__) . '/cache'
    );

    // ROUTES

    $app->get('/', function () use ($app) {
        $app->render('index.html');
    });

    $app->get('/proteins', function () use ($app) {

        $app->render('proteins/list.html');
    });


    /* Temporary stuff for my LGP project */
    $app->get('/lgp/products/:productId', function ($productId) use ($app) {
        $result = array(
            "id" => $productId,
            "name" => "Product #".$productId,
            "description" => "The longer description for the product",
            "smallDescription" => "The smaller description for the product"
        );
        header("Content-Type: application/json");
        echo json_encode($result);
    });

    $app->run();
?>