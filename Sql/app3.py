import sqlite3
from fpdf import FPDF

con = sqlite3.connect("database.db")
curson = con.cursor()

curson.execute("PRAGMA table_info(ips)")
cols = curson.fetchall()

pdf = FPDF(orientation="P", unit= "pt", format="A4")
pdf.add_page()

for col in cols:
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=100, h=30, txt=col[1], border=1)
    
pdf.output("db.pdf")