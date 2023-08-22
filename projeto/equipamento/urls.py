from django.conf.urls import url

from .views import  EquipamentoListView, EquipamentoCreateView, EquipamentoUpdateView, EquipamentoDeleteView

urlpatterns = [
	url(r'list/$', EquipamentoListView.as_view(), name='equipamento_list'),
	url(r'cad/$', EquipamentoCreateView.as_view(), name='equipamento_create'),
 	url(r'(?P<pk>\d+)/$', EquipamentoUpdateView.as_view(), name='equipamento_update'),
	url(r'(?P<pk>\d+)/delete/$', EquipamentoDeleteView.as_view(), name='equipamento_delete'), 
]
