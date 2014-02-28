<?php
    // initialize
    include_once('../Common/init.php');

    // include needed database functions
    // include_once($BASE_PATH . 'database/questions.php');

    if(!isset($_GET['sort']) || !validSorting($_GET['sort'])) {
        $_GET['sort'] = "newest";
    }
    if(!isset($_GET['page']) || !is_numeric($_GET['page'])) {
        $_GET['page'] = "1";
    }

    $pageNumber = intval($_GET['page']);
    $questions = getQuestionsWithSorting($_GET['sort'], 5*$pageNumber, 0);
    $counter = getNumberOfQuestionsWithSorting($_GET['sort']);
    $tags = array();

    foreach($questions as &$question) {
        $tags[] = getTagsOfQuestion($question['questionid']);
        $question['creationdate_p'] = getPrettyDate($question['creationdate']);
        $question['title'] = htmlspecialchars(stripslashes($question['title']));
        $question['body'] = getSmallerText(htmlspecialchars(stripslashes($question['body'])), 330);
        $question['gravatar'] = "http://www.gravatar.com/avatar/".md5(strtolower(trim($question['email'])))."?s=50&r=pg&d=identicon";
    }

    // send data to smarty
    $smarty->assign('sorted_questions', $questions);

    // display smarty template
    $smarty->display('index.tpl');

?>
