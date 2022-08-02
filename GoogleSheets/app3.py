import gspread

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")
spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")

data = worksheet1.get_values("A2:B2")
print(data)

col = worksheet1.get_values("B1:B11")
print(col)

#alternate to col values
col1 = worksheet1.col_values(2)
print(col1)

rows = worksheet1.row_values(3)