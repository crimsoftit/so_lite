import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute("INSERT INTO posts VALUES('manu', 'ni yule mguyz')")
    c.execute("INSERT INTO posts VALUES('bil', 'pia ni yule mguyz')")
