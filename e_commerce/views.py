from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .Response import Response

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
    # return Response( 
    #     data = {'id': 1, 'name': 'item.name', 'description': 'item.description', 'price': 200}, 
    #     status = 200, 
    #     error = {'code': 300, 'message': 'Item Created Successfully'}, 
    #     headers = {'X-Custom-Header': 'Item Created Successfully'}
    # ).to_json()
    # return HttpResponse( "e_commerce/index.html")


def book(request):
    return JsonResponse( {"data":"e_commerce/book.html"})

def author(request):
    return JsonResponse( {"data":"e_commerce/author.html"})

def categories(request):
    return JsonResponse( {"data":"e_commerce/author.html"})