import cv2 

img = cv2.imread("qr.png")
detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(img)
print(url, coords, pixels)