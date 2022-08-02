import gspread
import re

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")
spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")

worksheet1.update('B2',299)

worksheet1.update_cell(5,5,99)