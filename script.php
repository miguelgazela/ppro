<?php

ini_set("display_errors", 1);

$output = array();
$cmd_result = exec("python /Users/migueloliveira/Dropbox/projects/ppro/proteilysis/script_processPdbId.py 1AEP", $output);

echo var_dump($output);

?>