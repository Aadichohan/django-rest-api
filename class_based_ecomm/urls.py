from django.contrib import admin
from django.urls import path, include
from class_based_ecomm.views import BookView
from e_commerce.ModelViews.User import User

urlpatterns = [
     path('books/', view=BookView.as_view(), name='book-list'),
]