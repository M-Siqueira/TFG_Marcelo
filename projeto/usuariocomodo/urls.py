from django.conf.urls import url

from .views import  UsuarioComodoListView, UsuarioComodoCreateView, UsuarioComodoUpdateView, UsuarioComodoDeleteView, UsuarioComodoDetailView

urlpatterns = [
	url(r'list/$', UsuarioComodoListView.as_view(), name='usuariocomodo_list'),
	url(r'cad/$', UsuarioComodoCreateView.as_view(), name='usuariocomodo_create'),
 	url(r'(?P<pk>\d+)/$', UsuarioComodoUpdateView.as_view(), name='usuariocomodo_update'),
	url(r'(?P<pk>\d+)/delete/$', UsuarioComodoDeleteView.as_view(), name='usuariocomodo_delete'), 
    url(r'(?P<pk>\d+)/detalhes/$', UsuarioComodoDetailView.as_view(), name='usuariocomodo_detail'),
]
