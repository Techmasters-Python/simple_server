import json
import logging

from storages import FileBackend

backend = FileBackend()


def index(request):
    if request['method'] == "GET":
        quotes = backend.list_quotes()
        return json.dumps(quotes)
    if request['method'] == 'POST':
        parsed = json.loads(request['payload'])
        backend.add_quote(parsed)
        return request['payload']

    return json.dumps({
        'message': "Not allowed"
    })


def handle_404(path):
    logging.critical(f"Not Found {path}")

    # make the string binary
    return f"<h1>Sorry, can't find {path}!</h1>"
