from django import forms
from django.contrib.auth.models import User
from .models import *

class RestForm(forms.ModelForm):
 class Meta:
  model=Rest 
  widgets={
   'nombre':forms.TextInput(attrs={'placeholder':'nombre','class' : 'form-control'}),
   'cuisine':forms.TextInput(attrs={'placeholder':'cuisine','class' : 'form-control'}),
   'borough':forms.TextInput(attrs={'placeholder':'borough','class' : 'form-control'}),
   'street':forms.TextInput(attrs={'placeholder':'street','class' : 'form-control'}),
   'building':forms.TextInput(attrs={'placeholder':'building','class' : 'form-control'}),
   'zipcode':forms.TextInput(attrs={'placeholder':'zipcode','class' : 'form-control'}),
   }
  fields = ('nombre','cuisine','borough','street','building','zipcode')
