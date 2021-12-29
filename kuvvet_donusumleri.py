import cv2
import numpy as np

resim = cv2.imread('mr.jpg',0)



def duzenle(resim):
    minDeger = np.min(resim)
    maxDeger =np.max(resim)
    resim2 = resim.astype(float)
    resim2 = resim2- minDeger
    resim2 = resim2/maxDeger
    sonResim = resim2*255
    return sonResim.astype(np.uint8)


def kuvvetDonusumu(foto,c,y):
    #gamma değeri 1'den 0'a gittikçe fotoğraftaki beyaz yoğunluğu artar.
    #gamma değeri 1'den uzaklaştıkça fotoğraftaki siyah yoğunluğu artar.
    newFoto =c*foto**y
    return duzenle(newFoto)


cv2.imshow("",kuvvetDonusumu(resim, 1, 0.0001))
cv2.waitKey(0)
cv2.destroyAllWindows()