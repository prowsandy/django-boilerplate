from django.urls import path
from home.views import *
from django.contrib.auth import views as auth_views

app_name = "home"

urlpatterns = [
    path('', home, name="home"),
    path('profile', Profile.as_view(), name="profile"),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='home/change_password.html',
            success_url = '/accounts/logout/'
        ),
        name='change_password'
    ),
]
