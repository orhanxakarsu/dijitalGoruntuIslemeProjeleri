import cv2
import numpy as np
from filtrelemedeKullanilacakGenelFonksiyonlar import boxFiltreOlustur,gaussFiltreOlustur,korelasyon


foto = cv2.imread('celeba.jpg',0)

#boxFiltre=korelasyon(foto, boxFiltreOlustur(37, 1))
gaussFiltre =korelasyon(foto, gaussFiltreOlustur(5, 5, 2, 15))

#birlestirilmisFoto =np.hstack((boxFiltre,gaussFiltre))

print(gaussFiltreOlustur(5, 5, 1, 1))

cv2.imshow('',gaussFiltre)

cv2.waitKey(0)
cv2.destroyAllWindows() 