import cv2
import numpy as np


resim =cv2.imread('foto/rontgen.jfif')

def stack(*args):
    return np.hstack(args)

def logDonusumu(c,resim):
    array =c* np.log(resim.astype(float)+1)# Log fonksiyonu numpy kütüphanesine tanımlıdır.
    #astype(float) dememizin sebebi resimde kullanılan arraylerin tipi int8'dir. Yani 8 bittir.
    #Ama biz 1 ile topladığımız zaman 255 değeri 256 olabiliyor. Bu da array'de sıfırlanmasına yol açabiliyor.
    #Bu bizim istemediğimiz bir durum. Bu yüzden int8 tipinden float tipine çeviriyoruz.
    return rescale(array)

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
    

logDonusumuneUgramisResim =logDonusumu(1,resim)

#duzeltilmisResim = rescale(logDonusumuneUgramisResim)
eskiYeniBirlestir =stack(resim,logDonusumuneUgramisResim)
print(eskiYeniBirlestir)
cv2.imshow("Log Dönüşümü",eskiYeniBirlestir)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(np.max(logDonusumuneUgramisResim))