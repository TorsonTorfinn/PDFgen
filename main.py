from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, item in df.iterrows():
    # Setting the Header
    pdf.add_page()
    pdf.set_font(family='Courier', style='B',size=24)
    pdf.set_text_color(254, 100, 100)
    pdf.cell(w=0, h=12, txt=item['Topic'], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    # Setting the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style='I', size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=10, txt=item['Topic'], align='R', ln=1)

    for i in range(item['Pages'] - 1):
        pdf.add_page()

            # Setting the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style='I', size=10)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=10, txt=item['Topic'], align='R', ln=1)
pdf.output("outout.pdf")