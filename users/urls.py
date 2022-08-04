from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path("validate_username/", views.validate_username, name="validate_username"),
    path("view_profile", views.view_profile, name="view_profile"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
    path("settings/password/", views.password, name="password"),
    path("social", views.social, name="social"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path(
        "activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",
        views.activate,
        name="activate",
    ),
]
