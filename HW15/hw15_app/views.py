from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django import forms
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, ListView

from tags_app.models import Tag
from .forms.registration import RegistrationForm
from .models import Info, Post, Image, PostImage

# Create your views here
info = Info.objects.all()


def main_page(request):
    return render(request, 'main_page.html', context={'info': info, 'user': request.user})


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            return redirect('/profile')
    else:
        form = RegistrationForm
    return render(request, 'registration_form.html', context={'reg_form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('base')


@method_decorator(login_required(login_url='/logout'), name='dispatch')
class Profile(View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return render(request, 'profile.html', context={'user': user})


@method_decorator(login_required(login_url='/logout'), name='dispatch')
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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ImagePostForm(PostForm):
    image = MultipleFileField()

    class Meta(PostForm.Meta):
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
        fields = PostForm.Meta.fields + ['image', 'tag']


def create_post(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            # Создаем и сохраняем объект Post без назначения тегов

            post = Post(
                user=request.user,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                is_public=form.cleaned_data['is_public'],
            )
            post.save()

            # Назначаем теги после сохранения объекта Post
            post.tag.set(form.cleaned_data['tag'])

            # Сохранение изображений
            files = request.FILES.getlist('image')
            for file in files:
                img = Image.objects.create(image=file)
                PostImage.objects.create(images=img, post=post)

            return redirect('posts')

    else:
        form = ImagePostForm()
    return render(request, 'create_post.html', {'form': form})


class PostListView(ListView):
    queryset = Post.objects.order_by('-created_at').all()
    template_name = 'posts.html'
    context_object_name = 'posts'
    http_method_names = ['get']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.all()

        return self.queryset.filter(is_public=True).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = "Посты через PostListView"
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class Tags(View):

    @staticmethod
    def get(request):
        count_tag = Tag.objects.annotate(cnt=Count('post_tags')).order_by('-cnt')

        context = {
            'title': 'Популярные теги',
            'tag': count_tag,
        }
        return render(request, 'popular_tags.html', context)


class GetTag(View):
    @staticmethod
    def get(request, tag):
        existing_tag = Tag.objects.filter(tag_label=tag).first()
        posts_by_tags = Post.objects.filter(tag=existing_tag).all()

        context = {
            'title': f"Посты по тегам: {existing_tag}",
            'posts': posts_by_tags
        }

        return render(request, 'posts.html', context)


class BaseTemplate(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            return render(request, 'base.html', context={'user': user})
        return render(request, 'base.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("base")
