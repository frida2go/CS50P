from fpdf import FPDF

class Tshirt(FPDF):
    def __init__(self):
        super().__init__()

    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0,60,"CS50 Shirtificate", align ="C")
        self.ln(20)


def set_name(name):
    cs50pdf = Tshirt()
    cs50pdf.add_page()
    cs50pdf.image("shirtificate.png",x=10,y=60,w=190)
    cs50pdf.set_font("helvetica", size = 25)
    cs50pdf.set_text_color(255, 255, 255)
    cs50pdf.cell(0,213, name, align ="C")
    cs50pdf.output("shirtificate.pdf")




name = input("Name: ")
set_name(f"{name} took CS50")



