import datetime

from django import forms
from .models import Advert


class PostForm(forms.ModelForm):
    """
    Форма для создания объявления
    """
    def clean_price(self):
        """
        проверяем, что цена не отрицательная
        """
        data = self.cleaned_data['price']
        if data < 0:
            raise forms.ValidationError("Sorry, the price is so low!")
        return data

    def clean_year(self):
        """
        проверяем, что год выпуска авто не меньше 1900,
        и не больше текущего года
        """
        data = self.cleaned_data['year']
        now = datetime.datetime.now()
        if data > now.year or data < 1900:
            raise forms.ValidationError("Type correct year!")
        return data

    class Meta:
        """
        подключаем модель и поля для объявления
        """
        model = Advert
        fields = ('maker', 'automodel', 'body', 'color', 'year', 'price',
                  'pic', 'phone', 'status')


class LoginForm(forms.Form):
    """
    форма для авторизации
    """
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15)


class ForGroupForm(forms.ModelForm):
    """
    форма админки для модераторов
    """
    class Meta:
        model = Advert
        fields = ('status',)
