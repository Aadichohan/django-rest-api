from rest_framework.serializers import ModelSerializer
from  e_commerce.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'category',
            'desc',
            'published_date',
            'created_at',
        ]
        read_only_fields = ['created_at']