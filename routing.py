from static import serve_file
from views import index, handle_404


def render_view(func, request):
    return func(request).encode()


def route_request(request):
    if request['path'] == '/':
        return render_view(index, request)
    return serve_file(request['path'])
    # return handle_404(path)
