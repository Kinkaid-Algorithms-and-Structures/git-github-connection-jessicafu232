import cv2
import numpy as np
import scipy

print ("Hello, world")

box = np.ones([400,400],dtype=float)

for i in range(400):
    box[:,i] = i*0.0025

cv2.imshow("gradient",box)

cv2.waitKey(0)
cv2.destroyAllWindows()