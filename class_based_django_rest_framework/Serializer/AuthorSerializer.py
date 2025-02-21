
from rest_framework.serializers import ModelSerializer
from  e_commerce.models import  Author

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