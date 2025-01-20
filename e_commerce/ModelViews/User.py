# my_api_views.py
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class User(View):
    def get(self, request):
        print('method: ',request)
        data = {"message": "This is a GET request."}
        return JsonResponse(data)
    
    # @csrf_exempt
    def post(self, request):
        # return User.my_api_post_view(request)  # Handle POST request
        print('method: ',request)
        data = {"message": "This is a POST request.", "received_data": request.POST}
        return JsonResponse(data)
    
    def put(self, request):
        data = {"message": "This is a PUT request."}
        return JsonResponse(data)
    

    def all_user_data(request):
        return JsonResponse({"users": 'all users'})


    def single_user_data(request):
        return JsonResponse({"users": 'Single users'})
