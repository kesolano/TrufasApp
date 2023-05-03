from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Vista1', views.Vista1, name='Vista1'),
]