# ********************** Text Extraction from Image ****************************

# Importing Libraries
import pytesseract
from PIL import Image

# https://sourceforge.net/projects/tesseract-ocr/files/latest/download
if __name__ == '__main__':
    
    # Opening the tesseract.exe file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\VAIBHAV\AppData\Local\Tesseract-OCR\tesseract.exe'
    # Opening image using PIL library
    img = Image.open('img.jpg')
    # parsing image to the pytesseract function image_to_string(image)
    text = pytesseract.image_to_string(img)
    print(text)
