from django import forms
from .models import *

class AddPostForm(forms.Form):
    userName = forms.CharField(required= True, max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Ім\'я'}))
    telephone = forms.IntegerField(required= True, min_value=380000000000, max_value=380999999999, widget=forms.NumberInput(attrs={'placeholder': 'Номер телефону'}))
    countryName = forms.CharField(required= True,max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Назва країни'}))
    capitalName = forms.CharField(required= True,max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Столиця'}))
    area = forms.IntegerField(required= False, min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Площа'}))
    img = forms.ImageField(required= False, label="Зображення")
    inputArea = forms.CharField(required= False,max_length=255,widget=forms.Textarea(attrs={'placeholder': 'Інфо', 'cols' : 150, 'rows' : 7, 'class' : "input_area"}))
