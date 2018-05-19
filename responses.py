def http_response(body,
                  content_type='text/html'):
    template = f"HTTP/1.1 200 OK\n" \
               f"Content-Type: {content_type}" \
               f"\n\n"
    return template.encode() + body
