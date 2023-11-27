from django.shortcuts import render

from item.models import Catgory,Item

from .forms import signUpForm

# Create your views here.
def index(request):
    allitems=Item.objects.filter(is_sold=False)
    cats=Catgory.objects.all()

    return render(request,'core/index.html',{
        'items':allitems,
        'cats':cats
    })


def baser(request):
    return render(request,'core/base.html')

def contact(request):
    return render(request,'core/contact.html')

















