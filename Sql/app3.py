import sqlite3
from fpdf import FPDF

con = sqlite3.connect("database.db")
curson = con.cursor()

curson.execute("PRAGMA table_info(ips)")
cols = curson.fetchall()

for col in cols:
    print(col[1])