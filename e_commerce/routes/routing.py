# from django.urls import path
# from django.http import JsonResponse

# def method_route(http_method, view):
#     def wrapper(request, *args, **kwargs):
#         if request.method == http_method:
#             return view(request, *args, **kwargs)
#         else:
#             return JsonResponse({"error": "Method Not Allowed"}, status=405)
#     return wrapper


from django.http import JsonResponse
from django.views import View

# Custom decorator to define methods for an endpoint
def method_route(http_method):
    print('http_method: ',http_method)
    """
    A decorator to route a view to a specific HTTP method like GET, POST, etc.
    """
    def decorator(view):
        print('view: ',view)
        def wrapper(request, *args, **kwargs):
            
            if request.method == http_method:
                return view(request, *args, **kwargs)
            else:
                return JsonResponse({"error": "Method Not Allowed"}, status=405)
        return wrapper
    return decorator
