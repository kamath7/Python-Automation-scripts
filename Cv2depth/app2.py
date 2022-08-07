import cv2 

video = cv2.VideoCapture("kk.mp4")
# print(video.read()) #gives a tuple
success, frame = video.read()
count = 1
while success:
    cv2.imwrite(f'images//{count}.jpg', frame)
    success, frame = video.read()
    count += 1