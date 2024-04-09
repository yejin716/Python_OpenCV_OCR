import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

a = Image.open('./Test_3/LDM1.png')
result = pytesseract.image_to_string(a, lang='kor+eng')
print(result)