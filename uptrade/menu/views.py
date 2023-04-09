from django.shortcuts import render
from .models import MenuName

# Create your views here.
def index(request):
    menu = MenuName.objects.all()
    context = {
        'menu': menu
    }
    return render(request, 'index.html', context)

def index_menu(request, menu_id):
    menu = MenuName.objects.all()
    context = {
        'menu': menu
    }
    return render(request, 'index.html', context)