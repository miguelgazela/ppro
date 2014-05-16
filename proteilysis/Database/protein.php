<?php
    require_once('Common/init.php');

    function getAllProteins($limit) {

        global $db;

        if (!is_numeric($limit)) {
            throw new Exception("Invalid limit passed to 'getAllProteins' function.");
        }

        try {
            $stmt = $db->prepare("SELECT * FROM post, answer WHERE postid = answerid AND ownerid = ? AND draft = false LIMIT ?");
            $stmt->execute(array($userid, $limit));
            return $stmt->fetchAll();
        } catch(Exception $e) {
            $errors->addError('answer', 'error processing select on answer table');
            $errors->addError('exception', $e->getMessage());
            throw ($errors);
        }
    }
?>