from static import detect_mime_type


def test_detect_mime_type():
    test_value = '/hello.txt'
    assert detect_mime_type(test_value) == 'text/plain'
