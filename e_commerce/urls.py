from django.contrib import admin
from django.urls import path, include
from e_commerce.Views import *
from e_commerce.ModelViews.User import User

urlpatterns = [
    # path('', view=views.index, name='index'),
    path('add_author/', view=addAuthor, name='add_author'),
    path('update_author/<int:id>/', view=updateAuthor, name='update_author'),
    path('get_author/<int:id>/', view=getAuthor, name='get_author'),
    path('get_authors/', view=getAuthors, name='get_authors'),

    path('add_category/', view=addCategory, name='add_category'),
    path('update_category/<int:id>/', view=updateCategory, name='update_category'),
    path('get_category/<int:id>/', view=getCategory, name='get_category'),
    path('get_categories/', view=getCategories, name='get_categories'),

    path('add_book/', view=addBook, name='add_book'),
    path('update_book/<int:id>/', view=updateBook, name='update_book'),
    path('get_book/<int:id>/', view=getBook, name='get_book'),
    path('get_books/', view=getBooks, name='get_book_list'),
   
]


# urlpatterns = [
#     path('', view=views.index, name='index'),
#     path('add_book/', view=views.add_book, name='add_book'),
#     path('get_all_books/', view=views.get_book_list, name='get_book_list'),
#     path('get_book/<int:id>/', view=views.get_book, name='get_book'),
#     path('book/', view=views.book, name='book'),
#     path('add_author/', view=views.add_author, name='add_author'),
#     path('author/', view=views.author, name='author'),
#     path('categories/', view=views.categories, name='categories'),   
# ]



# urlpatterns = [
#     path('my-api/', User.my_api_get_view, name='my-api-get'),  # Route for GET
#     path('my-api/',User.my_api_post_view, name='my-api-post'),  # Route for POST
#     path('my-api/', User.as_view(), name='my-api-get'),  # Route for GET
#     path('my-api/all-users/', User.all_user_data, name='all-users'),  # Route for GET
#     path('my-api/single-users/', User.single_user_data, name='all-users'),  # Route for GET
   
# ]

# urlpatterns = [
# ]
