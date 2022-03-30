from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# Add a title
pdf.set_font(family='Arial', size=24, style='B')
pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

# Add Period label and its value
pdf.cell(w=150, h=40, txt='Period', border=1, align='C')
pdf.cell(w=0, h=40, txt='March 2022', border=1, align='C', ln=1)

# Add flatmates' names and how much they need to pay
pdf.cell(w=150, h=40, txt='John', border=1, align='C')
pdf.cell(w=0, h=40, txt='66.6', border=1, align='C', ln=1)
pdf.cell(w=150, h=40, txt='Marry', border=1, align='C')
pdf.cell(w=0, h=40, txt='53.4', border=1, align='C', ln=1)

pdf.output('bill.pdf')
