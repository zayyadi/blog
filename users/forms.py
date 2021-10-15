from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, NewUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserRegisterForm:
    email = forms.EmailField()

    class Meta:
        model = NewUser
        fields =  ['username', 'email','first_name','username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = NewUser
        fields = ['username', 'email']