import cv2 
import webbrowser

video = cv2.VideoCapture(1)
success, frame = video.read()
detector = cv2.QRCodeDetector()


while success:
    url, coords, pixels = detector.detectAndDecode(frame)
    
    if url:
        print(f"Opening {url}")
        webbrowser.open(url)
        break
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break
    success, frame = video.read()

video.release()
cv2.destroyAllWindows()
# img = cv2.imread("qr.png")



# print(url, coords, pixels)
