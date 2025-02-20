from django.contrib import admin
from django.urls import path, include
from class_based_ecomm.views import BookView
from e_commerce.ModelViews.User import User

urlpatterns = [
     path('books/', view=BookView.as_view(), name='book-list'),
    # path('add_author/', view=addAuthor, name='add_author'),
    # path('update_author/<int:id>/', view=updateAuthor, name='update_author'),
    # path('get_author/<int:id>/', view=getAuthor, name='get_author'),
    # path('get_authors/', view=getAuthors, name='get_authors'),

    # path('add_category/', view=addCategory, name='add_category'),
    # path('update_category/<int:id>/', view=updateCategory, name='update_category'),
    # path('get_category/<int:id>/', view=getCategory, name='get_category'),
    # path('get_categories/', view=getCategories, name='get_categories'),

    # path('add_book/', view=addBook, name='add_book'),
    # path('update_book/<int:id>/', view=updateBook, name='update_book'),
    # path('get_book/<int:id>/', view=getBook, name='get_book'),
    # path('get_books/', view=getBooks, name='get_book_list'),
   
]