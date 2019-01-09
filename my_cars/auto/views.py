from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.forms import User, UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Maker, AutoModel, Color, Body, Person, Advert, MakerAndModel
from .forms import PostForm, LoginForm


def index(request):
    ads = Advert.objects.filter(day__lte=timezone.now()).order_by('-day')
    return render(request, 'auto/index.html',
                  {'ads':ads, 'username': auth.get_user(request).username})

# @transaction.atomic
def detail(request, pk):
    # with transaction.atomic():
    #     pass
    ad = get_object_or_404(Advert, pk=pk)
    return render(request, 'auto/detail.html',
                  {'ad':ad, 'username': auth.get_user(request).username})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user = request.user
            post.day = timezone.now()
            post.save()
            return redirect('auto:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'auto/new_post_and_edit.html', {'form': form})


def edit(request, pk):
    post = get_object_or_404(Advert, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user = request.user
            post.day = timezone.now()
            post.save()
            return redirect('auto:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'auto/new_post_and_edit.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'auto/login.html',
                              {'login_error': 'Пользователь не найден'})

    else:
        return render(request, 'auto/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = auth.authenticate(username=form.cleaned_data['username'],
                                         password=form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'auto/register.html', {'form': form})