from django.shortcuts import redirect


class AuthAndRegMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and (request.path == '/login' or request.path == '/registration'):
            return redirect('main_page')
        response = self._get_response(request)
        return response
