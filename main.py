from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv('topics.csv')

for index, row in topics.iterrows():
    pdf.add_page()

    #header
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1)

    #line across page separating header from body and
    # then evenly space lines for writing like a notebook
    # alternative would be to set range(20, 290, 10) then replace 20+10*i with just i
    for i in range (27):
        pdf.line(10,20+(10*i),200,20+(10*i))

    pdf.ln(266)

    # footer
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f'{row['Topic']} page 1 of {row['Pages']}', align='R')

    #loop through and create the number of pages based on the csv.
    # Since we already created the first page outside the loop
    # that's why it's row['Pages']-1
    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # evenly space lines across page for writing like a notebook
        # alternative would be to set range(10, 290, 10) then replace 10*j with just j
        for j in range(29):
            pdf.line(10, 10*j,200, 10*j)

        pdf.ln(278)

        #footer
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        #i starts at 0 and we already created page 1.
        # This is why page count has +2
        pdf.cell(w=0, h=10, txt=f'{row['Topic']} page {i+2} of {row['Pages']}', align='R')

pdf.output("output.pdf")