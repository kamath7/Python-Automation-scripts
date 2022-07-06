import tabula

table = tabula.read_pdf('./ex1.pdf',  pages = 1)

table[0].to_csv("./lalle2.csv",index=None)