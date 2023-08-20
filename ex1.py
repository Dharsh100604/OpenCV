import cv2
img = cv2.imread('bgimg.png',1)
print(img)
cv2.imshow('bgimg',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()