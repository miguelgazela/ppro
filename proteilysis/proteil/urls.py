from django.conf.urls import patterns, include, url
from proteil import views

urlpatterns = patterns('',
	url(r'^$', views.index),
)