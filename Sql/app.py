import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

cursor.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cursor.fetchall())