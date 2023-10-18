import cv2
image = cv2.imread('ex.png')
filtered_image = cv2.blur(image, (5, 5))  # 第二个参数是滤波器的大小
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllwindows()

