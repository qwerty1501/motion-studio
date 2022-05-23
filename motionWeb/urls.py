from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls
from . import settings


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('motionApp.urls')),
    path('', include('feedback.urls')),
    path('', include('clientApp.urls')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
] 

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)