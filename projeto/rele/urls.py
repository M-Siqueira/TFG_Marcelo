from django.conf.urls import url

from .views import  ReleListView, ReleCreateView, ReleUpdateView, ReleDeleteView

urlpatterns = [
	url(r'list/$', ReleListView.as_view(), name='rele_list'),
	url(r'cad/$', ReleCreateView.as_view(), name='rele_create'),
 	url(r'(?P<pk>\d+)/$', ReleUpdateView.as_view(), name='rele_update'),
	url(r'(?P<pk>\d+)/delete/$', ReleDeleteView.as_view(), name='rele_delete'), 
]
