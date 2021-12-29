import matplotlib.pyplot as plt
import numpy as np
import cv2


def stack(*args):
    return np.hstack(args)

#Kolay Method:
def cv2_main():
    foto=cv2.imread('foto_.jfif',0)
    #Altta kullandığımız fonksiyon cv2 içinde tanımlı bizim için histogram eşitleme yapan fonksiyon
    hist_esitlenmis_foto = cv2.equalizeHist(foto)
    birFoto =stack(foto,hist_esitlenmis_foto)
    cv2.imshow('',birFoto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Benim yaptığım fonksiyon:
def olustur(foto,fotonunBitDegeri):
    toplamPixelSayisi = int(foto.size)
    pixeller=list(range(256))
    degerler =np.zeros(256,dtype=float)
    sonuclar =np.full_like(foto,0)
    
    for i in pixeller:
        for sutun in foto:
            for pixel in sutun:
                if i==pixel:
                    degerler[i]+=1
    degerler = degerler/toplamPixelSayisi
    gecici=0
    for pixel in pixeller:
        for i in range(pixel+1):
            gecici+=255*degerler[i]
        sonuclar[foto==pixel]=int(gecici)
        gecici=0
    return sonuclar.astype(np.uint8)
            
        
#Videoda yaptıkları:
def histogramOlustur(foto,L):
    histogram,bins = np.histogram(foto,bins=L,range=(0,L))
    
def normallestirilmisHistogramOlustur(foto,L):
    histogram =histogramOlustur(foto,L)
    return histogram/foto.size

def kumulatifDagilimOlustur(p_r_r):#p_r_r formüldeki Pr(r) fonksiyonu
    #cumsum() methodu direk verdiğimiz arrayin kümülatif dağılımını veriyor
    return np.cumsum(p_r_r)

def histogramEsitleme(foto,L):
    p_r_r=normallestirilmisHistogramOlustur(foto,L)
    kumulatifDagilim=kumulatifDagilimOlustur(p_r_r)
    donusumFonksiyonu = (L-1)*kumulatifDagilim
    shape=foto.shape
    ravel = foto.ravel()#Bu method bizim çok boyutlu dizimizi tek boyuta dönüştürüyor.
    hist_est_foto = np.zeros_like(ravel)
    for i,pixel in enumerate(ravel):
        #enumerate fonksiyonu 2 parametre alır. İlk index değeri ikincisi de o indexte dizinin vereceği degerdir.
        hist_es_foto[i] = donusum_fonksiyonu[pixel]
    return hist_es_foto.reshape(shape).astype(np.uint8)
        
    
    

def main():
    foto=cv2.imread('foto_.jfif',0) 
    yeniResim =histogramEsitleme(foto,256)
    birFoto =stack(foto,yeniResim)
    cv2.imshow('',birFoto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()





      
                
    








