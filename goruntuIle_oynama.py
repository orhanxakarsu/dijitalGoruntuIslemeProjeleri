import cv2
import numpy
resim =cv2.imread('babun2.jpg')

x=30
y=5
kanal=2

yogunluk = resim[x,y,kanal]
print(resim.shape)


cv2.imshow('einstein',resim[:70,:170])
cv2.waitKey(0)
cv2.destroyAllWindows()
print(resim.shape)
