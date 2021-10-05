from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, TemplateView
from .models import Userpost, Like
from django.http import JsonResponse
from posts import forms
from .forms import RegistrationForm, LoginForm, PostDetails



def index(request):
    return render(request, "base.html")


class PostView(ListView):
    model = Userpost
    template_name = "post.html"
    context_object_name = "posts"


def post_upload(request):
    form = PostDetails()
    if request.is_ajax():
        form = PostDetails(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'post.html', {'form': form})


# class UploadView(TemplateView):
#     form_class = forms.PostDetails
#     model = Userpost
#     template_name = "upload.html"
#     context = {}
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         self.context["form"] = form
#         return render(request, self.template_name, self.context)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("userpost")


def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Userpost.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'
        like.save()

    return redirect("userpost")


def registration(request):
    form = RegistrationForm()
    context = {"form": form}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"] = form
            return render(request, "registration.html", context)

    return render(request, "registration.html", context)


def signin(request):
    form = LoginForm()
    context = {"form": form}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                context = {"form": form}
                return render(request, "login.html", context)

    return render(request, "login.html", context)


def signout(request):
    logout(request)
    return redirect("signin")
