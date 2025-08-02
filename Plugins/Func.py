import sqlite3

def connect_to_db():
    conn = sqlite3.connect("umbrella_chk.db")
    return conn
