import tkinter as tk
import customtkinter
from tkinter import filedialog
from PIL import Image

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

#tekst esimeses aknas
font= customtkinter.CTkFont("Calibri", 70)
font2= customtkinter.CTkFont("Calibri", 40)
font3= customtkinter.CTkFont("Calibri", 20)

pealkiri_1= customtkinter.CTkLabel(app, text="Tuvasta inimene", height=100,font=font)
pealkiri_1.grid(row=0, column=0)

#Inimese nimi ja info
x="Agnes"
info= "Elukoht: Tartu \nVanus: 21 \nEriala: FKM"

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

#info välja kirjutamine
info_tekst= customtkinter.CTkLabel(app, text="", font=font3, justify= "left")
def pildi_funkt():
    #global info_tekst
    #info_tekst= customtkinter.CTkLabel(app, text=f"{info}", font=font3)
    info_tekst.configure(text=f"{info}")
    info_tekst.grid(row= 2, column=0, sticky= "nw", padx= 50)

#järgmisele lehele minek
def kustuta(järjend):
    for i in järjend:
        i.destroy()
    #pilt_nupp.pack()
    


def pildi_tekitamine(tee):
    my_image = customtkinter.CTkImage(light_image=Image.open(tee),
                                  dark_image=Image.open(tee),
                                  size=(430, 250))
    return my_image


def pildi_nupu_tekitamine(pilt):
    global pilt_nupp
    pilt_nupp = customtkinter.CTkButton(app, image=pilt, text="", fg_color="black",
                                          command=pildi_funkt)
    pilt_nupp.grid(row=0, column= 0, sticky= "n")
    

#Kõik mida edasi nupp käivitab
def edasi_nupp_funktsioonid():
    global nimi
    kustuta([edasi_nupp, upload_button, pealkiri_1])
    my_image= pildi_tekitamine(path)
    pildi_nupu_tekitamine(my_image)
    #pilt_nupp.pack()
    nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)
    nimi.grid(row=1, column=0, sticky= "n")
    jätka.grid(row=3, column=0)

#"Vali uus pilt" nupp
 
def jätka_nupp_funktsioonid():
    global nimi
    global info_tekst
    üleslaadimine()
    andmete_muutmine()
    kustuta([pilt_nupp, nimi, info_tekst])
    my_image= pildi_tekitamine(path)
    pildi_nupu_tekitamine(my_image)
    nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)
    nimi.grid(row=1, column=0, sticky= "n")
    jätka.grid(row=3, column=0)

#NIME ja INFO muutujate muutmine
def andmete_muutmine():
    global x
    global info



path = r"C:\Users\krull\Desktop\Media\Photoshop\valter.png"


#NUPUD ESIMESE AKNAS
upload_button = customtkinter.CTkButton(app, text='Lae üles inimese pilt',
                                        font= font2, command= upload_command,
                                        height=100, width=600)
upload_button.grid(row=1, column=0, rowspan= 2)

edasi_nupp= customtkinter.CTkButton(app, fg_color= "#008000", text="Edasi", height=30, width=100, 
                                    command=edasi_nupp_funktsioonid)
edasi_nupp.grid(row=3, column=0)


#Nupud teises aknas
    #jätkamis nupp
jätka= customtkinter.CTkButton(app, text='Vali uus pilt',
                                        font= font3, command=jätka_nupp_funktsioonid,
                                        height=40, width=125)



#run gui
app.mainloop()
