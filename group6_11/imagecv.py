
import cv2
import numpy as np
import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

target_dir = "group6_11/input-image"




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

# FileSystemEventHandler の継承クラスを作成
class FileChangeHandler(FileSystemEventHandler):
     # ファイル作成時のイベント
     def on_created(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s created' % filename)
         image_path="group6_11/input-image/" + filename
         img1=cv2.imread("image_path")
         facewaku(img1)

     # ファイル変更時のイベント
     def on_modified(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s changed' % filename)

     # ファイル削除時のイベント
     def on_deleted(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s deleted' % filename)

     # ファイル移動時のイベント
     def on_moved(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s moved' % filename)


if __name__ == "__main__":
 #この辺にwatchdog
 #img1 = cv2.imread('group6_11/sample2.jpg')
 
 #facewaku(img1)
 # ファイル監視の開始
     event_handler = FileChangeHandler()
     observer = Observer()
     observer.schedule(event_handler, target_dir, recursive=True)
     observer.start()
     # 処理が終了しないようスリープを挟んで無限ループ
     try:
         while True:
             time.sleep(0.1)
     except KeyboardInterrupt:
         observer.stop()
     observer.join()
