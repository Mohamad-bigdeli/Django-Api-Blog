from django.urls import path
from . import views

app_name = "api-v1"

urlpatterns = [
    path("posts/", views.postList, name="post-list"),
    path("posts/<int:id>/", views.postDetail, name="post-detail"),

]