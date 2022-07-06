from fpdf import FPDF

pdf = FPDF(orientation='portrait', unit='pt', format='A4')

pdf.add_page()
pdf.image('tiger.jpeg', w=80, h=50)
pdf.set_font(family="Times", style="B",size=27)
pdf.cell(w=0, h=50, txt="Awesome Tiger",align="C")
pdf.output('output1.pdf')