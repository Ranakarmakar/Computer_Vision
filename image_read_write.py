import cv2

pic = cv2.imread("lena.jpg", 1)
print(pic)
cv2.imshow("image", pic)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena_copy.png", pic)
