import watchdog
import cv2

def grayscale(self, img1):
 #グレースケール化
 self.img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
 cv2.imwrite(grayscale-img, self.img_gray)



if __name__ == "__main__":
 #この辺にwatchdog
 img1 = cv2.imread('google.png')
 grayscale(img1)