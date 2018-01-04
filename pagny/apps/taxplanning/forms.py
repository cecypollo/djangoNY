from django import forms
from .models import TaxP

class taxform(forms.ModelForm):
    class Meta:
        model=TaxP

        fields=[
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
        ]
        labels = {
            'q1':'Question 1',
            'q2': 'Question 2',
            'q3': 'Question 3',
            'q4': 'Question 4',
            'q5': 'Question 5',
        }
        widgets ={
            'q1' : forms.TextInput(attrs={'class' :'form-control'}),
            'q2': forms.TextInput(attrs={'class' :'form-control'}),
            'q3': forms.TextInput(attrs={'class': 'form-control'}),
            'q4': forms.TextInput(attrs={'class': 'form-control'}),
            'q5': forms.TextInput(attrs={'class': 'form-control'}),
        }