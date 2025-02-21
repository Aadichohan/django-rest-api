
from rest_framework.views import APIView
from rest_framework import status

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from e_commerce.response import Response as EcommerceResponse
# from class_based_django_rest_framework.drf_response.drf_response import DRFResponse
# from rest_framework.response import Response as DRFResponse
from e_commerce.models import Book
from ...Serializer.BookSerializer import BookSerializer
import json
from django.shortcuts import render, get_object_or_404


class BookView(View):

    def get(self, request, book_id=None):
        try:
            if book_id:
                # book = Book.objects.get(id=book_id)
                book = get_object_or_404(Book, pk=book_id)
                book_serializer = BookSerializer(book)
                # return DRFResponse(book_serializer.data)
                return EcommerceResponse(
                    data    = [book_serializer.data], 
                    status  = status.HTTP_200_OK, 
                    error   = {}, 
                    headers = {}
                ).to_json()
            
            books = Book.objects.all()
            book_serializer = BookSerializer(books, many=True)
            return EcommerceResponse( 
                data    = book_serializer.data, 
                status  = status.HTTP_200_OK, 
                error   = {}, 
                headers = {}
            ).to_json()
        
        except json.JSONDecodeError as e:
            return EcommerceResponse(
                data    = {}, 
                status  = status.HTTP_400_BAD_REQUEST, 
                error   = {'error': str(e)}, 
                headers = {}
            ).to_json()
