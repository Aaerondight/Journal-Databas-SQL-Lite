import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row #return dictionary like results when using SELECT

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")

def add_entry(content, date):
    with connection:
        connection.execute("INSERT INTO entries VALUES(?, ?);", (content, date))


def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor

# HOW TO MAKE QUERIES DYNAMIC
# GET_USER = "SELECT + FROM users WHERE first_name = ? AND last_name = ?;"
# cursor = connection.execute(GET_USER, (username, password,))

#JOINS
#SELECT * FROM users JOIN orders ON users.userid = orders.orderid
#SELECT users.*, orders.price FROM users JOIN orders ON users.userid = orders.orderid

