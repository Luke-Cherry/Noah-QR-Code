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
    pdf.image(img.get_image(), x=5, y=5, w=30, h=30)

    pdf.output("test.pdf")

    

if __name__ == "__main__":
    main()