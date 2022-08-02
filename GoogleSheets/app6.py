import gspread
import re

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")
spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")

exis_col = worksheet1.get_values('B2:B11')
print(exis_col)
new_col = [[(round(float(i[0]) ** 2))] for i in exis_col]
print(new_col)

worksheet1.update('B2:B11', new_col)