from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app import views as app_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('app.urls')),
    path('terminal/', app_views.terminal, name='terminal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
