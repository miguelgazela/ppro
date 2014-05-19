<?php

$command = escapeshellcmd('python script_processPdbId.py 1AEP');
$result[$id]['cmd'] = $command;
$output = exec($command);

echo $output;

?>