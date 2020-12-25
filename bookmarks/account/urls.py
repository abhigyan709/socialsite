from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # previous logn view
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]