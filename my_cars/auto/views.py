from django.shortcuts import render, get_object_or_404

from .models import Maker, AutoModel, Color, Body, Person, Advert, MakerAndModel

from django.utils import timezone

def index(request):
    ads = Advert.objects.filter(day__lte=timezone.now()).order_by('-day')
    return render(request, 'auto/index.html', {'ads':ads})


def detail(request, pk):
    ad = get_object_or_404(Advert, pk=pk)
    return render(request, 'auto/detail.html', {'ad':ad})

def edit(request):
    return "edit this one"