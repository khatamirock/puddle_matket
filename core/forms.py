from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class signUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('usernam','email','pass','pass2')
    
    






