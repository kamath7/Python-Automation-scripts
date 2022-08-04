import cv2

img = cv2.imread('./elfs.jpeg')
img2 = cv2.imread('./watermark.png')

print(img2.shape)

x = img.shape[1] - img2.shape[1]  # finding the end
y = img.shape[0] - img2.shape[0]

water_place = img[y:, x:]
cv2.imwrite('water_place.jpeg', water_place)

blend = cv2.addWeighted(water_place, 0.5, img2, 0.5, 0)
cv2.imwrite('blender.jpeg', blend)

img[y:, x:] = blend 
cv2.imwrite('watermak.jpeg', img)