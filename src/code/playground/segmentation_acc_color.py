import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

img = cv2.imread('sample2.jpg', 0)
print(img)
print("hi")
hist = cv2.calcHist([img],[0],None,[256],[0,256])
colors = np.where(hist>100)
img_number = 0
for color in colors[0]:
    #print(color)
    split_image = img.copy()
    split_image[np.where(img != color)] = 0
    cv2.imwrite(str(img_number)+".jpg",split_image)
    img_number+=1
plt.hist(img.ravel(),256,[0,256])
plt.savefig('plt')
plt.show()