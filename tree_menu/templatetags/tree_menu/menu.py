from django import template

from tree_menu.logic.build_tree.domain import get_menu

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    curr_link = context['request'].build_absolute_uri()
    menu = get_menu(menu_name, curr_link)
    return {"root": menu}


@register.inclusion_tag('tree_menu/menu_item.html')
def draw_menu_item(item):
    return {"menu_item": item}
