import cv2 

video = cv2.VideoCapture(0) #1st webcam
cv2.namedWindow("Window")

while True:
    success, frame = video.read()
    # cv2.imshow("Window", frame)
    height = frame.shape[0]
    width = frame.shape[1]

    face_cascade = cv2.CascadeClassifier('faces.xml')
    op = cv2.VideoWriter('op1.avi', cv2.VideoWriter_fourcc(*'DIVX'),30, (width, height))

    while success:
        faces = face_cascade.detectMultiScale(frame, 1.1, 4)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255),4)
        op.write(frame)
    success, frame = video.read()

    #This breaks on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
# success,frame = video.read()

# height = frame.shape[0]
# width = frame.shape[1]

# face_cascade = cv2.CascadeClassifier('faces.xml')
# op = cv2.VideoWriter('op1.avi', cv2.VideoWriter_fourcc(*'DIVX'),30, (width, height))

# while success:
#     faces = face_cascade.detectMultiScale(frame, 1.1, 4)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255),4)
#     op.write(frame)
#     success, frame = video.read()

# op.release()