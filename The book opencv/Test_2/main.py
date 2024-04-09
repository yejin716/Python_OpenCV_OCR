#원본이미지로 문자인식
import pytesseract
import os

path_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

path_img = "./Test_2/img_captured.png"

pytesseract.pytesseract.tesseract_cmd = path_tesseract
config = ('-l kor+eng --oem 3 --psm 11')
text = pytesseract.image_to_string(path_img, config=config)
print(text)