from django import forms
from .models import Userpost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostDetails(forms.ModelForm):
    class Meta:
        model=Userpost
        fields=["author","post_content"]
        widgets = {
            "author":forms.Select(attrs={"class":"form-select"}),
            "post_content": forms.Textarea(attrs={"class": "form-control"}),
            }

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
