import cv2
import os
import numpy as np

# for the collage
columns = 3
rows = 2

horizontal_margin = 40
vertical_margin = 20

images = os.listdir('collageImages')
print(images)

shape = cv2.imread('collageImages/1.jpeg').shape

big_image = np.zeros((shape[0] * rows + horizontal_margin * (rows + 1),
                     shape[1] * columns + vertical_margin * (columns + 1), shape[2]), np.uint8)
                     
cv2.imwrite('grid.jpeg', big_image)
