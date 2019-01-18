from django.conf.urls import handler404
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
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('auth/register/', views.register, name='register'),
    path('auto/my_posts/', views.MyPostsView.as_view(), name='my_posts'),
]

# handler404 = 'auto.views.error404'
# handler404 = views.error404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
