import sqlite3
database= sqlite3.connect("database.db")
database.execute('''INSERT INTO numbers(sec,minu,hour,day,month,year,tl,ml,loc,gmt) VALUES ('40','29','10','21','11','2003','2','2','north','8')''')
database.commit()
database.close()
