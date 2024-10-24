from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("validate_username/", views.validate_username, name="validate_username"),
    path(
        "password_reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        views.custom_password_reset_done,
        name="password_reset_done",
    ),
    path(
        "password_reset/complete/",
        views.custom_password_reset_complete,
        name="password_reset_complete",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("view_profile", views.view_profile, name="view_profile"),
    # path("profile/", views.profile, name="profile"),
    path("settings/", views.setting, name="settings"),
    path("settings/password/", views.password, name="password"),
    path("social", views.social, name="social"),
    path(
        "login/",
        views.MyLoginView.as_view(),
        name="login",
    ),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    # path(
    #     "activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",
    #     views.activate,
    #     name="activate",
    # ),
]
