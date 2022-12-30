from django.urls import path
from .views import dashboard, profile_list,profile,homepage,register

app_name = "dwitter"

urlpatterns = [
    path("",homepage,name="homepage"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("register/",register,name="register"),
]