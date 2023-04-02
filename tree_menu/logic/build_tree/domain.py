from tree_menu import models
from tree_menu.logic.convert.convert_link import convert_link
from tree_menu.logic.build_tree import entities


def get_menu_item_models(menu_name: str):
    return models.MenuItem.objects.filter(menu__name=menu_name)


def build_tree(menu_name: str, curr_link: str):
    root = entities.MenuItem(title=menu_name, visible=True)
    menu_item_models = get_menu_item_models(menu_name)
    menu_items_map = {}
    active_menu_items = []

    # заполнение карты элементов меню и пополнение списка активных пунктов
    # у которых ссылка совпадает с адресом текущей страницы
    for menu_item_model in menu_item_models:
        menu_item_entity = entities.MenuItem(
            title=menu_item_model.title,
            link=convert_link(menu_item_model.link)
        )
        print(menu_item_entity.link)
        menu_items_map[menu_item_model.pk] = menu_item_entity
        if menu_item_entity.link == curr_link:
            menu_item_entity.active = True
            active_menu_items.append(menu_item_entity)
    
    # создание связей между элементами меню для образования древовидной структуры
    # во главе с элементом root
    for menu_item_model in menu_item_models:
        menu_item_entity = menu_items_map[menu_item_model.pk]
        if menu_item_model.parent_id is not None:
            parent_entity = menu_items_map[menu_item_model.parent_id]
        else:
            parent_entity = root
        menu_item_entity.parent = parent_entity
        parent_entity.add_child(menu_item_entity)

    # установка флага видимости элементов меню первого уровня независимо от того, есть ли в меню активный элемент
    for child in root.children:
        child.visible = True

    # установка флага развернутости элемента меню для всех активных пунктов
    for active_menu_item in active_menu_items:
        popup = active_menu_item
        for child in popup.children:
            child.visible = True
        while popup.parent is not None:
            for child in popup.parent.children:
                child.visible = True
            popup = popup.parent

    return root
