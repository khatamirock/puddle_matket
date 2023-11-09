from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')


def baser(request):
    return render(request,'core/base.html')

def contact(request):
    return render(request,'core/contact.html')