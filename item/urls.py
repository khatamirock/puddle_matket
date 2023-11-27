from django.urls import path
from . import views #more effective for including all views 
# from views import detail #have to include 1by1

app_name='item'

urlpatterns=[
    path(
        '<int:pk>/',views.detail,name='dtls'

    )
]



