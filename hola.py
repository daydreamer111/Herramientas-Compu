import cv2
import numpy as np

img = "/home/pedros/Documents/Jackie/leo.jpeg"
image = cv2.imread(img)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_copy = image.copy()

#rickett = [[1,1,1],[0,0,0],[-1,-1,-1]]
#rickett_y = np.asarray(rickett)
#print(rickett_y)
print(image)
count = 0

for i in range(0, image.shape[0]):
     for j in range(0, image.shape[1]):
          for k in range(0, image.shape[2]):
              if count == 1:
                  image[i][j] = [0,0,0]
              elif count == 2:
                  image[i][j] = image[i][j]*-1
          count+=1
          if count == 3:
              count = 0
              sum = image[i][j][0] + image[i][j][1] + image[i][j][2]
              sum += image[i][j-1][0] + image[i][j-1][1] + image[i][j-1][2]
              sum += image[i][j-2][0] + image[i][j-2][1] + image[i][j-2][2]
              image[i][j-1][1] = sum

while True:
    cv2.imshow("Output", image)
    cv2.waitKey(10)

cv2.destroyAllWindows()
