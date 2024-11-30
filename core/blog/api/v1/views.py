# from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import CustomPagination

"""@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""
# -----------------------------------------------------------------------------------------------------
'''class PostList(APIView):
    """
    getting a list of posts and creating new post.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        """retrieving a list of posts."""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """creating a post with provided data."""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''
# -----------------------------------------------------------------------------------------------------
'''class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    getting a list of posts and creating new post.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retrieving a list of posts."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """creating a post with provided data."""
        return self.create(request, *args, **kwargs)'''


# -----------------------------------------------------------------------------------------------------
class PostList(ListCreateAPIView):
    """
    getting a list of posts and creating new post.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# -----------------------------------------------------------------------------------------------------
"""@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successful"}, status=status.HTTP_204_NO_CONTENT)"""
# -----------------------------------------------------------------------------------------------------
'''class PostDetail(APIView):
    """getting detail of post and edit plus removing it."""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retrieving the post data."""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        """editing the post data."""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
    def delete(self, request, id):
        """deleting the post object."""
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"item removed successful"}, status=status.HTTP_204_NO_CONTENT)'''
# -----------------------------------------------------------------------------------------------------
'''class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """getting detail of post and edit plus removing it."""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retrieving the post data."""
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        """editing the post data."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """deleting the post object."""
        return self.destroy(request, *args, **kwargs)'''


# -----------------------------------------------------------------------------------------------------
class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting detail of post and edit plus removing it."""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# -----------------------------------------------------------------------------------------------------
# Example for ViewSet in CBV
class PostModelViewSet(ModelViewSet):
    """getting a list and detail of posts and
    creating new post and post and edit plus removing post."""

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author", "status"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = CustomPagination

    # @action(detail=False, methods=["get"])
    # def get_ok(self, request):
    #     return Response({"detail":"ok"})


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
