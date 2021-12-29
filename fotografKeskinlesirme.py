import numpy as np
import cv2
from filtrelemedeKullanilacakGenelFonksiyonlar import korelasyon,araligiDagit,gaussFiltreOlustur

def ikinciTurevdenKeskinlestir(foto,c):
    foto = foto.astype(np.uint16)
    filtre1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    filtre2=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    
    filtrelenmisResim = korelasyon(foto, filtre2)
    sifirEklenmisFoto = np.pad(foto,
                                  ((1,1),(1,1)),
                                  constant_values=((0,0),(0,0)))
    resim = araligiDagit(filtrelenmisResim)
    toplam= sifirEklenmisFoto+c*resim
    #return araligiDagit(toplam)
    return araligiDagit(toplam)

def bulaniklastirarakKeskinlestirme(foto,boyut,k):
    padIcin = boyut//2
    foto = foto.astype(np.uint16)
    bulaniklastirilmisFoto = korelasyon(foto,gaussFiltreOlustur(boyut, boyut, 1, boyut//6))
    genisletilmisFoto = np.pad(foto,((padIcin,padIcin),(padIcin,padIcin)),
                               constant_values=((0,0),(0,0)))
    deger = genisletilmisFoto - bulaniklastirilmisFoto
    sonResim = genisletilmisFoto+k*araligiDagit(deger)
    return sonResim.astype(np.uint8)


def birinciTurevKeskinlestir(foto):
    foto =foto.astype(float)
    sobelKernelX = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    sobelKernelY = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    keskinResimX = korelasyon(foto, sobelKernelX)
    keskinResimY = korelasyon(foto,sobelKernelY)
    sonResim = np.sqrt(keskinResimX**2 + keskinResimY**2)
    #bu son resimle direk köşeleri bulabiliriz.
    genisletilmisFoto = np.pad(foto,((1,1),(1,1)),
                               constant_values=((0,0),(0,0)))
    toplanmisResim =sonResim+genisletilmisFoto
    return (toplanmisResim).astype(np.uint8)


foto = cv2.imread('3.jpg',0)
keskinlestirilmisResim1 = ikinciTurevdenKeskinlestir(foto,0.01)
cv2.imshow('',keskinlestirilmisResim1)
cv2.waitKey(0)
cv2.destroyAllWindows()


#filtreY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])



