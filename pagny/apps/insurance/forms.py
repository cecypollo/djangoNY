from django import forms
from .models import Insurance

class insuranceform(forms.ModelForm):
    class Meta:
        model=Insurance

        fields=[
            'add1',
            'add2',
            'time',
            'value',
            'finishes',
            'domestichelp',
        ]
        labels = {
            'add1':'Address 1',
            'add2':'Address 2',
            'time':'When was the last time you shopped your policy?',
            'value':'What is the estimated value of your contents?',
            'finishes': 'Does your house have above standard finishes?',
            'domestichelp': 'Do you have full-time domestic help?',

        }
        widgets ={
            'add1' : forms.TextInput(attrs={'class' :'form-control'}),
            'add2': forms.TextInput(attrs={'class' :'form-control'}),
            'time': forms.TextInput(attrs={'class' :'form-control'}),
            'value': forms.TextInput(attrs={'class' :'form-control'}),
            'finishes': forms.TextInput(attrs={'class' :'form-control'}),
            'domestichelp': forms.TextInput(attrs={'class' :'form-control'}),
        }
