import cv2

image = cv2.imread('humans.jpeg',1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)