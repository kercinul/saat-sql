import sqlite3
database= sqlite3.connect("database.db")
database.cursor()
database.execute('''CREATE TABLE IF NOT EXISTS numbers(sec,minu,hour,day,month,year,tl,ml,loc,gmt,ID)''')
database.commit()
database.close()
