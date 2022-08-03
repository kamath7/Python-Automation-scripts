import cv2

image = cv2.imread('humans.jpeg',1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)

for (x,y,w,h) in faces:
    #x,y - coords
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 3) #x+w = first corner of the rectangle to the end 
    
cv2.imwrite('humanf.jpeg',image)