
import cv2
import numpy as np
import os

# img=cv2.imread('group6_11/sample.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow('result',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def facewaku(img1):
    cascade_path =  "group6_11/cascades/haarcascade_frontalface_default.xml"
    
    cascade = cv2.CascadeClassifier(cascade_path)

    img=img1
    #grayscale
    img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    assert os.path.isfile(cascade_path), 'haarcascade_frontalface_default.xml がない'
    
    
    facerect = cascade.detectMultiScale(img_g, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))


    print(facerect)
    color = (255, 255, 255) #白

    # 検出した場合
    if len(facerect) > 0:

    #検出した顔を囲む矩形の作成
        for rect in facerect:
            cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
 
    
    cv2.imwrite('group6_11/facewaku/result', img)
    
    #cv2.imwrite('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#画像の保存
#i=0
#cv2.imwrite(f"./facewaku/face_rectangle{i}.jpg", img)
#i=i+1


if __name__ == "__main__":
 #この辺にwatchdog
 img1 = cv2.imread('group6_11/sample2.jpg')
 
 facewaku(img1)
