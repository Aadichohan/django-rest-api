from rest_framework.serializers import ModelSerializer
from  e_commerce.models import Book, Author, Categories

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'last_name',
            'age',
            'created_at',
        ]
        read_only_fields = ['created_at']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            'id',
            'title',
            'desc',
            'created_at',
        ]
        read_only_fields = ['created_at']


class BookSerializer(ModelSerializer):
    author   = AuthorSerializer()
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'desc',
            'published_date',
            'created_at',
            'author',
            'category',
        ]
        read_only_fields = ['created_at']