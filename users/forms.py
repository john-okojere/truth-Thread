from django import forms
from .models import User, ProfilePic, About
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    date_of_birth = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    class Meta:
        model = User
        fields = ("username","first_name","last_name","phone","gender","email",'date_of_birth',"password1","password2")
    

class EditRegisterForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    class Meta:
        model = User
        fields = ("first_name","last_name","phone","gender","email",'date_of_birth')
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = ('image',)

class BioForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('country','state','address','about')
