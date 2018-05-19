import json
import logging
from urllib.parse import parse_qsl

import atexit

from storages import DatabaseBackend

backend = DatabaseBackend()
backend.on_start()
atexit.register(backend.on_exit)


def format_entry(data):
    return "<h1>{quote}</h1><h4>-{author}</h4>".format(**data)


def index(request):
    if request['method'] == "GET":
        quotes = backend.list_quotes()
        return "\n\n".join(map(format_entry, quotes))
    return 'Unknown Action'


def create_get(request):
    return """
        <form action="/create" method="post">
        <textarea rows="10" cols="40" name="quote"></textarea>
        <br>
        <input type="text" name="author"></textarea>
        <br>
        <input type="submit">
        </form>
        """


def create_post(request):
    data = dict(parse_qsl(request['payload']))
    backend.add_quote(data)
    return format_entry(data)


def create(request):
    if request['method'] == "GET":
        return create_get(request)
    if request['method'] == "POST":
        return create_post(request)
    return 'Unknown Action'


def handle_404(path):
    logging.critical(f"Not Found {path}")

    # make the string binary
    return f"<h1>Sorry, can't find {path}!</h1>".encode()
