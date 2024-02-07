import sys
from pyfiglet import Figlet
from fpdf import FPDF
import qrcode
import csv
import re

figlet = Figlet()

def main():
    #Prints initial title
    print(figlet.renderText("Noah QR Code"), end="")
    print("_" * 63)
    print()
    #input("Please enter the name of the csv file: ")
    

    #Move to read csv file
    links_list = []
    with open("NoahDownload1.csv", encoding="UTF-8-sig") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            links_list.append(row)

    for row in links_list:
        print(row)
        create_pdf(row[1], row[0] , create_qrcode(row[1]))


#Check CSV valid, returns number of rows
def check_csv():
    ...

#Reads CSV file
def read_csv():
    ...

#Passes in link to convert it to a QR code 
def create_qrcode(link):
    return qrcode.make(f"https://www.noahcompendium.co.uk/?id=-{link}&template=template_printview")
    
def create_pdf(link, string, img):
    pdf = FPDF()
    pdf.add_page()

    #Draws vertical/horizontal lines across the page
    pdf.line(105, 0, 105, 297)
    for i in range(1,6):
        pdf.line(0, i*49.5, 210, i*49.5)

    #Turns QR object into image
    pdf.image(img.get_image(), x=5, y=10, w=35, h=35)

    #Adds scan here text to the label
    pdf.set_font("Helvetica", size=16, style="B")
    pdf.text(x=8, y=10, text="Scan here for drug datasheet")

    pdf.set_xy(x=40, y=15)
    current_font = 20
    pdf.set_font("Helvetica", size=current_font)
    while pdf.get_string_width(string) > 170:
        current_font -= 1
        pdf.set_font("Helvetica", size=current_font)
    pdf.multi_cell(w=60, text=string, align="C", max_line_height=pdf.font_size)

    pdf.set_xy(x=40, y=38)
    pdf.set_font("Helvetica", size=10)
    pdf.cell(w=60, text=f"noahcompendium.co.uk/?id=-{link}", align="C")

    #Creates file in datasheet folder
    file_name = re.sub(r'[/\\:*?"<>|]', '', string)
    pdf.output(f"datasheets/{file_name}.pdf")
    

if __name__ == "__main__":
    main()