from tree_menu.logic.build_tree import entities
from tree_menu.logic.build_tree.db import get_menu_items
from tree_menu.logic.convert.convert_link import convert_link


def get_menu(menu_name: str, curr_link: str):
    root = entities.MenuItem(title=menu_name, visible=True)
    models = get_menu_items(menu_name)
    menu_items = {}
    active_menu_items = []

    for model in models:
        menu_item = get_menu_item_from_model(model)
        menu_items[model.pk] = menu_item
        if menu_item.link == curr_link:
            menu_item.active = True
            active_menu_items.append(menu_item)

    for model in models:
        menu_item = menu_items[model.pk]
        if model.parent_id is not None:
            parent_entity = menu_items[model.parent_id]
        else:
            parent_entity = root
        menu_item.parent = parent_entity
        parent_entity.add_child(menu_item)

    for active_menu_item in active_menu_items:
        set_visibility_to_relatives(active_menu_item)

    for child in root.children:
        child.visible = True

    return root


def get_menu_item_from_model(model):
    return entities.MenuItem(
        title=model.title,
        link=convert_link(model.link)
    )


def set_visibility_to_relatives(active_menu_item):
    popup = active_menu_item
    for child in popup.children:
        child.visible = True
    while popup.parent is not None:
        for child in popup.parent.children:
            child.visible = True
        popup = popup.parent
