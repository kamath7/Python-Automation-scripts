import statistics
import gspread
import time

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")

spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")
worksheet2 = spreadsheet.worksheet("Copy")

while True:
    val1  = worksheet1.acell('B10')
    time.sleep(2)
    val2 = worksheet1.acell('B10')
    if val1 != val2:
        worksheet2.update('A1','Changed')