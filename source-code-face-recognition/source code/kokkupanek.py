#jaani gui2ver

import tkinter as tk
import customtkinter
from tkinter import filedialog
from PIL import Image
import cv2
import face_recognition
from simple_facerec import SimpleFacerec

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
 

 #Akna seadistamine   
app= customtkinter.CTk()
app.geometry("720x520")
app.title("Näotuvastus")



#tekst esimeses aknas
font= customtkinter.CTkFont("Comic Sans MS", 70)
font2= customtkinter.CTkFont("Calibri", 40)
font3= customtkinter.CTkFont("Calibri", 25)

pealkiri_1= customtkinter.CTkLabel(app, text="Tuvasta inimene", height=100,font=font)
pealkiri_1.pack(padx=10, pady= 10)

path = ""
x = ""

#NUPUD ESIMESES AKNAS
#piltide üles laadimine

def üleslaadimine():
    filename = filedialog.askopenfilename()
    global path
    path= filename
    print('Valitud:', filename)

def upload_command():
    üleslaadimine()
    pildi_tekitamine(path)


def pildi_funkt():
    tekst= customtkinter.CTkLabel(app, text=f"{info}", font=font3)
    tekst.pack(pady=3)
#pildi_kast= customtkinter.CTkImage()

#järgmisele lehele minek
def kustuta(järjend):
    for i in järjend:
        i.destroy()
    #pilt_nupp.pack()
    

#face_recognition osa
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("source-code-face-recognition/source code/images")

def määrame_isikut(kujutis):
    print(kujutis)
    img = cv2.imread(kujutis)
    face_locations, face_names = sfr.detect_known_faces(img)
    nimi = face_names[0] #idexiga 0 on ära tuntud pildi nimi
    return nimi 

#siia funktsiooni sisse kirja sõnastik, mis võtab pildid (nende pealkirjas vütmetena) ja tagastab 2 lauseleise descriptioni nende kohta

def pildi_tekitamine(tee):
    my_image = customtkinter.CTkImage(light_image=Image.open(tee),
                                  dark_image=Image.open(tee),
                                  size=(430, 250))
    return my_image


def pildi_nupu_tekitamine(pilt):
    global pilt_nupp
    pilt_nupp = customtkinter.CTkButton(app, image=pilt, text="",
                                          command=pildi_funkt)
    # pilt_nupp.grid(row=0, column=0, padx=20, pady=20, sticky= "ew")
    # pilt_nupp.grid_columnconfigure(0, weight=1)
    # pilt_nupp.grid_rowconfigure(0, weight=1)
    pilt_nupp.pack()
    
    
# def pildi_nupu_tekitamine(my_image):
#     pilt_nupp = customtkinter.CTkLabel(app, image=my_image)
#     pilt_nupp.pack()

#Kõik mida edasi nupp käivitab
def edasi_nupp_funktsioonid():
    global nimi
    global x
    x= määrame_isikut(path)
    kustuta([edasi_nupp, upload_button, pealkiri_1])
    my_image= pildi_tekitamine(path)
    pildi_nupu_tekitamine(my_image)
    #pilt_nupp.pack()
    nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)
    nimi.pack(pady=5)
    jätka.pack(pady=40)
    
def jätka_nupp_funktsioonid():
    üleslaadimine()
    #kustuta([pilt_nupp, nimi])
    my_image= pildi_tekitamine(path)
    pildi_nupu_tekitamine(my_image)
    nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)
    nimi.pack(pady=5)
    jätka.pack(pady=40)


#path = r"C:\Users\krull\Desktop\Media\Photoshop\valter.png"


#NUPUD ESIMESE AKNAS
upload_button = customtkinter.CTkButton(app, text='Lae üles inimese pilt',
                                        font= font2, command= upload_command,
                                        height=100, width=600)
upload_button.pack(pady=20)

edasi_nupp= customtkinter.CTkButton(app, text="Edasi", height=30, width=100, 
                                    command=edasi_nupp_funktsioonid)
edasi_nupp.pack()

#Inimese nimi ja info

info= "on väsinud"

#Nupud teises aknas
    #jätkamis nupp
jätka= customtkinter.CTkButton(app, text='Vali uus pilt',
                                        font= font3, command=jätka_nupp_funktsioonid,
                                        height=40, width=125)




#run gui
app.mainloop()