from django import forms
from .models import Advert

class PostForm(forms.ModelForm):

    def clean_price(self):
        data = self.cleaned_data['price']
        if data < 0:
            raise forms.ValidationError("Sorry, the price is so low!")
        return data

    def clean_year(self):
        data = self.cleaned_data['year']
        if data>2019 or data<1900:
            raise forms.ValidationError("Type correct year!")
        return data

    class Meta:
        model = Advert
        fields = ('maker', 'automodel', 'body', 'color', 'year', 'price', 'pic', 'phone', 'status')




class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15)



class ForGroupForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ('status',)