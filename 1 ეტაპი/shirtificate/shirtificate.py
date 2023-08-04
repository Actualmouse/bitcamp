from fpdf import FPDF

userName = input("Name: ")
value = f'{userName} took CS50'


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 40)
pdf.cell(0, 55, 'CS50 Shirtificate', align="C")
pdf.image('shirtificate.png', x = 0, y = 70, w = 0, h = 0, type = '', link = '')
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
txtwidth = pdf.get_string_width(value)
width = pdf.w
x = (width - txtwidth) / 2
pdf.set_x(x)
pdf.cell(txtwidth, 255, value, 0, 0, align='C')




pdf.output("shirtificate.pdf")