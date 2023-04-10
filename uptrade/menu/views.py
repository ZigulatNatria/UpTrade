from django.shortcuts import render
from .models import MenuName

# Create your views here.
def index(request):
    return render(request, 'index2.html')


def index_menu(request, menu_id):
    return render(request, 'index2.html')