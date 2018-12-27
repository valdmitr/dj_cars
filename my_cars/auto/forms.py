from django import forms
from .models import Advert

class PostForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('maker', 'automodel', 'body', 'color', 'year', 'price', 'ad_user', 'pic')