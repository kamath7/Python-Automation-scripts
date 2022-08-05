import cv2 

vid = cv2.VideoCapture('video-sample.mp4')
success, frame = vid.read()
height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')

op = cv2.VideoWriter('myvid.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (height,width))

while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x,y ,w,h) in faces:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50,50))
    op.write(frame)
    success, frame = vid.read()

op.release()