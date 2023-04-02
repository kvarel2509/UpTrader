from django.db import migrations

def add_data(apps, schema_editor):
    Menu = apps.get_model('tree_menu', 'Menu')
    MenuItem = apps.get_model('tree_menu', 'MenuItem')
    
    world_place = Menu(name='world_place', title='Места')
    kitchen = Menu(name='kitchen', title='Кухни')
    Menu.objects.bulk_create([world_place, kitchen])

    america_place = MenuItem(title='Америка', menu=world_place, link='http://localhost:8000/america/')
    europe_place = MenuItem(title='Европа', menu=world_place, link='http://localhost:8000/europe/')
    asia_kitchen = MenuItem(title='Азиатская кухня', menu=kitchen, link='http://localhost:8000/asia/')
    europe_kitchen = MenuItem(title='Европейская кухня', menu=kitchen, link='http://localhost:8000/europe/')
    MenuItem.objects.bulk_create([
        america_place,
        europe_place,
        asia_kitchen,
        europe_kitchen
    ])

    canada_place = MenuItem(title='Канада', menu=world_place, parent=america_place, link='http://localhost:8000/canada/')
    russia_place = MenuItem(title='Россия', menu=world_place, parent=europe_place, link='http://localhost:8000/russia/')
    uk_place = MenuItem(title='UK', menu=world_place, parent=europe_place, link='http://localhost:8000/uk/')
    russia_kitchen = MenuItem(title='Российская кухня', menu=kitchen, parent=europe_kitchen, link='russia')
    china_kitchen = MenuItem(title='Китайская кухня', menu=kitchen, parent=asia_kitchen, link='http://localhost:8000/china/')
    MenuItem.objects.bulk_create([
        canada_place,
        russia_place,
        uk_place,
        russia_kitchen,
        china_kitchen
    ])

    london_place = MenuItem(title='Лондон', menu=world_place, parent=uk_place, link='london')
    moscow_place = MenuItem(title='Москва', menu=world_place, parent=russia_place, link='https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0')
    MenuItem.objects.bulk_create([
        london_place,
        moscow_place,
    ])


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('tree_menu', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_data),
    ]