from django import forms
from django.forms.widgets import TextInput


class SearchForm(forms.Form):
    SearchBox = forms.CharField(label='', max_length=200, widget=TextInput(attrs={
        'class': 'form-control me-2',
        'type': 'search',
        'placeholder': 'Digite a cidade'}))
