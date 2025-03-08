from rest_framework.serializers import ModelSerializer
from  e_commerce.models import Book
from .AuthorSerializer import AuthorSerializer
from .CategorySerializer import CategorySerializer






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