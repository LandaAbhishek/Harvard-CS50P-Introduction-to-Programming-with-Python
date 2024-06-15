# importing libraries
from fpdf import FPDF

# create shirtificate header and assigning shirtificate.png image
class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("Times", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

# function to input name
def main():
    name = input("Name: ").title().strip()
    shirt(name)

# function to generate and save certificate
def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("Times", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")

# calling main function
if __name__ == "__main__":
    main()
