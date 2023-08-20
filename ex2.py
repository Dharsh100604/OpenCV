import cv2
#import numpy as np
img = cv2.imread('bgimg.png',0)
print(img)
cv2.imshow('v',img)  #img will store in v
cv2.waitKey(0)  #image will display until u press escape key
cv2.imwrite('dharsh.png',img) #copy of the image
cv2.destroyAllWindows()  