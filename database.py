import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries(content TEXT, date TEXT)")

def add_entry(content, date):
    entries.append({"content": content, "date": date})

def get_entries():
        return entries

