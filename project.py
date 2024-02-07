import os
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
    #file_name = check_csv(input("Please enter the name of the csv file: "))
    
    #read_csv(file_name)
    read_csv("NoahDownload.csv")


#Check CSV valid, returns number of rows
def check_csv(file_name):
    while True:
        if not file_name:
            print("Error: Please enter a filename.")
            file_name = input("Please enter the name of the CSV file: ")
        elif not os.path.isfile(file_name):
            print(f"Error: File '{file_name}' not found.")
            file_name = input("Please enter the name of the CSV file: ")
        else:
            return file_name

#Reads CSV file
def read_csv(file_name):
    links_list = []
    with open(file_name, encoding="UTF-8-sig") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            links_list.append(row)

    for row in links_list:
        #print(row)
        create_pdf(row[1], row[0] , create_qrcode(row[1]))

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

    for x in range(0, 1):
        for y in range(0, 6):
            x_offset = x * 105
            y_offset = y * 49.5
            print(x_offset, y_offset)
            #Turns QR object into image
            pdf.image(img.get_image(), x=5+x_offset, y=10+y_offset, w=35, h=35)

            #Adds scan here text to the label
            pdf.set_font("Helvetica", size=16, style="B")
            pdf.text(x=8+x_offset, y=10+y_offset, text="Scan here for drug datasheet")

            pdf.set_xy(x=40+x_offset, y=15+y_offset)
            current_font = 15
            pdf.set_font("Helvetica", size=current_font)
            while pdf.get_string_width(string) > 170:
                current_font -= 1
                pdf.set_font("Helvetica", size=current_font)
            #pdf.multi_cell(w=60, text=string, align="C", border=1)

            pdf.set_xy(x=40+x_offset, y=30+y_offset)
            pdf.set_font("Helvetica", size=10)
            pdf.cell(w=60, text=f"noahcompendium.co.uk/?id=-{link}", align="C", border=1)

    #Creates file in datasheet folder
    file_name = re.sub(r'[/\\:*?"<>|]', '', string)
    pdf.output(f"datasheets/{file_name}.pdf")
    

if __name__ == "__main__":
    main()