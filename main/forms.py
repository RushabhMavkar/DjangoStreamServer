from django import forms
from . import models
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class Signup(forms.Form):
    name = forms.CharField(label='Name')
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class CreateServer(ModelForm):
    class Meta:
        model = models.Server
        exclude = ['admin']
