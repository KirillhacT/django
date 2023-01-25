from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comments, Example_Models
from .form import CommentsForm, RegisterUserForm, LoginUserForm, AddPostForm

from .utils import *

# class PostView(View):
#     """"Вывод записи"""
#     def get(self, request):
#         posts = Post.objects.all()
#         template = 'blog/index.html'
#         context = {
#             "post_list": posts
#         }
#         return render(request, template, context=context)

class PostView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    def get_queryset(self):
        return Post.objects.all()


# class PostDetail(View):
#     """отдельная страница записи"""
#     def get(self, request, slug):
#         post = Post.objects.get(slug=slug)
#         template = 'blog/blog_detail.html'
#         list_of_comments = Comments.objects.filter(post=post)
#         context = {
#             "post": post,
#             "list_of_comments": list_of_comments
#         }
#         return render(request, template, context=context)

class PostDetail(ListView):
    model = Post
    template_name = "blog/blog_detail.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_of_comments"] = Comments.objects.filter(post=context["post"])
        return context
    def get_queryset(self):
        return Post.objects.get(slug=self.kwargs.get("slug"))

class AddComments(View):
    """Добавление комментариев"""
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f"/{pk}")

        # print(f"{request.POST}")
        # return redirect("/")

# class AddPost(CreateView):
#     form_class = AddPostForm
#     template_name = "blog/add_post.html"
#     context_object_name = "form"
#     success_url = reverse_lazy('home')

class AddPost(ListView):
    model = Post
    template_name = "blog/add_post"













#Slug example
class Example(DataMixin, ListView):
    model = Example_Models
    template_name = "example/example.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs): #Динамический контекст
        context = super().get_context_data(**kwargs)
        # context["example"] = "EXAMPLE"
        #MIXIN
        c_def = self.get_user_context(title="Главная")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self): #По какому критерию отбира  ем
        return Example_Models.objects.all()


    #Реализация Example_Detail на ListView
    # def get_queryset(self):
    #     return Example_Models.objects.get(slug=self.kwargs["slug"])

    # class Example(View):
    #     #View
    #     def get(self, request):
    #         posts = Example_Models.objects.all()
    #         template = "example/example.html"
    #         context = {
    #             "posts": posts
    #         }
    #         return render(request, template, context)


class Example_Detail(DataMixin, DetailView):
    model = Example_Models
    template_name = "example/example_detail.html"
    context_object_name = "post"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #В контексте обращаемся к конкретному посту и вытаскиваем из него name
        c_def = self.get_user_context(title=context["post"].name)
        return dict(list(context.items()) + list(c_def.items()))

# class Example_Detail(View):
#     #View
#     def get(self, request, slug):
#         post = Example_Models.objects.get(slug=slug)
#         template = "example/example_detail.html"
#         context = {
#             "post": post
#         }
#         return render(request, template, context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "example/register.html"
    context_object_name = "form"
    success_url = reverse_lazy('login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/example/")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "example/login.html"
    context_object_name = "form"
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        context.update(c_def)
        return context
        # return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy("home")

def logout_user(request):
    logout(request)
    return redirect("/example/")










