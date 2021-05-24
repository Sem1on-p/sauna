from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
	path('catalog', views.catalog, name='catalog'),
	path('price', views.price, name='price'),
]