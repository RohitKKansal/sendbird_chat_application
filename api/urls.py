from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path("all_users/", views.list_all_users, name="users"),
    path("get_single_user/", views.get_single_user, name="get_single_user"),
    path("create_user/", views.create_user, name="create_user"),
    path("update_user/<str:user_id>/", views.update_user, name="update_user"),
    path("delete_user/<str:user_id>/", views.delete_user, name="delete_user"),
]
