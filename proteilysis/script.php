<?php

ini_set("display_errors", 1);

echo "Starting script\n";
$descriptorspec = array(
           0 => array("pipe", "r"),
           1 => array("pipe", "w"),
           2 => array("file", "error.log", "a")
        );

        $process = proc_open('python /Users/migueloliveira/Dropbox/projects/ppro/proteilysis/script_processPdbId.py 1AEP', $descriptorspec, $pipes);

        if (is_resource($process)) {

          // print pipe output
          echo stream_get_contents($pipes[1]);

          // close pipe
          fclose($pipes[1]);

          // close process
          proc_close($process);
        }

?>