import numpy as np
import cv2



def yerelHistogramİstatistikleri(foto,k0,k1,k2,k3,C,pencereBoyutu):
    foto = foto.astype(float)
    globalOrtalama = foto.sum()/foto.size#ya da direk np.mean() fonksiyonuyla
    globalStandartSapma = np.std(foto) # Standart sapmayı verir.
    ortalamaAltSinir = k0*globalOrtalama
    ortalamaUstSinir = k1*globalOrtalama
    standartSapmaAltSinir= k2*globalStandartSapma
    standartSapmaUstSinir= k3* globalStandartSapma
    
    pencereBoyutu=int(pencereBoyutu/2)
    M,N = foto.shape[:2]
    #Burada yağmak istediğimiz şey oluşturduğumuz pencerenin sağ alt ve sol üst->
    #-> köşesini elde etmek. Bunun için de pencere boyutunu yarıya böldük.
    # Tek sayı da olsa çift sayı da olsa pencere boyutunun yarısı bize pencerenin->
    #-> Uç noktalarının ne kadar uzaklaşması gerektiğini söyler.
    
    satirIndexleri =[]
    sutunIndexleri = []
    
    for satir in range(M):
        # O anki sütun bizim orta noktamızın bulunduğu sütun.
        ust = max(0,satir -pencereBoyutu)
        alt = min(M,satir+ pencereBoyutu+ 1)
        #alt'da +1 olmasının sebebi, Python'daki indexleme mantığıdır.
        for sutun in range(N):
            sol = max(0,sutun - pencereBoyutu)
            sag = min(N,sutun + pencereBoyutu +1)
           
            pencere_pixelleri = foto[ust:alt,sol:sag]
            ortalamaPencere = np.mean(pencere_pixelleri)
            pencereStandartSapma = np.std(pencere_pixelleri)
           
            ortalamaKosulu = ortalamaAltSinir <=ortalamaPencere and ortalamaPencere <= ortalamaUstSinir
            standartSapmaKosulu = standartSapmaAltSinir<= pencereStandartSapma and pencereStandartSapma <= standartSapmaUstSinir
            kosul =ortalamaKosulu and standartSapmaKosulu
            if(kosul):
                satirIndexleri.extend(list(range(sol,sag)))
                sutunIndexleri.extend(list(range(ust,alt)))                       
                 
    
    satirIndexleri =np.uint32(satirIndexleri)
    sutunIndexleri =np.uint32(sutunIndexleri)
    foto[sutunIndexleri,satirIndexleri] *= C
    
    return foto.astype(np.uint8)




def main():
   foto = cv2.imread('1.tif',0)
   foto2 =yerelHistogramİstatistikleri(foto,0,0.1,0,0.1,23,3)
   birlestirilmisFoto = np.hstack((foto,foto2))
   cv2.imshow('',birlestirilmisFoto)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   
   
if __name__=="__main__":
    main()