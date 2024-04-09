#글자부분 사각박스 생성 후 문자인식
import cv2
import numpy as np
import pytesseract

class find_text():
     path = {
        'tesseract': r'C:\\Program Files\\Tesseract-OCR\\tesseract',
        'output': './OpencvOCR/Label_3.jpg'
    }
     margin =5 
##########################################################################
     def __init__(self):
        self.img = cv2.imread("./OpencvOCR/img_Captured.png")  #이미지 불러오기
##########################################################################
     def get_hulls(self, img): #배경이 아닌 다른부분찾아냄 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5),0)
     #    cv2.imshow('gray',gray) #회색조
     #    cv2.waitKey(0)
        mser = cv2.MSER_create()
        region, _ = mser.detectRegions(gray)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in region]
     #    print(hulls)
     #    self.setRectangle(gray, hulls, (0, 255, 0), 1)
     #    cv2.imshow('hulls_area', gray)
     #    cv2.waitKey(0)
        return hulls
    
     
    
     def setRectangle(self, img, hulls, color, thickness): #사각형그림
        margin = self.margin
        for j, cnt in enumerate(hulls):
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img,
                          (x-margin, y-margin),
                          (x + w + margin, y + h + margin),
                          color, thickness)
    ##########################################################################
     def leave_text_area(self, img):
        hulls = self.get_hulls(img)
        out_path = self.path['output'] #검정색
        mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
        self.setRectangle(mask, hulls, (255, 255, 255), -1) #흰색
     #    cv2.imshow("mask",mask)
     #    cv2.waitKey(0)

        img_text = cv2.bitwise_and(img, img, mask=mask) #비트연산
        cv2.imshow("text area", img_text)
     #    cv2.imwrite(out_path, img_text) #이미지 저장
        cv2.waitKey(0) 

     def get_text(self):
        path_img = self.path['output']
        pytesseract.pytesseract.tesseract_cmd = self.path['tesseract']
        config = ('-l kor+eng --oem 3 --psm 11')
        text = pytesseract.image_to_string(path_img, config=config)
        print('=========텍스트 인식 결과========')
        print(text)


ocr_text = find_text()
# ocr_text.get_hulls(ocr_text.img)
ocr_text.leave_text_area(ocr_text.img)
ocr_text.get_text()


        
    
