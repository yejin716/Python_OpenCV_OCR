import cv2
import numpy as np
import pytesseract

img = cv2.imread('img_captured.png')

x,y,w,h = cv2.selectROI('img',img,False)

if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped',roi)
    cv2.imwrite('Test_1/cropped.jpg',roi)

    ocr = pytesseract.image_to_string('Test_1/cropped.jpg', lang='kor')
    print(ocr)

cv2.waitKey(0)
cv2.destroyAllWindows()