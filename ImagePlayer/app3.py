import cv2 

def calc_size(scale_percentage, width, height):
    new_width = int(round(width * scale_percentage / 100))
    new_height = int(round(height * scale_percentage / 100))
    return (new_width, new_height)

def resize(img_path, scale_percentage,resize_path="./"):
    image = cv2.imread(img_path)
    new_dim = calc_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resize_path,resized_image)

resize('./galaxy.jpeg',200,'./oorlalle.jpeg')