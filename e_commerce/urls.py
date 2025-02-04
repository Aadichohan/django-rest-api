from django.contrib import admin
from django.urls import path, include
from e_commerce import views
from e_commerce.ModelViews.User import User

urlpatterns = [
    path('', view=views.index, name='index'),
    path('add_book/', view=views.add_book, name='add_book'),
    path('get_all_books/', view=views.get_book_list, name='get_book_list'),
    path('get_book/<int:id>/', view=views.get_book, name='get_book'),
    path('book/', view=views.book, name='book'),
    path('add_author/', view=views.add_author, name='add_author'),
    path('author/', view=views.author, name='author'),
    path('categories/', view=views.categories, name='categories'),
    # path('my-api/', User.my_api_get_view, name='my-api-get'),  # Route for GET
    # path('my-api/',User.my_api_post_view, name='my-api-post'),  # Route for POST
    # path('my-api/', User.as_view(), name='my-api-get'),  # Route for GET
    # path('my-api/all-users/', User.all_user_data, name='all-users'),  # Route for GET
    # path('my-api/single-users/', User.single_user_data, name='all-users'),  # Route for GET
    
]

# urlpatterns = [
# ]
