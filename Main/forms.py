from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#creating required forms

class EmpRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1','password2']