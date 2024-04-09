#외각선 따고 문자인식
import sys
import numpy as np
import cv2 
import pytesseract

label = cv2.imread('img_Captured.png')

if label is None:
    print('image load failed')
    sys.exit()

label = cv2.resize(label, (0,0),fx=0.2, fy=0.2) # 사이즈 설정

src_gray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY) #흑백으로 

th, src_bin = cv2.threshold(src_gray, 0, 255, 
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU) #자동 이진화
print(th) #스레솔드 값 

contours, _ =cv2.findContours(src_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #contours = 리스트
print(len(contours))

#외각선 검출
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    if len(approx) != 4:
        continue

    #외각선 검출부분 나타내기
    w, h = 900, 500
    srcQuad = np.array([[approx[0, 0, :]], [approx[1, 0, :]],
                        [approx[2, 0, :]], [approx[3, 0, :]]]).astype(np.float32)
    dstQuad = np.array([ [w, 0],[w, h], [0, h],[0 ,0] ]).astype(np.float32) #출력점 순서 맞추기
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(label, pers, (w,h))

    dst_rgb = cv2.cvtColor(label, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(src_bin, lang='Hangul+eng'))

    cv2.polylines(label, pts, True, (0, 0, 255))

dst = cv2.resize(dst, (0,0),fx=0.2, fy=0.2)
cv2.imshow('src',label)
cv2.imshow('src_gray',src_gray)
cv2.imshow('src_bin',src_bin) 
# cv2.imshow('dst',dst) 
cv2.waitKey()
cv2.destroyAllWindows()