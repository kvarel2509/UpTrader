from django.urls import path
from django.views import generic


urlpatterns = [
    path('america/', generic.TemplateView.as_view(template_name='example/multi_menu.html'), name='america'),
    path('russia/', generic.TemplateView.as_view(template_name='example/multi_menu.html'), name='russia'),
    path('london/', generic.TemplateView.as_view(template_name='example/single_menu.html'), name='london'),
]
