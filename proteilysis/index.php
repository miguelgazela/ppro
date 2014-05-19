<?php
    ini_set('display_errors', 1);
    ini_set('log_errors', 1);

    require_once('Common/init.php');

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

    // FUNCTIONS

    function xml2array($xml) {
        $arr = array();
     
        foreach ($xml->children() as $r) {
            $t = array();
            if(count($r->children()) == 0) {
                $arr[$r->getName()] = strval($r);
            } else {
                $arr[$r->getName()][] = xml2array($r);
            }
        }
        return $arr;
    }

    // ROUTES

    $app->get('/', function () use ($app, $BASE_URL) {
        $app->render('index.html', array("baseUrl" => $BASE_URL));
    });


    $app->get('/proteins', function () use ($app, $db, $BASE_URL) {
        $stmt = $db->prepare("select * from protein");

        try {
            $stmt->execute();
            $result = $stmt->fetchAll();
            $app->render('proteins/list.html', array("baseUrl" => $BASE_URL, "proteins" => $result));
        } catch(PDOException $e) {
            echo "Error!: " . $e->getMessage() . "<br/>";
            die();
        }
    });


    $app->get('/proteins/:id', function($id) use ($app, $db, $BASE_URL) {
        $file = new SimpleXmlElement(file_get_contents("http://www.uniprot.org/uniprot/".$id.".xml"));
        $app->render('proteins/view.html', array("baseUrl" => $BASE_URL, "protein" => array("accID" => $id, "content" => xml2array($file->entry))));
    })->conditions(array('id' => '[A-Z0-9]{6}'));


    $app->get('/proteins/:id/debug', function($id) use ($app) {
        $file = new SimpleXmlElement(file_get_contents("http://www.uniprot.org/uniprot/".$id.".xml"));
        echo '<pre>';print_r(xml2array($file->entry));exit;
    });


    $app->get('/proteins/search', function() use ($app, $db, $BASE_URL) {
        $app->contentType('application/json');
        $result = array();
        $query = $app->request->get('query');

        echo json_encode(array('data' => $result, 'query' => $query));
    });


    $app->get('/proteins/new', function() use ($app, $BASE_URL) {
        $app->render('proteins/new.html', array("baseUrl" => $BASE_URL));
    });


    $app->post('/proteins/new', function() use ($app, $db, $BASE_URL) {
        global $BASE_PATH;

        $app->contentType('application/json');
        $data = $app->request->post();

        if (!isset($data['list-ids']) || $data['list-ids'] == "") {
            echo json_encode(array("status_code" => "101", "status_msg" => "Missing required list of ids"));
        } else {
            $result = array();

            $listIds = str_replace("\r\n", "\n", $data['list-ids']);
            $listIds = explode("\n", $listIds);

            foreach($listIds as &$id) {
                $result[$id] = array();

                // check if protein already exists in the database
                $stmt = $db->prepare("select * from protein where pdbId = ?");

                try {
                    $stmt->execute(array($id));
                    $protein = $stmt->fetch();

                    if($protein) {
                        $result[$id]['state'] = "EXISTS";
                        $result[$id]['protein'] = $protein;
                    } else {
                        $result[$id]['state'] = "NOT_EXISTS";

                        $command = escapeshellcmd('python '.$BASE_PATH.'script_processPdbId.py '.$id);
                        $result[$id]['cmd'] = $command;
                        $output = shell_exec($command);

                        $result[$id]['script_result'] = $output;
                    }
                } catch (PDOException $e) {
                    echo "Error! " . $e->getMessage() . "<br/>";
                    die();
                }
            }

            echo json_encode(array('data' => $result));
        }
    });

    $app->run();
?>