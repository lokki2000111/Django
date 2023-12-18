from django.urls import path
from . import views
from .views import LoginUser, Profile, ProfileUpdate, BaseTemplate, LogoutView, Tags, GetTag

home_page = 'home_page'
posts = 'posts'

urlpatterns = [
    path(f'{home_page}', views.main_page, name='main_page'),
    path('registration', views.registration_page, name='reg_page'),
    path('login', LoginUser.as_view(), name='login'),
    path('profile', Profile.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileUpdate.as_view(), name='update'),
    path(f'{posts}/create', views.create_post, name='create_post'),
    path(f'{posts}', views.get_posts, name='posts'),
    path('base', BaseTemplate.as_view(), name='base'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('tags', Tags.as_view(), name='tags'),
    path('tags/<str:tag>', GetTag.as_view(), name='get_tag'),
]
