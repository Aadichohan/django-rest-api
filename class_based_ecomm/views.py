import json
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from e_commerce.response import Response
# from class_based_ecomm.models import Book, Author, Categories
from e_commerce.models import Book, Author, Categories
# Create your views here.

class BookView(View):
    # template_name = "books/book_list.html"
    # def get(self, request):
    #     print('stop')
    #     books = Book.objects.all()
    #     return render(request, self.template_name, {'books': books})

    def get(self, request):
        books = Book.objects.all()
        books_data = [{"id":book.id, "title": book.title, "author": book.author_id, "category": book.category_id, "desc": book.desc, "published_date":book.published_date} for book in books]
        # return JsonResponse(books_data, safe=False)
        return Response( 
            data    = [], 
            status  = 200, 
            error   = {}, 
            headers = {}
        ).to_json()

    
    @csrf_exempt  # This is required for the POST method in Postman or other clients for testing purposes
    def post(self, request):
        # Handle deletion first if "delete" is in request
        if "delete" in request.POST:
            book_id = request.POST.get("delete")
            book = get_object_or_404(Book, id=book_id)
            book.delete()
            return Response( 
                data    = [], 
                status  = 200, 
                error   = {}, 
                response = {'response': 'Book Deleted'},
                headers = {}
             ).to_json()
            # return JsonResponse({'message': 'Book deleted successfully'})

        # If not a delete, create a new book
        try:
            data           = json.loads(request.body)  # Read JSON data from the request
            title          = data.get('title')
            author         = data.get('author_id')
            category       = data.get('category_id')
            desc           =  data.get('desc')
            published_date = data.get('published_date')

            # Validate required fields
            if not title or not author or not category:
                return Response( 
                    data    = [], 
                    status  = 400, 
                    error   = {'message': 'All fields are required'}, 
                    response = {'response': 'All fields are required'},
                    headers = {}
                ).to_json()
                # return JsonResponse({'error': 'All fields are required'}, status=400)

            # Save the new book
            book = Book.objects.create(
                title = title,
                author_id = author,
                category_id = category,
                desc = desc,
                published_date= published_date
            )
            return Response( 
                    data    = [{'id': book.id, 'title': book.title}], 
                    status  = 201, 
                    error   = {}, 
                    response = {'response': 'Book created successfully'},
                    headers = {}
                ).to_json()
            # return JsonResponse({'message': 'Book created successfully', 'book': {'id': book.id, 'title': book.title}}, status=201)
        except json.JSONDecodeError:
             return Response( 
                    data    = [], 
                    status  = 400, 
                    error   = {'message': 'Invalid JSON format'}, 
                    response = {'response': 'Invalid JSON format'},
                    headers = {}
                ).to_json()
            # return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    # def list_books(self, request):
    #     books = Book.objects.all()
    #     response = []
    #     for book in books:
    #         response.append(
    #             {
    #                 "id": book.id,
    #                 "title": book.title,
    #                 "author_id": book.author_id,
    #                 "category_id": book.category_id,
    #                 "description": book.desc,
    #                 "published_date": book.published_date,
    #             }
    #         )
    #     return Response( 
    #         data    = response, 
    #         status  = 200, 
    #         error   = {}, 
    #         headers = {}
    #     ).to_json()
    
    def put(self, request):
        # print('post ',request.POST)
        try:
            data    = json.loads(request.body)
            book_id = data.get("id")
            book    = get_object_or_404(Book, id=book_id)
            # Get the related author and category using the ids
            author_id = data.get("author_id")
            category_id = data.get("category_id")

                # Fetch the related Author and Category instances
            author   = get_object_or_404(Author, id=author_id)
            category = get_object_or_404(Categories, id=category_id)

                # Now prepare the data for the form, including the related Author and Category
            form_data = {
                "title": data.get("title"),
                "desc": data.get("desc"),
                "published_date": data.get("published_date"),
                "author": author,  # Pass the actual Author instance
                "category": category  # Pass the actual Category instance
            }
            # print(form_data)
            form = self.get_form(form_data, instance=book)
            # print( form)
            if form.is_valid():
                form.save()
                # Return a JSON response confirming the update
                return Response( 
                    data    = [], 
                    status  = 204, 
                    error   = {}, 
                    response = {"success": True, 'response': 'Book updated successfully'},
                    headers = {}
                ).to_json()
                # return JsonResponse({"success": True, "message": "Book updated successfully"})
        
            # Return errors as JSON if form is invalid
            # return JsonResponse({"success": False, "errors": form.errors}, status=400)
            return Response( 
                    data    = [], 
                    status  = 204, 
                    error   = {'message': form.errors}, 
                    response = {"success": False, 'response': 'form.errors'},
                    headers = {}
                ).to_json()

        except json.JSONDecodeError:
             return Response( 
                    data    = [], 
                    status  = 400, 
                    error   = {'message': 'Invalid JSON format'}, 
                    response = {'response': 'Invalid JSON format'},
                    headers = {}
                ).to_json()

    def delete(self, request):
        try:
            data    = json.loads(request.body)
            book_id = data.get("id")
            book = get_object_or_404(Book, id=book_id)
            book.delete()
            # Return a JSON response confirming the deletion
            return Response( 
                    data    = [], 
                    status  = 204, 
                    error   = {}, 
                    response = {"success": True, 'response': 'Book deleted successfully'},
                    headers = {}
                ).to_json()
        
        except json.JSONDecodeError:
             return Response( 
                    data    = [], 
                    status  = 400, 
                    error   = {'message': 'Invalid JSON format'}, 
                    response = {'response': 'Invalid JSON format'},
                    headers = {}
                ).to_json()

    def patch(self, request):
        try:
            data    = json.loads(request.body)
                       # Get the book ID from the JSON data
            book_id        = data.get("id")
            title          = data.get("title")
            desc           = data.get("desc")
            published_date = data.get("published_date")
            if not book_id:
                return Response( 
                    data    = [], 
                    status  = 204, 
                    error   = {"message": "Book ID is required"}, 
                    response = {"success": False, 'response': 'Book ID is required'},
                    headers = {}
                ).to_json()
                # return JsonResponse({"error": "Book ID is required"}, status=400)

            # Fetch the Book instance from the database using the provided ID
            book = get_object_or_404(Book, id=book_id)

            # Get related author and category using their ids, if provided
            author_id = data.get("author_id")
            category_id = data.get("category_id")

            # Update the author if an author_id is provided
            if author_id:
                author = get_object_or_404(Author, id=author_id)
                book.author = author

            # Update the category if a category_id is provided
            if category_id:
                category = get_object_or_404(Categories, id=category_id)
                book.category = category

            # Only update fields that are provided in the request
            if title:
                book.title = title
            if desc:
                book.desc = desc
            if published_date:
                book.published_date =  data.get("published_date", book.published_date)

            # Save the partially updated Book instance
            book.save()
            # Return a JSON response confirming the partial update
            return Response( 
                    data    = [], 
                    status  = 204, 
                    error   = {}, 
                    response = {"success": True, 'response': 'Book patched successfully'},
                    headers = {}
                ).to_json()
            
            # Return errors as JSON if form is invalid
            # return JsonResponse({"success": False, "errors": form.errors}, status=400)

        except json.JSONDecodeError:
             return Response( 
                    data    = [], 
                    status  = 400, 
                    error   = {'message': 'Invalid JSON format'}, 
                    response = {'response': 'Invalid JSON format'},
                    headers = {}
                ).to_json()
    
    def get_form(self, data=None, instance=None):
        # Define the form inside the view to handle dynamic instance passing
        class BookForm(ModelForm):
            class Meta:
                model = Book
                fields = ["title", "category", "author", "desc", "published_date"]

        # Return the form with data and instance if provided
        return BookForm(data, instance=instance)
    
    # def get_form(self, data=None):
    #     from django.forms import ModelForm

    #     class BookForm(ModelForm):
    #         class Meta:
    #             model = Book
    #             fields = ["title", "category", "author", "desc", "published_date"]

    #     return BookForm(data)
