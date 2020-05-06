from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from property import views

#global routers
urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('property/', include(('property.urls', 'property'), namespace='property')),
]

#admin property_management
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



admin.site.site_header = "ANGESCO"
admin.site.site_title = "Gestión Inmobiliaria Portal"
admin.site.index_title = "Bienvenido al portal de Gestión Inmobiliaria ANGESCO"
