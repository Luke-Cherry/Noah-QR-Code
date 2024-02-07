import sys
from pyfiglet import Figlet
from fpdf import FPDF
import qrcode
import csv

figlet = Figlet()

def main():
    #Prints initial title
    print(figlet.renderText("Noah QR Code"), end="")
    print("_" * 63)
    print()
    #input("Please enter the name of the csv file: ")
    create_qrcode("480155")

    #Move to read csv file
    links_list = []
    with open("NoahDownload.csv") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            links_list.append(row)
    
    create_pdf()


#Check CSV valid, returns number of rows
def check_csv():
    ...

#Reads CSV file
def read_csv():
    ...

#Passes in link to convert it to a QR code 
def create_qrcode(link):
    img = qrcode.make(f"https://www.noahcompendium.co.uk/?id=-{link}&template=template_printview")
    pdf = FPDF()
    pdf.add_page()
    pdf.image(img.get_image(), x=5, y=5, w=50, h=50)
    str = "Zodon® 25 mg/ml oral solution for cats and dogs"
    str = str.replace("/", "-")
    pdf.output(f"datasheets/{str}.pdf")
    
def create_pdf():
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_margins(5, 15)
    pdf.add_page()
    pdf.set_line_width(0.5)
    pdf.line(x1=105, y1=0, x2=105, y2=297)
    
    for i in range(1,6):
        y = 49.5 * i
        print(y)
        pdf.line(x1=0, y1=y, x2=210, y2=y)
    img = qrcode.make(f"https://www.noahcompendium.co.uk/?id=-480155&template=template_printview")
    pdf.image(img.get_image(), x=5, y=10, w=35, h=35)

    pdf.set_font("Helvetica", size=16, style="B")
    pdf.text(x=8, y=10, text="Scan here for drug datasheet")

    pdf.set_xy(x=40, y=15)
    current_font = 20
    pdf.set_font("Helvetica", size=current_font)
    string = f"Kesium® 40mg/10mg & 50mg/12.5mg chewable tablets for cats & dogs and Kesium® 200mg/50mg, 400mg/100mg & 500mg/125mg chewable tablets for dogs"
    while pdf.get_string_width(string) > 240:
        current_font -= 1
        pdf.set_font("Helvetica", size=current_font)
    pdf.multi_cell(w=60, text=string, align="C", max_line_height=pdf.font_size)

    pdf.set_xy(x=40, y=38)
    current_font = 30
    pdf.set_font("Helvetica", size=current_font)
    while pdf.get_string_width(f"noahcompendium.co.uk/?id=-458494") > 60:
        current_font -= 1
        pdf.set_font("Helvetica", size=current_font)
    pdf.cell(w=60, text="noahcompendium.co.uk/?id=-458494", align="C")

    


    pdf.image(img.get_image(), x=110, y=10, w=35, h=35)

    pdf.set_font("Helvetica", size=16, style="B")
    pdf.text(x=113, y=10, text="Scan here for drug datasheet")

    pdf.set_xy(x=145, y=15)
    current_font = 20
    pdf.set_font("Helvetica", size=current_font)
    string = f"Kesium® 40mg/10mg & 50mg/12.5mg chewable tablets for cats & dogs and Kesium® 200mg/50mg, 400mg/100mg & 500mg/125mg chewable tablets for dogs"
    while pdf.get_string_width(string) > 240:
        current_font -= 1
        pdf.set_font("Helvetica", size=current_font)
    pdf.multi_cell(w=60, text=string, align="C", max_line_height=pdf.font_size)

    pdf.set_xy(x=145, y=38)
    current_font = 30
    pdf.set_font("Helvetica", size=current_font)
    while pdf.get_string_width(f"noahcompendium.co.uk/?id=-458494") > 60:
        current_font -= 1
        pdf.set_font("Helvetica", size=current_font)
    pdf.cell(w=60, text="noahcompendium.co.uk/?id=-458494", align="C")


    pdf.output("test.pdf")
    

if __name__ == "__main__":
    main()