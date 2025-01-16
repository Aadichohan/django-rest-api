from django.contrib import admin
from django.urls import path, include
from e_commerce import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('book/', view=views.book, name='book'),
    path('author/', view=views.author, name='author'),
    path('categories/', view=views.categories, name='categories')
]
