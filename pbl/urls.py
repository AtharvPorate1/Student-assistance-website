
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include



urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include("base.urls")),

    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
    
    
]
# urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)