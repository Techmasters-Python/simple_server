def http_response(body):
    template = b"HTTP/1.1 200 OK\n" \
               b"Content-Type: text/html; charset=ISO-8859-1" \
               b"\n\n"
    return template + body
