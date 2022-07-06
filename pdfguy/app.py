from fpdf import FPDF

pdf = FPDF(orientation='portrait', unit='pt', format='A4')

pdf.add_page()
pdf.image('tiger.jpeg', w=80, h=50)
pdf.output('output1.pdf')