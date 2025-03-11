from django.urls import path
from .views import register, login_user, logout_user, profile, profile_update

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile-update/", profile_update, name="profile_update"),
]
