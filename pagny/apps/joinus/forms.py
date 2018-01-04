from django import forms
from .models import Client

class joinusform(forms.ModelForm):
    class Meta:
        model=Client

        fields=[
            'firstname',
            'surname',
            'birth',
            'marital',
            'children',
            'housenum',
            'street',
            'postalcode',
            'username',
            'password',
            'pin',
            'email',
            'telnum',
        ]
        labels = {
            'firstname':'First Name',
            'surname' : 'Surname',
            'birth' : 'Day of birth',
            'marital': 'Marital Status',
            'children':'Number of children',
            'housenum' :'House number',
            'street': 'Street',
            'postalcode': 'Postal Code',
            'username':'Username',
            'password':'Password',
            'pin':'Pin',
            'email':'Email',
            'telnum':'Telephone number',
        }
        widgets ={
            'firstname' : forms.TextInput(attrs={'class' :'form-control'}),
            'surname': forms.TextInput(attrs={'class' :'form-control'}),
            'birth': forms.TextInput(attrs={'class' :'form-control'}),
            'marital': forms.TextInput(attrs={'class' :'form-control'}),
            'children': forms.TextInput(attrs={'class' :'form-control'}),
            'housenum': forms.TextInput(attrs={'class' :'form-control'}),
            'street': forms.TextInput(attrs={'class' :'form-control'}),
            'postalcode': forms.TextInput(attrs={'class' :'form-control'}),
            'username': forms.TextInput(attrs={'class' :'form-control'}),
            'password': forms.TextInput(attrs={'class' :'form-control'}),
            'pin': forms.TextInput(attrs={'class' :'form-control'}),
            'email': forms.TextInput(attrs={'class' :'form-control'}),
            'telnum': forms.TextInput(attrs={'class' :'form-control'}),
        }