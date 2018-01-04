from django import forms
from .models import estateP

class estateform(forms.ModelForm):
    class Meta:
        model=estateP

        fields=[
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
        ]
        labels = {
            'q1':'Do you understand how your assets will pass at upon your death?',
            'q2': 'Have your estate planning goals changed?',
            'q3': 'Have you acquired major assets?',
            'q4': 'Is there someone you like to disinherit?',
            'q5': 'Are you in a contentious situation?',
        }
        widgets ={
            'q1' : forms.TextInput(attrs={'class' :'form-control'}),
            'q2': forms.TextInput(attrs={'class' :'form-control'}),
            'q3': forms.TextInput(attrs={'class': 'form-control'}),
            'q4': forms.TextInput(attrs={'class': 'form-control'}),
            'q5': forms.TextInput(attrs={'class': 'form-control'}),
        }