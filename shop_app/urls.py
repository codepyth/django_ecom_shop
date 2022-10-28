import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('', views.cart, name='cart'),
]