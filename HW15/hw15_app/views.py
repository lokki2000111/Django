from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, ListView

from .forms.registration import RegistrationForm
from .models import Info, Post

# Create your views here
info = Info.objects.all()


def main_page(request):
    return render(request, 'main_page.html', context={'info': info})


def first(request):
    return render(request, 'first.html', context={'info': info})


def second(request):
    return render(request, 'second.html', context={'info': info})


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegistrationForm
    return render(request, 'registration_form.html', context={'reg_form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class Profile(View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)

        return render(request, 'profile.html', context={'user': user})


class ProfileUpdate(UpdateView):
    model = User
    template_name = 'update_profile.html'
    fields = ['first_name', 'last_name']

    def get_success_url(self):
        return reverse_lazy('profile')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public']


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')  # замените на имя вашего представления списка постов
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def get_posts(request):
    posts = Post.objects.order_by('-id').all()
    return render(request, 'posts.html', context={'posts': posts})
