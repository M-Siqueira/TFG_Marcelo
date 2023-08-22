from django.conf.urls import url

from .views import  ComodoListView, ComodoCreateView, ComodoUpdateView, ComodoDeleteView

urlpatterns = [
	url(r'list/$', ComodoListView.as_view(), name='comodo_list'),
	url(r'cad/$', ComodoCreateView.as_view(), name='comodo_create'),
 	url(r'(?P<pk>\d+)/$', ComodoUpdateView.as_view(), name='comodo_update'),
	url(r'(?P<pk>\d+)/delete/$', ComodoDeleteView.as_view(), name='comodo_delete'), 
]
