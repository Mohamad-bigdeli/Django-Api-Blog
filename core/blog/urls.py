from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    # path("cbv-view/", views.IndexView.as_view(), name="index"),
    # path("go-to-my-github/", views.RedirectToMyGithub.as_view(), name="redirect-github"),
    path("posts/", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", views.PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/edit", views.PostEditView.as_view(), name="post-edit"),
    path(
        "posts/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
