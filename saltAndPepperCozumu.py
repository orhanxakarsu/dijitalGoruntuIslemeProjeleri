import cv2
import numpy as np
from filtrelemedeKullanilacakGenelFonksiyonlar import korelasyon,medyanFiltre,ekranaYaz
foto = cv2.imread('salt_and_pepper.tif',0)



yeniFoto =medyanFiltre(foto, 7, 7)
ekranaYaz(yeniFoto)

