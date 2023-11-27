# for image loading use less >>>>
from django.conf import settings
from django.conf.urls.static import static
# 
from django.contrib import admin
from django.urls import path,include
from core.views import index,baser,contact
 

urlpatterns = [
    path('main/',include('core.urls')),
    # this is the path from this the file in core:urls will find the next path format....
    path('bs/',baser,name='codeBase' ),
    path('admin/', admin.site.urls),

    path('items/',include('item.urls'))
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
