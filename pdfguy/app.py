from fpdf import FPDF
from numpy import unicode_

pdf = FPDF(orientation='portrait', unit='pt', format='A4')

pdf.add_page()
pdf.image('tiger.jpeg', w=80, h=50)
pdf.set_font(family="Times", style="B",size=27)
pdf.cell(w=0, h=50, txt="Awesome Tiger",align="C", border=1,ln=1)
pdf.set_font(family="Times",size=23, style="B")
pdf.cell(w=0, h=20, txt="Description", ln=1)

pdf.set_font(family="Times", size=20)
txt4 = """
The Bengal tiger is a population of the Panthera tigris tigris subspecies It ranks among the biggest wild cats alive today. It is considered to belong to the world's charismatic megafauna
The tiger is estimated to have been present in the Indian subcontinent since the Late Pleistocene, for about 12,000 to 16,500 years.Today, it is threatened by poaching, loss and fragmentation of habitat, and was estimated at comprising fewer than 2,500 wild individuals by 2011. None of the Tiger Conservation Landscapes within its range is considered large enough to support an effective population of more than 250 adult individuals.
"""
pdf.multi_cell(w=0, h=15, txt=txt4)
pdf.output('output1.pdf')