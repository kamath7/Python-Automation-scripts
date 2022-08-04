import cv2
import numpy as np

foreground = cv2.imread('./giraffe.jpeg')
background = cv2.imread('./safari.jpeg')

width = foreground.shape[1]
height = foreground.shape[0]

# print(foreground(40, 40))
resized_bg = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j,i]

        if np.any(pixel == [1, 255, 0]) :
            foreground[j,i] = resized_bg[j,i]


cv2.imwrite('op.jpeg', foreground)