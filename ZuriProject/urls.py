from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('', lambda request: redirect('admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('test/', include('testapp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
