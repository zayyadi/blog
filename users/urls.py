from django.urls import path

from  . import views

app_name = 'users'

urlpatterns = [
    path('validate_username', views.validate_username, name='validate_username'),
    path('profile/', views.profile, name='profile'), 
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]