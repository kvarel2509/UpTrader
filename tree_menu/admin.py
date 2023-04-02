from django.contrib import admin
from tree_menu import models


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ['name', 'title', 'description']


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'menu', 'parent', 'link']
