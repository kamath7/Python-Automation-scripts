import cv2 

video = cv2.VideoCapture("video.mp4")
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
no_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
print(width, " ", height, " ", no_frames)