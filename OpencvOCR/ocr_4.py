import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

path_img = './OpencvOCR/cropped.jpg'
result = pytesseract.image_to_string(path_img, lang='kor+eng')
print(result)