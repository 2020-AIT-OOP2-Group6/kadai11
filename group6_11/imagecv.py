import cv2



def facewaku(img1):
    cascade_path =  "./cascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    color = (255, 255, 255) #検出した顔を囲む四角形の色

    #画像ファイルの読み込み
    img = cv2.imread(img1)

    #グレースケールに変換する
    img_g = cv2.imread(img,cv2.COLOR_BGR2GRAY)
 
    
    #rect = cascade.detectMultiScale(img_g)
    #if len(rect) > 0:
     #   for x, y, w, h in rect:
      #      cv2.rectangle(img_g, (x, y), (x+w, y+h), color)

    cv2.imshow('detected', img_g)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#画像の保存
#i=0
#cv2.imwrite(f"./facewaku/face_rectangle{i}.jpg", img)
#i=i+1


if __name__ == "__main__":
 #この辺にwatchdog
 img1 = cv2.imread('sample.png')
 
 facewaku(img1)