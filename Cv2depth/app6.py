import cv2 

vid = cv2.VideoCapture(0)
success,frame = vid.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')

op = cv2.VideoWriter('op.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

count = 0 

while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255),4)
    cv2.imshow('Recording', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    op.write(frame)
    success,frame = vid.read()
    count += 1

op.release()
