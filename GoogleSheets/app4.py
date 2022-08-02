import gspread
import re

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")
spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")

cell2  = worksheet1.acell("B2").value 
print(cell2)

cell3 = worksheet1.find('77')
print(cell3.row,cell3.col)
cell11 = worksheet1.findall('88')
print(cell11)

#partial search

regx = re.compile(r'9')
cells = worksheet1.findall(regx)