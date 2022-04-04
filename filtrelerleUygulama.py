import tkinter as tk
from tkinter import ttk,filedialog
import cv2
import numpy as np
from PIL import Image,ImageTk







# root window
root = tk.Tk()
root.geometry("800x600")
root.title('Filtrele')
root.resizable(0,0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


def ekranaResimGetir(foto1):

    foto1 = foto1[:, :, ::-1]
    resim = Image.fromarray(foto1)
    img = resim.resize((300, 400), Image.ANTIALIAS)
    
    
    photo = ImageTk.PhotoImage(img)
    
    fotoLabel = ttk.Label(root, image = photo)
    fotoLabel.image = photo
    fotoLabel.grid(column=1,row=6)


def boxFilter():
    boyut = (int(boxKernelSatir.get()),int(boxKernelSutun.get()))
    
    kernel = np.ones(boyut,np.float32)/(boyut[0]*boyut[1])
    yeniFoto= cv2.filter2D(foto,-1 , kernel)
    ekranaResimGetir(yeniFoto)

def gaussFilter():
    boyut =(int(gaussKernelSatir.get()),int(gaussKernelSutun.get()))    
    yeniFoto = cv2.GaussianBlur(foto, boyut, int(gaussKernelSigma.get()))
    ekranaResimGetir(yeniFoto)

def medianFilter():
    boyut=int(medyanFiltreSatir.get())
    yeniFoto = cv2.medianBlur(foto,boyut)
    ekranaResimGetir(yeniFoto)
    
def bileteralFilter():
    boyut = int(biLeteralSatir.get())
    sigmaUzay = int(biLeteralSigmaUzay.get())
    sigmaRenk = int(biLeteralSigmaRenk.get())
    yeniFoto=cv2.bilateralFilter(foto, boyut, sigmaRenk, sigmaUzay)
    
    ekranaResimGetir(yeniFoto)


def fotografSec():
    
    dosyaIsmi = filedialog.askopenfilename(initialdir = "/",title = "Fotoğraf Seç")
    global foto
    stream = open(u'{0}'.format(dosyaIsmi), "rb")
    byte = bytearray(stream.read())
    numpyarray = np.asarray(byte, dtype=np.uint8)
    foto = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
    print(dosyaIsmi)

    ekranaResimGetir(foto)
    
    
    
    
# username

#Yazının Yeri
sayac=False
ilkSira = ttk.Label(root, text="Box Filtre Boyutu")
ilkSira.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)



#Box Kernelin Yeri
boxKernelSatir = ttk.Entry(root)
boxKernelSatir.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
if not sayac:
    boxKernelSatir.insert(tk.END,'1')

boslukIlk = ttk.Label(root, text="X")
boslukIlk.grid(column=2, row=0, sticky=tk.W, padx=2, pady=2)


boxKernelSutun = ttk.Entry(root)
boxKernelSutun.grid(column=3, row=0, sticky=tk.W, padx=5, pady=5)
if not sayac:
    boxKernelSutun.insert(tk.END,'1')


boxKernelButon = ttk.Button(root,text='Hesapla',command=boxFilter)
boxKernelButon.grid(column=6,row=0,sticky=tk.W, padx=2, pady=2)






#Yazının Yeri
ikinciSira = ttk.Label(root, text="Gauss Filtre Boyutu")
ikinciSira.grid(column=0, row=1, sticky=tk.W, padx=2, pady=2)



#Gauss Kernelin Yeri
gaussKernelSatir = ttk.Entry(root)
gaussKernelSatir.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

if not sayac:
    gaussKernelSatir.insert(tk.END,'1')

boslukIkı = ttk.Label(root, text="X")
boslukIkı.grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)


gaussKernelSutun = ttk.Entry(root)
gaussKernelSutun.grid(column=3, row=1, sticky=tk.W, padx=5, pady=5)
if not sayac:
    gaussKernelSutun.insert(tk.END,'1')
    
gaussKernelSigmaLabel = ttk.Label(root, text="Sigma Gir:")
gaussKernelSigmaLabel.grid(column=4, row=1, sticky=tk.E, padx=1, pady=1)

gaussKernelSigma = ttk.Entry(root)
gaussKernelSigma.grid(column=5, row=1, sticky=tk.E, padx=5, pady=5)
gaussKernelSigma.insert(tk.END,'35')



gaussKernelButon = ttk.Button(root,text='Hesapla',command=gaussFilter)
gaussKernelButon.grid(column=6,row=1,sticky=tk.W, padx=2, pady=2)



#Yazının Yeri
ucuncuSira = ttk.Label(root, text="Medyan Filtre Boyutu")
ucuncuSira.grid(column=0, row=2, sticky=tk.W, padx=2, pady=2)



#Medyan Filtrenin Yeri
medyanFiltreSatir = ttk.Entry(root)
medyanFiltreSatir.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
medyanFiltreSatir.insert(tk.END,'1')



medyanFiltreButon = ttk.Button(root,text='Hesapla',command=medianFilter)
medyanFiltreButon.grid(column=6,row=2,sticky=tk.W, padx=2, pady=2)










#Yazının Yeri
dorduncuSira = ttk.Label(root, text="BiLeteral Filtre Boyutu")
dorduncuSira.grid(column=0, row=3, sticky=tk.W, padx=2, pady=2)



#BiLeteral Kernelin Yeri
biLeteralSatir = ttk.Entry(root)
biLeteralSatir.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
biLeteralSatir.insert(tk.END,'1')




biLeteralSigmaRenkLabel = ttk.Label(root, text="Sigma Renk")
biLeteralSigmaRenkLabel.grid(column=2, row=3, sticky=tk.E, padx=1, pady=1)

biLeteralSigmaRenk = ttk.Entry(root)
biLeteralSigmaRenk.grid(column=3, row=3, sticky=tk.W, padx=5, pady=5)
biLeteralSigmaRenk.insert(tk.END,'35')


biLeteralSigmaUzayLabel = ttk.Label(root, text="Sigma Uzay")
biLeteralSigmaUzayLabel.grid(column=2, row=4, sticky=tk.E, padx=1, pady=1)

biLeteralSigmaUzay = ttk.Entry(root)
biLeteralSigmaUzay.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)
biLeteralSigmaUzay.insert(tk.END,'35')


biLeteralButon = ttk.Button(root,text='Hesapla',command=bileteralFilter)
biLeteralButon.grid(column=6,row=4,sticky=tk.W, padx=2, pady=2)


fotografSecButon = ttk.Button(root,text='Fotograf Seç',command=fotografSec)
fotografSecButon.grid(column=0,row=6)


root.mainloop()