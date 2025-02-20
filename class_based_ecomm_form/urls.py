from django.contrib import admin
from django.urls import path, include
from class_based_ecomm_form.views import BookView


urlpatterns = [
     path('books/', view=BookView.as_view(), name='book-list'),
]