import sys
from pyfiglet import Figlet

figlet = Figlet()

def main():
    #Prints initial title
    print(figlet.renderText("Noah QR Code"), end="")
    print("_" * 63)

#Check CSV valid, returns number of rows
def check_csv():
    ...

#Reads CSV file
def read_csv():
    ...

#Passes in link to convert it to a QR code 
def create_qrcode():
    ...



if __name__ == "__main__":
    main()