import cv2 


video = cv2.VideoCapture("kk.mp4")

no_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

# print(no_frames, fps )

timestamp = '00:00:15.03'
timestamp_list = timestamp.split(':')
timestamp_list_floats = [float(i) for i in timestamp_list]
# print(timestamp_list_floats)
hours,mins,secs = timestamp_list_floats
print(hours, mins, secs)

frame_nr = hours * 3600 * fps + mins * 60  * fps + secs * fps #frame at that timestamp

video.set(1, frame_nr)
success, frame = video.read()
cv2.imwrite('lalle.jpeg', frame)