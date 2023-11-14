from django.contrib import admin

# Register your models here.
from .models import Catgory,Item


admin.site.register(Catgory)
admin.site.register(Item)


