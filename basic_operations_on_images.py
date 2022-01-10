import numpy as np
import cv2

img = cv2.imread("images.jpg")

print(img.shape)
print(img.dtype)
print(img.size)

b, g, r = cv2.split(img)
# img = cv2.merge(b, g, r)

ball = img[200:150, 230:180]
img[200:150, 230:180] = ball


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()