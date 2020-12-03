
import cv2
import numpy as np

# img=cv2.imread('group6_11/sample.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow('result',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def facewaku(img1):
    #cascade_path =  "./cascades/haarcascade_frontalface_default.xml"
    #cascade = cv2.CascadeClassifier(cascade_path)

    color = (255, 255, 255) #検出した顔を囲む四角形の色

    #grayscale
    img_g=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    
    # rect = cascade.detectMultiScale(img)
    # if len(rect) > 0:
    #     for x, y, w, h in rect:
    #         cv2.rectangle(img, (x, y), (x+w, y+h), color)

   
    cv2.imshow('result', img_g)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#画像の保存
#i=0
#cv2.imwrite(f"./facewaku/face_rectangle{i}.jpg", img)
#i=i+1


if __name__ == "__main__":
 #この辺にwatchdog
 img1 = cv2.imread('group6_11/sample.jpg')
 
 facewaku(img1)
