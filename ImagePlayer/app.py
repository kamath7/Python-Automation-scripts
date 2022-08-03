import cv2

color = cv2.imread("galaxy.jpeg", 0)
print(color) #color matrices

#creating to grayscale
cv2.imwrite('grayscale.jpg',color)