import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

cursor.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cursor.fetchall())

cursor.execute("SELECT address,asn FROM 'ips' ORDER BY asn")
print(cursor.fetchall())

cursor.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cursor.fetchall())

cursor.execute("SELECT * FROM 'ips' WHERE asn = 144")
print(cursor.fetchall())

cursor.execute("SELECT * FROM 'ips' WHERE asn = 144 AND domain LIKE '%sa'")
print(cursor.fetchall())

results = cursor.fetchall()
for row in results:
    print(row)
# cursor.fetchall() -> must be executed only once
