from static import serve_file
from views import index, about_page, handle_404


def route_request(path):
    if path == '/':
        return index()
    if path == '/about':
        return about_page()
    return serve_file(path)
    # return handle_404(path)
