from django.contrib import admin
from django.urls import path, include

from django.conf import settings, views
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('age_app', include('age_app.urls')),
    path('', views.AgePredictionView)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
