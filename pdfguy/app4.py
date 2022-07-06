from tkinter import PAGES
import tabula 

table = tabula.read_pdf('./weather.pdf',  pages = 1)
print(type(table[0])) #pandas df
table[0].to_csv("lalle.csv",index=None)
