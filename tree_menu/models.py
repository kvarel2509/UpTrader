from django.db import models


class Menu(models.Model):
	name = models.SlugField(
		verbose_name='обозначение',
		unique=True,
	)
	title = models.CharField(
		verbose_name='название',
		max_length=255
	)
	description = models.TextField(
		verbose_name='описание',
		blank=True
	)

	def __str__(self) -> str:
		return self.name


class MenuItem(models.Model):
	title = models.CharField(
		verbose_name='название',
		max_length=255
	)
	menu = models.ForeignKey(
		verbose_name='меню',
		to=Menu,
		on_delete=models.CASCADE,
		related_name='menu_items'
	)
	parent = models.ForeignKey(
		verbose_name='родитель',
		to='self',
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
		related_name='children'
	)
	link = models.TextField(
		verbose_name='адрес ссылки',
	)

	def __str__(self) -> str:
		return self.title
