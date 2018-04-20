import logging


def index():
    return b"<h1>Hello to my Home Page</h1>"


def about_page():
    return b"<h1>About Me</h1>"


def handle_404(path):
    logging.critical(f"Not Found {path}")

    # make the string binary
    return f"<h1>Sorry, can't find {path}!</h1>".encode('utf-8')
