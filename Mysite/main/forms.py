# make this for customizing the form given by django otherwise we need to 
#create this file

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")

    def save(self, commit=True):
        user = super(NewUserCreationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']

        if commit: 
            user.save()
        
        return user
