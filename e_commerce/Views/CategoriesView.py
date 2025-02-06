import json
from django.shortcuts import render, get_object_or_404

from ..models import Categories
from ..response import Response

def getCategories(request):
    if request.method == 'GET':
        category_list = Categories.objects.values()
        # print(book_list)
        return Response( 
        data    = list(category_list), 
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

def getCategory(request, id):
    if request.method == 'GET':
        # book_list = Book.objects.values()
        try:
            category_detail = get_object_or_404(Categories, pk=id)
            print(category_detail.id)
            return Response( 
            data    = [{"id": category_detail.id, "name": category_detail.title, "created_date": category_detail.created_at}], 
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
        
def addCategory(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        title = data.get('title')
        desc = data.get('desc')
        # author_instance = Author.objects.get(author=1) 

        category = Categories.objects.create(
            title = title,
            desc = desc
        )
        return Response( 
            data    = [{"category_id": category.id, "title": category.title, "created_date": category.created_at}], 
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