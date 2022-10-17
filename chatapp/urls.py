from django.urls import path, re_path
from chatapp.views import *

urlpatterns = [
    re_path(r"^$", HomeView.as_view(), name="home"),
]