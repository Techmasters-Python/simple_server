import json
import sqlite3


class AbstractBackend:
    def list_quotes(self):
        raise NotImplemented

    def add_quote(self, quote):
        raise NotImplemented

    def on_start(self):
        pass

    def on_exit(self):
        pass


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


class DatabaseBackend(AbstractBackend):
    conn = None
    cursor = None

    def on_start(self):
        self.conn = sqlite3.connect('quotes.db')
        self.cursor = self.conn.cursor()

    def on_exit(self):
        self.conn.close()

    def list_quotes(self):
        self.cursor.execute("SELECT * FROM quotes")
        result = self.cursor.fetchall()
        return [{'author': x[0], 'quote': x[1]}
                for x in result]

    def add_quote(self, quote):
        self.cursor.execute(
            f"INSERT INTO quotes VALUES ('{quote['author']}', '{quote['quote']}')")
        self.conn.commit()
