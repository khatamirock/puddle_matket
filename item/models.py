from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Catgory(models.Model):
    name= models.CharField(max_length=255)
    
    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name


class Item(models.Model):

    def __str__(self) -> str:
        return (self.name," -- ",self.category," -- $",self.price)

    category=models.ForeignKey(Catgory,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    desc=models.TextField(blank=True,null=True)
    price=models.FloatField()
    is_sold=models.BooleanField(default=False)
    created=models.TimeField(auto_now_add=True)
    img=models.ImageField(upload_to='item_img',blank=True,null=True) #this 'item_img' should be the name of the folder and it
    # should be the same in settings.py under `static` files declaration
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)