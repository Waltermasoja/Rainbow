from django.http import HttpResponseForbidden

ALLOWED_IPS = ['127.0.0.1', '192.168.1.100']  

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/superuser-panel/') and request.META['REMOTE_ADDR'] not in ALLOWED_IPS:
            return HttpResponseForbidden("Access Denied!")
        
        response = self.get_response(request)
        return response
    
class TokenCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/superuser-panel/'):
            # Check if token is stored in the session
            if request.session.get('superuser_token') != "secure-token-12345":
                return HttpResponseForbidden("Access Denied!")
        
        response = self.get_response(request)
        return response
