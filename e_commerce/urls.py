from django.contrib import admin
from django.urls import path, include
from e_commerce import views
from e_commerce.ModelViews.User import User

urlpatterns = [
    path('', view=views.index, name='index'),
    path('book/', view=views.book, name='book'),
    path('author/', view=views.author, name='author'),
    path('categories/', view=views.categories, name='categories'),
    # path('my-api/', User.my_api_get_view, name='my-api-get'),  # Route for GET
    # path('my-api/',User.my_api_post_view, name='my-api-post'),  # Route for POST
    path('my-api/', User.as_view(), name='my-api-get'),  # Route for GET
    path('my-api/all-users/', User.all_user_data, name='all-users'),  # Route for GET
    path('my-api/single-users/', User.single_user_data, name='all-users'),  # Route for GET
    # path('my-api/all-users/', User.as_view(), name='all-users'),  # Route for GET
    # path('my-api/',User.as_view(), name='my-api-post'),  # Route for POST
]

# urlpatterns = [
# ]
