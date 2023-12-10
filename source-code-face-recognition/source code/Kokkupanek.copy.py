#vana kasutajaliidesega töötav versioon

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

#GRID
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=10)
app.rowconfigure(3, weight=5)
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

#tekst esimeses aknas
font= customtkinter.CTkFont("Calibri", 70)
font2= customtkinter.CTkFont("Calibri", 40)
font3= customtkinter.CTkFont("Calibri", 25)

pealkiri_1= customtkinter.CTkLabel(app, text="Tuvasta inimene", height=100,font=font)
pealkiri_1.grid(row=0, column=0, columnspan=2)

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

#järgmisele lehele minek
def kustuta(järjend):
    for i in järjend:
        i.destroy()
    

#face_recognition osa
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("source-code-face-recognition/source code/images")

täisnimi = ""

def määrame_isikut(path):
    global täisnimi
    global inimeste_sõnastik
    kujutis = any 
    img = cv2.imread(path)
    face_locations, face_names = sfr.detect_known_faces(img)
    täisnimi = face_names[0] #idexiga 0 on ära tuntud pildi nimi
    #siia funktsiooni sisse kirja sõnastik, mis võtab pildid (nende pealkirjas vütmetena) ja tagastab 2 lauseleise descriptioni nende kohta
# Define a dictionary to store information about people
    inimeste_sõnastik = {
    "Jaan Janno": "Praktikumi juhendaja",
    "Agnes Rohtsalu": "Materjaliteadus + kõrvaleriala",
    "Jaan Krull": "Materjaliteadus",
    "Tauno Palts": "Vastutav õppejõud aines"
}
    return täisnimi 

def pildi_funkt():
    global täisnimi
    global tekst
    täisnimi = str(täisnimi)
    tekst= customtkinter.CTkLabel(app, text=f"{inimeste_sõnastik[täisnimi]}", font=font3)
    tekst.grid(row= 2, column=0, sticky= "nw", padx= 50, columnspan=2)


def pildi_tekitamine(tee):
    my_image = customtkinter.CTkImage(light_image=Image.open(tee),
                                  dark_image=Image.open(tee),
                                  size=(430, 250))
    return my_image


def pildi_nupu_tekitamine(pilt):
    global pilt_nupp
    pilt_nupp = customtkinter.CTkButton(app, image=pilt, text="", fg_color="black",
                                          command=pildi_funkt)
    # pilt_nupp.grid(row=0, column=0, padx=20, pady=20, sticky= "ew")
    # pilt_nupp.grid_columnconfigure(0, weight=1)
    # pilt_nupp.grid_rowconfigure(0, weight=1)
    pilt_nupp.grid(row=0, column= 0, sticky= "n", columnspan=2)
    
def live_nupp():
     live_nupp= customtkinter.CTkButton(app, text='Live',
                                        font= font3, 
                                        command = popup,
                                        fg_color="red")
     live_nupp.grid(row=0, column= 1, sticky= "ne")
     
def popup():
        
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("source-code-face-recognition/source code/images")

    # Load Camera
    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names): #nimed mida kuvatakse võetakse pildi pealkirjast
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2) #teksti värv on must ja teksti paksus on 2 pikslit
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4) 

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    
#Kõik mida edasi nupp käivitab
def edasi_nupp_funktsioonid():
    global nimi
    global x
    x= määrame_isikut(path)
    live_nupp()
    kustuta([edasi_nupp, upload_button, pealkiri_1])
    my_image= pildi_tekitamine(path)
    pildi_nupu_tekitamine(my_image)
    #pilt_nupp.pack()
    nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2) #valge kirjutis jaani poolt
    nimi.grid(row=1, column=0, sticky= "n", columnspan=2)
    jätka.grid(row=3, column=0, columnspan=2)
    
#UUE PILDI NUPP
def jätka_nupp_funktsioonid():
    global nimi
    üleslaadimine()
    live_nupp()
    x = määrame_isikut(path)
    #muuda_teksti()
    kustuta([pilt_nupp,tekst, nimi])
    my_image= pildi_tekitamine(path)
    pildi_nupu_tekitamine(my_image)
    nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)
    nimi.grid(row=1, column=0, sticky= "n", columnspan=2)
    jätka.grid(row=3, column=0, columnspan=2)



#NUPUD ESIMESE AKNAS
upload_button = customtkinter.CTkButton(app, text='Lae üles inimese pilt',
                                        font= font2, command= upload_command,
                                        height=100, width=600)
upload_button.grid(row=1, column=0, rowspan= 2, columnspan=2)

edasi_nupp= customtkinter.CTkButton(app, text="Edasi", fg_color="#008000", height=30, width=100, 
                                    command=edasi_nupp_funktsioonid)
edasi_nupp.grid(row=3, column=0, columnspan=2)

#Nupud teises aknas
    #jätkamis nupp
jätka= customtkinter.CTkButton(app, text='Vali uus pilt',
                                        font= font3, command=jätka_nupp_funktsioonid,
                                        height=40, width=125)


#run gui
app.mainloop()