import sqlite3

con = sqlite3.connect("database.db")
curson = con.cursor()

new_row = [('1.1.1.1','a.b.c',100),('2.2.2.2','d.e.f',300)]
curson.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_row)
con.commit()

curson.execute("SELECT * FROM 'ips'")
print(curson.fetchall())