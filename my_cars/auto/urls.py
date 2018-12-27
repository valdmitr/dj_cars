from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'auto'
urlpatterns = [
    path('', views.index, name='index'),
    path('auto/<int:pk>/', views.detail, name='detail'),
    path('auto/<int:pk>/edit/', views.edit, name='edit'),
    path('auto/new/', views.post_new, name='post_new'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)