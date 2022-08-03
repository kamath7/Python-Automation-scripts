import cv2
import os 

li_of_imgs = os.listdir('./images/')

for img in li_of_imgs:
    color = cv2.imread(f"images/{img}", 0)
    cv2.imwrite(f'imagesgray/gray={img}',color)
