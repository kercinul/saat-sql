import sqlite3
database= sqlite3.connect("database.db")
database.cursor()
database.execute('''CREATE TABLE numbers (
    sec   INTEGER,
    minu  INTEGER,
    hour  INTEGER,
    day   INTEGER,
    month INTEGER,
    year  INTEGER,
    tl    INTEGER,
    ml    INTEGER,
    loc   TEXT,
    gmt   TEXT,
    ID    TEXT     PRIMARY KEY   
);''')
database.commit()
database.close()
