from django.conf.urls import patterns, include, url
from protein_folding_analysis import views

urlpatterns = patterns('',

    url(r'^$', views.index, name="index"),
)