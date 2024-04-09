import cv2 as cv
import os
import pytesseract
from PIL import Image

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Camera open failed")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Can't read camera")
        break

    cv.imshow('pc_Label', img) 
    if cv.waitKey(1) == ord('c'):
        img_captured = cv.imwrite('img_captured.png',img)
    if cv.waitKey(1) == ord('q'):
        break

    

cap.release()
cv.destroyAllWindows()

   