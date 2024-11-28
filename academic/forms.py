from django import forms
from django.forms import ModelForm
from academic.models import *

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label='Enter name',
        min_length=5,
        widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'your name'})
        )
    email = forms.EmailField(
        label='Enter email',
        widget= forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'enter email'}
        )
    )
    age = forms.IntegerField(
        label='Enter age',
        min_value=18,
        max_value=150,
        widget=forms.NumberInput(attrs={
            'class':'form-control', 'placeholder':'enter age'
        })
    )
    
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'salary']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter name'}),
            'salary' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter salary'})
        }