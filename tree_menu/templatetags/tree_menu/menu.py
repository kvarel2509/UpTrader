from django import template

from tree_menu.logic.build_tree.domain import build_tree


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    curr_link = context['request'].build_absolute_uri()
    root = build_tree(menu_name, curr_link)
    return {"root": root}


@register.inclusion_tag('tree_menu/menu_item.html')
def draw_menu_item(item):
    return {"menu_item": item}
