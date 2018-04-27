import json


class AbstractBackend:
    def list_quotes(self):
        raise NotImplemented

    def add_quote(self, quote):
        raise NotImplemented


class InMemoryBackend(AbstractBackend):
    quotes = []

    def list_quotes(self):
        return self.quotes

    def add_quote(self, quote):
        self.quotes.append(quote)


class FileBackend(AbstractBackend):

    def add_quote(self, quote):
        with open('data.json', 'r') as f:
            content = json.loads(f.read())
            content.append(quote)

        with open('data.json', 'w') as f:
            f.write(json.dumps(content))

    def list_quotes(self):
        with open('data.json', 'r') as f:
            return json.loads(f.read())
