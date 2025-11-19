from barcode import EAN13 from barcode.writer import ImageWriter from
fpdf import FPDF

— Create Barcode —

code_number = “123456789102” # Must be 12 digits barcode =
EAN13(code_number, writer=ImageWriter()) barcode.save(“my_barcode”)

— Create PDF —

pdf = FPDF() pdf.add_page()

pdf.set_font(“Arial”, size=16) pdf.cell(200, 10, txt=“Maniya Amiri -
Python Project”, ln=True, align=‘C’)

pdf.ln(20) pdf.set_font(“Arial”, size=12) pdf.cell(200, 10,
txt=“Barcode:”, ln=True)

pdf.image(“my_barcode.png”, x=10, y=40, w=100)

pdf.output(“my_project.pdf”)
