import cv2

image = cv2.imread("data/imgs/automne.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("data/output/automne.jpg", image_gray)