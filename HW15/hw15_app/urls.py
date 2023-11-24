from django.urls import path
from . import views

app_name = 'home_page'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
]
