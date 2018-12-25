from django.shortcuts import render

from .models import Maker, AutoModel, Color, Body, Person, Advert, MakerAndModel

from django.utils import timezone

def index(request):
    ads = Advert.objects.filter(day__lte=timezone.now()).order_by('-day')
    return render(request, 'auto/index.html', {'ads':ads})


def detail(request):
    return "Hi!"

def edit(request):
    return "edit this one"