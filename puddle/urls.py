# for image loading use less >>>>
from django.conf import settings
from django.conf.urls.static import static
# 
from django.contrib import admin
from django.urls import path
from core.views import index
from core.views import baser
from core.views import contact
urlpatterns = [
    path('',index,name='index'),
    path('bs/',baser,name='codeBase' ),
    path('contact/',contact,name='contact' ),# need he name for mentions in {%this form%}
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
