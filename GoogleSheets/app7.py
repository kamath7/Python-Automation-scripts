import statistics
import gspread

gc = gspread.service_account("iconic-iridium-341007-a5694e7775b8.json")

spreadsheet = gc.open("Nicesheet")

worksheet1 = spreadsheet.worksheet("AwesomeSheet")

exis_col = worksheet1.get_values('B2:B11')
exis_col = [float(i[0]) for i in exis_col]

avg1 = statistics.mean(exis_col)
worksheet1.update('B22',avg1)