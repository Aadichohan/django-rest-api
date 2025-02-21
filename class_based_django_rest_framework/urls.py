from django.contrib import admin
from django.urls import path, include
from class_based_django_rest_framework.Views.Book.BookView import  BookView
from class_based_django_rest_framework.Views.Book.BookViewSet import  BookViewSet
# from e_commerce.ModelViews.User import User

urlpatterns = [
     path('books-view-rest/', view=BookView.as_view(), name='book-list'),
     path('books-view-rest/<int:book_id>/', BookView.as_view(), name='book-detail')
    #  path('books-viewset-rest/', view=BookViewSet.as_view(), name='book-list'),
]