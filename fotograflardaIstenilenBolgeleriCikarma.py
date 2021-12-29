from filtrelemedeKullanilacakGenelFonksiyonlar import konvolusyon,gaussFiltreOlustur
import cv2
import numpy as np

foto = cv2.imread('space.tif',0)

esik_degeri =125
esik_maske = foto>esik_degeri
# Şimdi bir maske oluşturarak pixel değeri 125 ve altında olan bütün pixelleri siyaha dönüştürdük.
# Bu işlem sayesinde fotoğrafımız 2 bit bir fotoğraf oldu.
# Fakat istediğimiz noktaları bu şekilde elde edemeyiz. İlk önce düşük geçiren bir filtreyle konvolusyon uygulamamız lazım.
#Bunu yaptığımız zaman fotoğraftaki yüksek frekansa sahip değerler çıkışa geçemeyeceği için noktalardan kurtulmuş oluruz.
#Burada küçük noktaları gürültü olarak düşünelim.

sigma = 5
m=n=6*sigma+1
gaussKernel =gaussFiltreOlustur(m, n, 1, sigma)
filtreliFoto =konvolusyon(foto, gaussKernel)

bulanik_esik_maske = filtreliFoto>esik_degeri
bos = np.empty(filtreliFoto.shape,np.uint8)

esik_degeri =125
esik_maske = filtreliFoto>esik_degeri
bos = np.empty(bulanik_esik_maske.shape,np.uint8)
for a,sutun in enumerate(bulanik_esik_maske):
    for b,pixel in enumerate(sutun):
        if pixel==False:
            bos[a,b]=0
        else:
            bos[a,b]=255


cv2.imshow('',bos)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Bu şekilde istediğimiz bölgeleri çıkarmış olduk.
#Yani küçük olan istemediğimiz noktaları çıkarmış olduk.

