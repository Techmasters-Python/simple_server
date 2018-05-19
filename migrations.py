import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE quotes(author TEXT, quote TEXT)")
    conn.commit()
    conn.close()
