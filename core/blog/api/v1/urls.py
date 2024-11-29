from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

app_name = "api-v1"

# urlpatterns = [
#     path("posts/", views.postList, name="post-list"),
#     path("posts/", views.PostList.as_view(), name="post-list"),
#     path("posts/<int:id>/", views.postDetail, name="post-detail"),
#     path("posts/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
#     path("posts/", views.PostViewSet.as_view({'get':'list', 'post':'create'}), name="post-list"),
#     path("posts/<int:pk>", views.PostViewSet.as_view({'get':'retrieve', 'put':'update',
#                                 'patch':'partial_update', 'delete':'delete'}), name="post-detail"),
# ]
