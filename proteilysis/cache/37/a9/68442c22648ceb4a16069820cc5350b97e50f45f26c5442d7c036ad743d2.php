<?php

/* index.html */
class __TwigTemplate_37a968442c22648ceb4a16069820cc5350b97e50f45f26c5442d7c036ad743d2 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = $this->env->loadTemplate("base.html");

        $this->blocks = array(
            'content' => array($this, 'block_content'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "base.html";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $this->parent->display($context, array_merge($this->blocks, $blocks));
    }

    // line 3
    public function block_content($context, array $blocks = array())
    {
        // line 4
        echo "
<div class=\"jumbotron\">
  <h1>Welcome to Proteilysis!</h1>
  <p class=\"lead\">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
  <div>
    <form role=\"form\" action=\"";
        // line 9
        echo twig_escape_filter($this->env, (isset($context["baseUrl"]) ? $context["baseUrl"] : null), "html", null, true);
        echo "/proteins/search\" method=\"GET\">
      <input class=\"form-control input-lg\" type=\"search\" name=\"query\" placeholder=\"Search for a protein...\">
    </form>
  </div>
</div>

<div class=\"container\">
  <div class=\"page-header\">
    <h2>Latest proteins</h2>
  </div>
</div>

";
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
        return array (  38 => 9,  31 => 4,  28 => 3,);
    }
}
