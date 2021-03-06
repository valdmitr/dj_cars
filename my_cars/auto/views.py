from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.forms import User, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.views import generic

from .models import Advert
from .forms import PostForm, LoginForm


class IndexView(generic.ListView):
    """
    Главная страница со списком объявлений
    """
    template_name = 'auto/index.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Advert.objects.filter(day__lte=timezone.now()).order_by('-day')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = auth.get_user(self.request).username
        return context


# @transaction.atomic
class DetailView(generic.DetailView):
    """
    Детальное описание выбранного объявления
    """
    model = Advert
    template_name = 'auto/detail.html'
    context_object_name = 'ad'

    # with transaction.atomic():
    #     pass
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = auth.get_user(self.request).username
        return context


@login_required
def post_new(request):
    """
    Создание нового поста
    """
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
    return render(request, 'auto/new_post_and_edit.html',
                  {'form': form, 'username': auth.get_user(request).username})


def edit(request, pk):
    """
    Редактирование существующего поста
    """
    post = get_object_or_404(Advert, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user = request.user
            post.save()
            return redirect('auto:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'auto/new_post_and_edit.html',
                  {'form': form, 'username': auth.get_user(request).username})


def login(request):
    """
    Авторизация пользователя
    """
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
    """
    Разлогируем пользователя
    """
    auth.logout(request)
    return redirect("/")


def register(request):
    """
    Регистрируем пользователя
    """
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


class MyPostsView(generic.ListView):
    """
    Список постов пользователя
    """
    template_name = 'auto/my_posts.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Advert.objects.filter(ad_user=self.request.user).order_by('-day')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = auth.get_user(self.request).username
        return context


# def error404(request, exception):
#    return page_not_found(request, exception, template_name='auto/404.html')
#     return render(request,'404.html', status=404)
    #return HttpResponseNotFound(render(request,'auto/404.html')
