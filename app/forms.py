from django import forms
from .models import *
import uuid
from django.contrib.auth  import get_user_model

User = get_user_model()
from django.contrib.auth.forms import UserCreationForm    
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


    def clean_email(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username Already exits ")
        return username



