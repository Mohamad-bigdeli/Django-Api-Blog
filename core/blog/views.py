from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from .forms import PostCreateForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

# Create your views here.

# class IndexView(TemplateView):
#     """
#     a class based view to show index page
#     """
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["posts"] = Post.objects.all()
#         return context

# class RedirectToMyGithub(RedirectView):
#     url = "https://github.com/Mohamad-bigdeli"


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Post
    permission_required = "blog.view_post"
    # queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "post"


# class PostCreateView(FormView):
#     template_name = "blog/post_create.html"
#     form_class = PostCreateForm
#     success_url = reverse_lazy("blog:posts")

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    # fields = ["title", "content", "status",
    #            "category", "published_date"]
    success_url = reverse_lazy("blog:posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("blog:posts")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:posts")


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"
