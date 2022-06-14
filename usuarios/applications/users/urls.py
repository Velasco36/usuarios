
from django.urls import path, include

from . import views

app_name = 'users_apps'

urlpatterns = [
    path('register/',views.UserRegiisterView.as_view(), name='register'),
    path('login/',views.LoginUser.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('update/',views.UpdatePasswordView.as_view(), name='update')
]
