from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Maker, AutoModel, Color, Body, Person, Advert, MakerAndModel
from .forms import PostForm


def index(request):
    ads = Advert.objects.filter(day__lte=timezone.now()).order_by('-day')
    return render(request, 'auto/index.html', {'ads':ads})

# @transaction.atomic
def detail(request, pk):
    # with transaction.atomic():
    #     pass
    ad = get_object_or_404(Advert, pk=pk)
    return render(request, 'auto/detail.html', {'ad':ad})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.ad_user = request.user
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
            # post.ad_user = request.user
            post.day = timezone.now()
            post.save()
            return redirect('auto:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'auto/new_post_and_edit.html', {'form': form})

