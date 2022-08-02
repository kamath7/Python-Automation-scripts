import gspread

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")
spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")

data = worksheet1.get_values("A2:B2")
print(data)


