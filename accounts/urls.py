from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('create_auth_token/', auth_views.obtain_auth_token),
]