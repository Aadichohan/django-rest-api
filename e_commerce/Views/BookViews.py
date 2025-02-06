import json
from django.shortcuts import render, get_object_or_404

from ..models import Book
from ..response import Response

def getBooks(request):
    if request.method == 'GET':
        book_list = Book.objects.values()
        # print(book_list)
        return Response( 
        data    = list(book_list), 
        status  = 200, 
        error   = {}, 
        headers = {}
    ).to_json()
        # return JsonResponse( list(book_list), safe=False)
    
    return Response( 
        data    = [], 
        status  = 404, 
        error   = {}, 
        headers = {}
    ).to_json()

def getBook(request, id):
    if request.method == 'GET':
        # book_list = Book.objects.values()
        try:
            book_detail = get_object_or_404(Book, pk=id)
            # print(dict(book_detail))
            return Response( 
            data    = [{"id": book_detail.id, "title": book_detail.title}], 
            status  = 200, 
            error   = {}, 
            headers = {}
            ).to_json()
            # return JsonResponse( list(book_list), safe=False)

        except:
            return Response( 
                data    = [], 
                status  = 404, 
                error   = {}, 
                headers = {}
            ).to_json()
        

def addBook(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        title = data.get('title')
        author = data.get('author_id')
        category = data.get('category_id')
        desc = data.get('desc')
        published_date = data.get('published_date')
        # author_instance = Author.objects.get(author=1) 

        book = Book.objects.create(
            title = title,
            author_id = author,
            category_id = category,
            desc = desc,
            published_date= published_date
            )
        return Response( 
            data    = [{'id':book.id, 'title':book.title, "author_id": book.author_id, "category_id": book.category_id, "desc": book.desc, "published_date": book.published_date}], 
            status  = 201, 
            error   = {}, 
            response = {'response': 'Book Created'},
            headers = {}
        ).to_json()
    return Response( 
        data    = [], 
        status  = 404, 
        error   = {'message': 'Method Not Allowed'}, 
        headers = {}
    ).to_json()