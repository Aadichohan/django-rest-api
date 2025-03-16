
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from e_commerce.models import Book
from ...Serializer.BookViewsetSerializer import BookViewsetSerializer
from class_based_django_rest_framework.drf_response.drf_response import DRFResponse


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookViewsetSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        books = Book.objects.all()
        book_serializer = BookViewsetSerializer(books, many=True)
        return DRFResponse(
            data    = book_serializer.data, 
            status  = status.HTTP_200_OK, 
            error   = {}, 
            headers = {}
        ).to_json()

    def create(self, request):
        book_serializer = self.get_serializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return DRFResponse( 
                data    = [book_serializer.data], 
                status  = status.HTTP_201_CREATED, 
                error   = {}, 
                response = {'response': 'Book created successfully'},
                headers = {}
            ).to_json()
        # print(book_serializer.errors)
        return DRFResponse( 
            data    = [book_serializer.data], 
            status  = status.HTTP_400_BAD_REQUEST, 
            error   = [book_serializer.errors], 
            response = {'response': 'Something went wrong'},
            headers = {}
        ).to_json()
        

    def retrieve(self, request, pk=None):
        book = self.get_object()
        book_serializer = self.get_serializer(book)
        return DRFResponse(
            data    = [book_serializer.data], 
            status  = status.HTTP_200_OK, 
            error   = {}, 
            headers = {}
        ).to_json()

    def update(self, request, pk=None):
        book = self.get_object()
        book_serializer = self.get_serializer(book, data= request.data)
        if book_serializer.is_valid():
            book_serializer.save()

            return DRFResponse( 
                data    = [book_serializer.data], 
                status  = status.HTTP_200_OK, 
                error   = {}, 
                response = {'response': 'Book updated successfully'},
                headers = {}
            ).to_json()
        
        return DRFResponse( 
            data    = [book_serializer.data], 
            status  = status.HTTP_400_BAD_REQUEST, 
            error   = [book_serializer.errors], 
            response = {'response': 'Something went wrong'},
            headers = {}
        ).to_json()

    def partial_update(self, request, pk=None):
        book = self.get_object()
        book_serializer = self.get_serializer(book, data= request.data, partial=True)
        if book_serializer.is_valid():
            book_serializer.save()

            return DRFResponse( 
                data    = [book_serializer.data], 
                status  = status.HTTP_200_OK, 
                error   = {}, 
                response = {'response': 'Book updated successfully'},
                headers = {}
            ).to_json()
        
        return DRFResponse( 
            data    = [book_serializer.data], 
            status  = status.HTTP_400_BAD_REQUEST, 
            error   = [book_serializer.errors], 
            response = {'response': 'Something went wrong'},
            headers = {}
        ).to_json()

    def destroy(self, request, pk=None):
        book = self.get_object()
        book.delete()
        return DRFResponse( 
         
            status  = status.HTTP_204_NO_CONTENT, 
            error   = {}, 
            response = {'response': 'Book deleted successfully'},
            headers = {}
        ).to_json()
    
    # Custom action for marking a book as favorite (example)
    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        book = self.get_object()
        book.desc = 'favorite'
        book.save()
        return Response({'status': 'book marked as favorite'})