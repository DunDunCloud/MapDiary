from django import forms
from .models import Place

class PlaceUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']