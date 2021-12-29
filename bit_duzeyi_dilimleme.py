import cv2
import numpy as np

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

def stackv(*args):
    return np.vstack(args)


foto = cv2.imread('foto/foto.jfif',0)

#0<=bit düzlemi sayisi<=7
def bitDuzlemiDilimleme(foto,bitDuzlemi):
    #burada kullanacağımız fonksiyon np.bitwise_and()
    #bu fonksiyon için ilk önce elimizdeki fotoğrafla aynı boyutta olan ve
    #istediğimiz bitin derecesine sahip olan(eğer 6. bit düzeyini istiyorsak, 2^5 =elemanlarının hepsi 32 olan matris)
    #kullanmamız lazım(np.full_like kullanabiliriz). 
    #Sonra np.bitwise_and(kendiMatrisimiz,bitDuzeyiMatrisi) dersek,
    #Numpy arka tarafta her sayıyı 2 bite dönüştürüyor. Bunlarda istediğimiz düzeyi karşılaştırıp bize,
    #Eğer istediğimiz değer bit düzeyinde yoksa 0'ı, varsa da elemanları istediğimiz değer olan kendi matrisimizle aynı boyuta sahip olan bir matris döndürüyor.
    #Python'da bir sayıyı bit halinde gösterme : f"{sayi:08b}"(8 bit şeklinde gösterir)
    foto2=np.full_like(foto,2**bitDuzlemi)
    return np.bitwise_and(foto,foto2)

def fotoSikistirma(foto,hangiDuzey):
    bosDizi=np.full_like(foto,0)
    for i in hangiDuzey:
        bosDizi+=bitDuzlemiDilimleme(foto,i)
    return bosDizi
        

butunBitDuzlemleri =[]
for i in range(8):
    butunBitDuzlemleri.append(rescale(bitDuzlemiDilimleme(foto,i)))

butunBitDuzlemleri=butunBitDuzlemleri[::-1]
#Üstteki yaptığım şey bütün elemanları ters çevirir.

foto1 = stack(butunBitDuzlemleri[0],butunBitDuzlemleri[1],butunBitDuzlemleri[2])
foto2 = stack(butunBitDuzlemleri[3],butunBitDuzlemleri[4],butunBitDuzlemleri[5])
foto3 = stack(butunBitDuzlemleri[6],butunBitDuzlemleri[7],butunBitDuzlemleri[7])

sonFoto =stackv(foto1,foto2,foto3)
deneme=fotoSikistirma(foto,[6,7])
cv2.imshow('',deneme)
cv2.waitKey(0)
cv2.destroyAllWindows()

