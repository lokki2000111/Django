from django.shortcuts import render
from .models import Info


# Create your views here
def main_page(request):
    return render(request, 'main_page.html')


def first(request):
    info = Info.objects.all()
    return render(request, 'first.html', context={'info': info})


def second(request):
    return render(request, 'second.html')
