import cv2
import numpy as np
import matplotlib.pyplot as plt

def fotografNegatifiAl(foto):
    maxDeger = np.max(foto)
    negatif_foto = maxDeger - foto
    return negatif_foto


resim = cv2.imread('foto/foto.jfif',0)#virgül 0 dersek opencv fotoğrafı bilgisayara siyah beyaz olarak yükler.

yeniResim = fotografNegatifiAl(resim)
print(np.max(resim))
yanYana = np.hstack((resim,yeniResim))
#Bu fonksiyon arrayleri yanyana birleştirir.vstack'de üst üste birleştirir.

cv2.imshow('resim',yanYana)
cv2.waitKey(0)
cv2.destroyAllWindows()
