from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'aviso/', include('aviso.urls')),
    url(r'comodo/', include('comodo.urls')),
    url(r'equipamento/', include('equipamento.urls')),
    url(r'comodousuario/', include('usuariocomodo.urls')),
    url(r'rele/', include('rele.urls')),
    url(r'usuario/', include('usuario.urls')),
    
    url(r'^accounts/', include('django.contrib.auth.urls')),
]