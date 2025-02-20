import json
from django.shortcuts import render, get_object_or_404
from ..models import  Author
from ..response import Response

def getAuthors(request):
    if request.method == 'GET':
        author_list = Author.objects.values()
        # print(book_list)
        return Response( 
        data    = list(author_list), 
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


def getAuthor(request, id):
    if request.method == 'GET':
        # book_list = Book.objects.values()
        try:
            author_detail = Author.objects.get(pk=id)
            # print(dict(book_detail))
            return Response( 
            data    = [{"id": author_detail.id, "name": author_detail.name, "last_name": author_detail.last_name, "age": author_detail.age, "created_date": author_detail.created_at}], 
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

def addAuthor(request):
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
        # print(author.id)
        return Response( 
            # data    = list({"author_id": author.id, "name": author.name, "last_name": author.last_name, "age": author.age, "created_date": author.created_at}), 
            data    = [{"author_id": author.id, "name": author.name, "last_name": author.last_name, "age": author.age, "created_date": author.created_at}], 
            status  = 200, 
            error   = {}, 
            headers = {}
        ).to_json()

    return Response( 
        data    = [], 
        status  = 404, 
        error   = {'message': 'Method Not Allowed'}, 
        headers = {}
    ).to_json()

def updateAuthor(request, id):
    if request.method == 'PUT':

        data           = json.loads(request.body)
        author         = get_object_or_404(Author, pk=id)
        name           = data.get('name')
        last_name      = data.get('last_name')
        age            = data.get('age')
        if name:
            author.name = name
        if last_name:
            author.last_name = last_name
        if age:
            author.age = age

        author.save()
        return Response( 
            data    = [{'id':author.id, 'name':author.name, "last_name": author.last_name, "age": author.age}], 
            status  = 201, 
            error   = {}, 
            response = {'response': 'Author Updated'},
            headers = {}
        ).to_json()

    return Response( 
        data    = [], 
        status  = 404, 
        error   = {'message': 'Method Not Allowed'}, 
        headers = {}
    ).to_json()
        
