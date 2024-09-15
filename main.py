from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format='A4')
df = pd.read_csv('topics.csv')

for index, item in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Courier', style='B',size=24)
    pdf.set_text_color(254, 100, 100)
    pdf.cell(w=0, h=12, txt=item['Topic'], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    for i in range(item['Pages'] - 1):
        pdf.add_page()

pdf.output("outout.pdf")