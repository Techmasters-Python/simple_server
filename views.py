import json
import logging

quotes = []


def index(request):
    if request['method'] == "GET":
        return json.dumps(quotes)
    if request['method'] == 'POST':
        parsed = json.loads(request['payload'])
        quotes.append(parsed)
        return request['payload']

    return json.dumps({
        'message': "Not allowed"
    })


def handle_404(path):
    logging.critical(f"Not Found {path}")

    # make the string binary
    return f"<h1>Sorry, can't find {path}!</h1>"
