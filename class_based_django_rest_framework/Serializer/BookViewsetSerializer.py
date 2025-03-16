from rest_framework import serializers
from e_commerce.models import Book, Author, Categories
from .AuthorSerializer import AuthorSerializer
from .CategorySerializer import CategorySerializer

class BookViewsetSerializer(serializers.ModelSerializer):
    # ✅ WRITE using IDs
    author_id = serializers.CharField()
    category_id = serializers.CharField()

    # ✅ READ using nested object
    author_data = AuthorSerializer(source='author', read_only=True)
    category_data = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'desc', 'published_date', 'created_at',
            'author_id', 'category_id',  # IDs for writing
            'author_data', 'category_data'  # Nested objects for reading
        ]
        read_only_fields = ['created_at']


# class BookViewsetSerializer(serializers.ModelSerializer):
#     # ✅ WRITE using IDs
#     author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)
#     category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), write_only=True)

#     # ✅ READ using nested object
#     author_data = AuthorSerializer(source='author', read_only=True)
#     category_data = CategorySerializer(source='category', read_only=True)

#     class Meta:
#         model = Book
#         fields = [
#             'id', 'title', 'desc', 'published_date', 'created_at',
#             'author', 'category',  # IDs for writing
#             'author_data', 'category_data'  # Nested objects for reading
#         ]
#         read_only_fields = ['created_at']
