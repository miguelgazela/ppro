<?php
    ini_set('display_errors', 'On');

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

    $app->get('/hello/:name', function ($name) use ($app) {
        $app->render('index.html', array('name' => $name));
    });

    $app->run();
?>