<?php

/* index.html */
class __TwigTemplate_37a968442c22648ceb4a16069820cc5350b97e50f45f26c5442d7c036ad743d2 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1>";
        // line 7
        echo twig_escape_filter($this->env, ((array_key_exists("name", $context)) ? (_twig_default_filter((isset($context["name"]) ? $context["name"] : null), "User")) : ("User")), "html", null, true);
        echo ", welcome to Proteilysis!</h1>
    </body>
</html>";
    }

    public function getTemplateName()
    {
        return "index.html";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  27 => 7,  19 => 1,);
    }
}
