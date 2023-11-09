 
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
]
