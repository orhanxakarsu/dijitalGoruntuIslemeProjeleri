import numpy as np
import cv2


def boxFiltreOlustur(boyut,katsayi):
    normallestirilmemisFiltre =np.ones((boyut,boyut),dtype=float)*katsayi
    return normallestirilmemisFiltre/normallestirilmemisFiltre.sum()


def gaussFiltreOlustur(m,n,K,sigma):
    yarim_m = m//2 #2 bölme işareti kullanırsak böldüğü değeri int e yuvarlar.
    yarim_n = n//2;
    
    gaussFiltre = np.empty((m,n))#Empty ingilizcede boş demek. Burada boş bir array oluşturuyoruz.
    
    
    #Biz indexleme yaparken orta noktayı 0,0 olarak almıştık fakat python'da indexleme bu şekilde çalışmaz.
    # O yüzden enumerate fonksiyonunu kullanarak gerçek indexini tutmuş olduk.
    for s in range(-yarim_m,yarim_m+1):
        for t in range(-yarim_n,yarim_n+1):
            r_kare = s**2 + t**2
            payda = 2* sigma**2
            kuvvet = -(r_kare/payda)
            deger = K*np.exp(kuvvet)
            python_s = yarim_m+s
            python_t = yarim_n +t
            gaussFiltre[python_s,python_t] =deger
    return gaussFiltre/gaussFiltre.sum() # Sum içindeki bütün elemanları toplar.
       


#Biz korelasyonda, konvolüsyon ve medyan filtrelemede de ortak yaptığımız bir şey var->

#Teker teker bir filtre yardımıyla bütün fotoğrafı dolasmak.


def filtrele(giris,kernel_yada_filtre, yapilacakIslem):
    m,n = kernel_yada_filtre.shape
    yarim_m = m//2
    yarim_n = n//2
    sifirEklenmisGiris = np.pad(giris,
                                  ((yarim_m,yarim_m),(yarim_n,yarim_n)),
                                  constant_values=((0,0),(0,0)))
    #np.pad fonksiyonu fotoğrafın etrafına 0'lar ekler
    # İlk verdiğimiz tupplede üstüne ve altına ne kadar sıfır eklememiz gerektiğini söylüyoruz
    # İkinci tupple'de ise soluna ve sağına ne kadar 0 eklememiz gerektiğini belirtiyoruz.
    # Son değerler de bu üst,alt, sol , sag bölgelerine ne eklememiz gerektiğini söylüyoruz.
    #Fotoğrafımıza ne kadar 0 eklememiz gerektiğini anlamak için de kernel boyutunu yarıya bölmemiz yetiyor.
    # Mesela 5x5 bir kernel kullanacaksak 5//2 = 2 yapar. Kernelin kenarlarına 2 sıra 0 eklersek sorunumuz çözülür.
    #Burada tupplelerin eklenme sebebi budur.
    sifirEklenmisGiris = sifirEklenmisGiris.astype(float)
    M,N = sifirEklenmisGiris.shape[:2]
    cikisFoto = np.full_like(sifirEklenmisGiris,0)
    for satir in range (yarim_m,M-yarim_m):
        for sutun in range(yarim_n,N-yarim_n):
            girisPencere = sifirEklenmisGiris[satir-yarim_m:satir+yarim_m+1,sutun-yarim_n:sutun+yarim_n+1]
            cikisFoto[satir,sutun] = yapilacakIslem(girisPencere,kernel_yada_filtre)
            #Biz burada bu fonksiyona fonksiyon vermemiz gerekiyor. Verdiğimiz fonksiyon bize üzerinde bulunduğumuz pencereye ne yapmamız gerektiğini söyleyecek
    print(cikisFoto.shape)
    return cikisFoto.astype(np.uint8)



def korelasyon(girisPencere,kernel):
    yapilacakIslem = lambda girisPencere,kernel:((girisPencere*kernel)).sum()
    return filtrele(girisPencere, kernel, yapilacakIslem)


def medyanFiltre(giris,m,n):
    bosFiltre = np.empty((m,n))
    yapilacakIslem = lambda giris,kernel:np.median(giris)
    return filtrele(giris, bosFiltre, yapilacakIslem)
    

def konvolusyon(girisPencere,kernel):
    kernel = np.fliplr(kernel)#matrisi soldan sağa döndürür
    kernel = np.flipud(kernel)#matrisi aşağıdan yukarı döndürür
    return korelasyon(girisPencere, kernel)
            
def ekranaYaz(foto):
    cv2.imshow('',foto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
def araligiDagit(foto):
    foto = foto.astype(float)
    enKucukCikarilmisFoto = foto-np.min(foto)
    enBuyukBolunmusFoto = foto/np.max(foto)
    sonFoto = enBuyukBolunmusFoto*255
    return sonFoto.astype(np.uint8)






