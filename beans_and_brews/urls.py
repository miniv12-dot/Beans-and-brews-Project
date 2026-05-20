from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.get_admin_path() if hasattr(admin.site, 'get_admin_path') else admin.site.urls), # standard admin path
    path('', include('menu.urls')),
]

# NEW: Append media routing helper so uploaded images can be viewed in the browser
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)