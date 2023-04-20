

class PathUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        response.context_data["path_url"] = request.path[4:]
        response.context_data["site_url"] = request.get_host()
        return response

        
       