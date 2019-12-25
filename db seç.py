import sqlite3
baglanti = sqlite3.connect('database.db')
baglanti.row_factory = sqlite3.Row
veritabani_sec = baglanti.cursor()
oku = veritabani_sec.execute('Select sec,minu,hour,day,month,year,tl,ml,loc,gmt from numbers')
for verileri_cek in oku.fetchall():
    print(verileri_cek['sec'],verileri_cek['minu'],verileri_cek['hour'],verileri_cek['day'],verileri_cek['month'],verileri_cek['year'],verileri_cek['tl'],verileri_cek['ml'],verileri_cek['loc'],verileri_cek['gmt'])
#baglanti kapatma ve kaydetme.
baglanti.commit()
baglanti.close()
