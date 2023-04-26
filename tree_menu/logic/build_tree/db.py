from tree_menu.models import MenuItem


def get_menu_items(menu_name: str):
    return MenuItem.objects.filter(menu__name=menu_name)
