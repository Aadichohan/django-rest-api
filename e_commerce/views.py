from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .response import Response
from .models import Book, Author, Categories
import json

# Create your views here.

def index(request):
    # print('req ', request)
    data = {
            'id': 1, 
            'namess': 
            'item.name', 
            'description': 'item.description', 
            'price': 200
        }
    datas = [data, data]
    # print("{")
    # for key in data.keys():
    #     print(f"'{key}' : '{data[key]}'")
    # print("}")

    for item in datas:
        print(item)
   
    # return render(request, "e_commerce/index.html")
    return Response( 
        data    = datas, 
        status  = 200, 
        error   = {'code': 300, 'message': 'Item Created Successfully'}, 
        headers = {'X-Custom-Header': 'Item Created Successfully'}
    ).to_json()
    # return Respon]se( 
    #     data = {'id': 1, 'name': 'item.name', 'description': 'item.description', 'price': 200}, 
    #     status = 200, 
    #     error = {'code': 300, 'message': 'Item Created Successfully'}, 
    #     headers = {'X-Custom-Header': 'Item Created Successfully'}
    # ).to_json()
    # return HttpResponse( "e_commerce/index.html")


def add_author(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        last_name = data.get('last_name')
        age = data.get('age')

        author = Author.objects.create(
            name = name,
            last_name = last_name,
            age = age
        )
        print(author)
        return Response( 
            data    = list({"author_id": author.id, "name": author.name, "last_name": author.last_name, "age": author.age, "created_date": author.created_at}), 
            status  = 200, 
            error   = {}, 
            headers = {}
        ).to_json()

def get_book_list(request):
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

def get_book(request, id):
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

def add_book(request):
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
            data    = {'id':book.id, 'title':book.title}, 
            status  = 201, 
            error   = {}, 
            response = {'response': 'Book Created'},
            headers = {}
        ).to_json()

def book(request):
    return JsonResponse( {"data":"e_commerce/book.html"})

def author(request):
    return JsonResponse( {"data":"e_commerce/author.html"})

def categories(request):
    return JsonResponse( {"data":"e_commerce/author.html"})