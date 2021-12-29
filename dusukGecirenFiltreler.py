import cv2
import numpy as np

# Burada yapacağımız 3 ana şey var.

#İlki resim bulanıklaştırma

# İkincisi salt and papier noise denen gürültü 

#Üçüncüsü ise fotoğrafın içindeki konumunu belirlemek istediğimiz bazı bölgelerde kullanacağız



def main():
    a = np.array(range(6)).reshape((3,2))
    #normallestirilmemisFiltre =np.ones((3,3),dtype=float)*3
    print(a[2,1])


if __name__ =='__main__':
    main()