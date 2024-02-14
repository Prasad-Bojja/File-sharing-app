from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UploadFiles.as_view(), name='upload_files'),
    path('download_file/<uuid:uid>/', Download, name='download_file'),
    path('download_folder/<uuid:uid>/', DownloadFolder.as_view(), name='download_folder'),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()