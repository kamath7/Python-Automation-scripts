import pandas as pd
from fpdf import FPDF

df = pd.read_excel("./data.xlsx")
print(df)

for index, row in df.iterrows():
    pdf = FPDF(orientation="P", unit = "pt", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B",size=27)
    pdf.cell(w=0, h=50, txt=row["name"],align="C", border=1,ln=1)
    pdf.output(f"{row['name']}.pdf")
