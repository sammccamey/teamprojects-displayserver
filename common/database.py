"""
Uses a database file 'canieatit.db' in the current working directory.
"""

import sqlite3
import sys
import io
import contextlib

DB_PATH = 'wakeupinator.db'
def create_schema(db):
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ConfigItems(
            id integer PRIMARY KEY,
            key TEXT NOT NULL,
            value TEXT)''')
    cur.execute('''CREATE UNIQUE INDEX ConfigItemKeys ON ConfigItems (key);''')
    db.commit()

def initialize():
    db = None
    try:
        db = sqlite3.connect(DB_PATH)

        # First time, we should be making the table.
        create_schema(db)

    except sqlite3.Error as e:
        print('*************\nSQLITE ERROR: {}\n*************'.format(e))

    finally:
        db.commit()

    return db

def connect():
    try:
        return contextlib.closing(sqlite3.connect(DB_PATH))
    except sqlite3.Error as e:
        print('*************\nSQLITE ERROR: {}\n*************'.format(e))
