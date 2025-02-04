from django.http import JsonResponse

class Response():
    def __init__(self, data, status=200, error=None, response = {}, headers=None):
        self.data = data
        self.status = status
        self.error = error
        self.response = response
        self.headers = headers

    def to_json(self):
        response_data = {"data": self.data}
        if self.response:
            response_data["response"] = self.response  
        if self.error:
            response_data["error"] = self.error  
        return JsonResponse(response_data, status=self.status, headers=self.headers)