from django.conf.urls import patterns, include, url
from proteil import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="home"),
	url(r'^proteins/$', views.ProteinList.as_view(), name="protein_list"),
	url(r'^proteins/new$', views.protein_add, name="protein_add"),

	# util views
	url(r'^api/utils/upload_pisces_file$', views.upload_pisces_file, name="upload_pisces_file"),
	url(r'^api/utils/upload_ids_list$', views.upload_ids_list, name="upload_ids_list"),
	url(r'^api/proteins/add/(?P<id>[a-zA-Z0-9]{4,6})$', views.add_protein, name="add_protein"),
)

