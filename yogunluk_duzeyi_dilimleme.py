import cv2
import numpy as np


def binaryDilimleme(foto,A,B,altDeger,ustDeger):
    foto_cikis = np.full_like(foto,altDeger)
    #full_like fonksiyonu bize solda verdiğimiz arrayın içindeki arrayın elemanlarının hepsini sagda verdiğimiz değer yap demek.
    index = np.logical_and(foto>A,foto>B)
    #logical_and fonksiyonu da bize true ve falselerden oluşan bir array gönderir.
    #İçine girdiğimiz koşulların gerçekleştiği elemanı true,gerçekleşmeyeni de false dondurur.
    foto_cikis[index] = ustDeger
    return foto_cikis

def linearDilimleme(foto,A,B,deger):
    fotoCikis=foto.copy()
    index = np.logical_and(foto>A,foto>B)
    fotoCikis[index]=deger
    return fotoCikis

def rescale(foto):
    #Log dönüşümünden sonra çıkan resmin pixel değerleri çok küçük bir aralıktaydı.
    #Biz bu fonksiyonda bu pixel aralığını ilk 0-1 arasında getiriyoruz.
    #Tabi kendi içindeki değişkenliği bozmadan.
    #Sonrasında da 255 ile çarpıp gelen değerleri yeni pixellerimiz yapıyoruz.
    foto = foto.astype(float)
    fotoMin =np.min(foto)
    fotoMax = np.max(foto)
    cıkarılmısFoto = foto - fotoMin
    birimFoto=foto/fotoMax
    sonFoto = birimFoto*255
    return sonFoto.astype(np.uint8)


def stack(*args):
    return np.hstack(args)

foto=cv2.imread('babun2.jpg',0)

degistirilmisFoto =binaryDilimleme(foto,150,200,20,235)

cv2.imshow('',degistirilmisFoto)
cv2.waitKey(0)
cv2.destroyAllWindows()


