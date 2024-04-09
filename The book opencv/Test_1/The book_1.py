import sys
import cv2

img = cv2.imread('Label.jpg')

if img is None:  #없는 이미지일 경우 
    print('Image load failed') #실행
    sys.exit()
    
# print(type(img)) #이미지 정보 불러오기
# print(img.shape)
# print(img.dtype)

# cv2.namedWindow('image')  #이미지 불러오는 창 
cv2.imshow('image', img)
cv2.waitKey()