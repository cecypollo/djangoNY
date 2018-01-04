from django import forms
from .models import ClientSignIn

class signinform(forms.ModelForm):
    class Meta:
        model=ClientSignIn

        fields=[
            'username',
            'password',
        ]
        labels = {
            'username':'Username',
            'password' : 'Password',
        }
        widgets ={
            'username' : forms.TextInput(attrs={'class' :'form-control'}),
            'password': forms.TextInput(attrs={'class' :'form-control'}),
        }