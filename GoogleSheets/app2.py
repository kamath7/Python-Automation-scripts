import gspread

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")
spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.get_worksheet(0)
data = worksheet1.get_all_records()
print(data)

worksheet2 = spreadsheet.worksheet("AwesomeSheet2")
data1 = worksheet2.get_all_records()
print(data1)