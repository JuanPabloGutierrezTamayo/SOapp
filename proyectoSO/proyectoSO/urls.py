from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('crear/', crear, name="crear"),
    path('borrar/', borrar, name="borrar"),
    path('copiar/', copiar, name="copiar"),
    path('mover/', mover, name="mover"),
    path('verPermisos/', verPermisos, name="verPermisos"),
    path('cambiarPermisos/', cambiarPermisos, name="cambiarPermisos"),
    path('renombrar/', renombrar, name="renombrar"),
    path('cambiarPropietario/', cambiarPropietario, name="cambiarPropietario"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
