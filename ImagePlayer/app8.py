import cv2

foreground = cv2.imread('./giraffe.jpeg')
background = cv2.imread('./safari.jpeg')

width = foreground.shape[1]
height = foreground.shape[0]

# print(foreground(40, 40))

for i in range(width):
    for j in range(height):
        pixel = foreground[j,i]

        if list(pixel) == [28, 255, 76]:
            foreground[j,i] = background[j,i]


cv2.imwrite('op.jpeg', foreground)