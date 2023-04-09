from django import template
from menu.models import MenuName

register = template.Library()

@register.inclusion_tag('custom_tags/my_tag.html')
def my_tag_menu():
    menu = MenuName.objects.all()
    return {'menu': menu}
