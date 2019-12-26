import sqlite3,time
database = sqlite3.connect('database.db')
database.row_factory = sqlite3.Row
dbchoose = database.cursor()
oku = dbchoose.execute('Select sec,minu,hour,day,month,year,tl,ml,loc,gmt from numbers')
for dbchoose in oku.fetchall():
    sec =  int(dbchoose['sec'])
    minu =int(dbchoose['minu'])
    hour = int(dbchoose['hour'])
    day =  int(dbchoose['day'])
    month = int(dbchoose['month'])
    year = int(dbchoose['year'])
    tl = int(dbchoose['tl'])
    ml = int(dbchoose['ml'])
    loc = str(dbchoose['loc'])
    gmt = str(dbchoose['gmt'])
database.commit()

fuckyourself = ()
while True:
    if sec <60:
        sec=sec+1
    if sec == 60:
        sec=1
        minu = minu+1
    if ml == 1 and minu ==30 :
        ml =2
        minu = 0
    if ml ==2 and minu == 30:
        hour = hour +1
        ml = 1
        minu = 0
    if 12 == hour and tl ==1:
        hour = 1
        tl = 2
    if 12 == hour and tl ==2:
        tl =1
        hou = 1
        day = day +1
    if month == 1 and day == 32:
        day = 1
        month = month + 1
    if month == 3 and day == 32:
        day = 1
        month = month + 1
    if month == 5 and day == 32:
        day = 1
        month = month + 1
    if month == 7 and day == 32:
        day = 1
        month = month + 1
    if month == 8 and day == 32:
        day = 1
        month = month + 1
    if month == 10 and day == 32:
        day = 1
        month = month + 1
    if month == 12 and day == 32:
        day = 1
        month = month + 1
    if month == 4 and day ==31:
        day = 1

        month = month + 1
    if month == 6 and day ==31:
        day = 1
        month = month + 1
    if month == 9 and day ==31:
        day = 1
        month = month + 1
    if month == 11 and day ==31:
        day = 1
        month = month + 1
    if month == 13:
        month = 1
        year = year + 1
        fuckyourself = year%4   
    if fuckyourself == 0:
        if month == 2 and day == 30:
            day = 1
            month = month + 1
    else:
        if month == 2  and  day ==29:
            day = 1
            month = month + 1
    seci = int(sec)
    database.execute('''Delete  From numbers where ID = ('evet') ''')
    database.execute('''INSERT INTO numbers(sec) VALUES (seci) ''')
    database.commit()
    time.sleep(1)
database.close()
