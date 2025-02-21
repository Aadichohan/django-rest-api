from rest_framework.serializers import ModelSerializer
from  e_commerce.models import  Categories




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