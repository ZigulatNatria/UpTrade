from django import template
from menu.models import MenuName

register = template.Library()

@register.inclusion_tag('custom_tags/my_tag2.html')
def my_tag_menu(sort=None, menu_selected=0):
    if not sort:
        menu = MenuName.objects.all()
    else:
        menu = MenuName.objects.order_by(sort)
    return {'menu': menu, 'menu_selected': menu_selected}
