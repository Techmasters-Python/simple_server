import logging
import os
import subprocess

CONTENT_FOLDER = os.path.join(os.getcwd(), 'htdocs')


def detect_mime_type(path):
    path = os.path.join(CONTENT_FOLDER, path[1:])
    output = subprocess.check_output(
        ['file','--mime-type', path])
    output = output.decode().strip().split(': ')
    return output[1]


def serve_file(path):
    logging.critical(f"File requested {path}")

    absolute_path = os.path.join(CONTENT_FOLDER, path[1:])

    if not os.path.exists(absolute_path):
        return f"Couldn't find {path}".encode()

    with open(absolute_path, 'rb') as requested_file:
        return requested_file.read()
