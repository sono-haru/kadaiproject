from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        # デフォルトでusername,password1,password2(emailも追加)
        fields=('username','email','password1','password2')