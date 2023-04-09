from django.urls import path
from .views import index, index_menu


urlpatterns = [
    path('', index, name='start'),
    path('/<int:menu_id>', index_menu, name='menu'),
]