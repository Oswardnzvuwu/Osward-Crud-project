from.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}))
    password1 = forms.CharField(label='', max_length=100,help_text='must be at 8 characters including letters and digits', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    
    class Meta:
        model =User
        fields =['username','email','password1','password2']


class AddEmployeeForm(ModelForm) :
    class Meta:
        model =Employee

        fields =['ename', 'desg','salary']

        label = {
            'ename': '',
            'desg':'',
            'salary':'',

        }
        
        widgets = {
            'ename': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name',}),
            'desg': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Designation',}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Salary',}),
            }

