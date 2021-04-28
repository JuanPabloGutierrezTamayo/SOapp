from django.contrib import admin
from django.urls import path
from proyectoSO import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('crear/', views.crear, name="crear"),
    path('borrar/', views.borrar, name="borrar"),
    path('copiar/', views.copiar, name="copiar"),
    path('mover/', views.mover, name="mover"),
    path('verPermisos/', views.verPermisos, name="verPermisos"),
    path('cambiarPermisos/', views.cambiarPermisos, name="cambiarPermisos"),
    path('renombrar/', views.renombrar, name="renombrar"),
    path('cambiarPropietario/', views.cambiarPropietario, name="cambiarPropietario"),
    path('abrir/',views.abrir,name="abrir"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)