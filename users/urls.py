from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (CustomLoginView, UserCreateView, UserProfileDetailView, UserProfileUpdateView,
                         email_verification)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", CustomLoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("profile/", UserProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/", UserProfileUpdateView.as_view(), name="profile_update"),
]
