from static import serve_file
from views import index, handle_404, create


def render_view(func, request):
    return func(request).encode()


def route_request(request):
    if request['path'] == '/':
        return render_view(index, request)
    if request['path'] == '/create':
        return render_view(create, request)
    # return serve_file(request['path'])
    return handle_404(request['path'])
