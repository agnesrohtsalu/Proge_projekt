import tkinter as tk
import customtkinter
from tkinter import filedialog
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
 

#def kuva_leht(leht):
#    for i in lehed:
 #       if i.winfo_ismapped():
  #          i.wm_forget()
   # leht.pack()
def peida_esimesed_nupud(nupud):
    for nupp in nupud:
        nupp.wm_forget()
    
app= customtkinter.CTk()
app.geometry("720x480")
app.title("Näotuvastus")

#kiht2 = CTkToplevel(app)
#leht2= customtkinter.CTkFrame(master=kiht2 , width=720, height=480,)
#leht2.geometry("720x480")
#leht2.title("Isik tuvastatud")

#lehed=[app, leht2]

#tekst esimeses aknas
font= customtkinter.CTkFont("Comic Sans MS", 70)
font2= customtkinter.CTkFont("Calibri", 40)
font3= customtkinter.CTkFont("Calibri", 25)

pealkiri_1= customtkinter.CTkLabel(app, text="Tuvasta inimene", height=100,font=font)
pealkiri_1.pack(padx=10, pady= 10)



#NUPUD ESIMESES AKNAS
#piltide üles laadimine
def üleslaadimine():
    filename = filedialog.askopenfilename()
    print('Valitud:', filename)


upload_button = customtkinter.CTkButton(app, text='Lae üles inimese pilt',
                                        font= font2, command=üleslaadimine,
                                        height=100, width=600)
upload_button.pack(pady=20)

#järgmisele lehele minek
def kustuta(järjend):
    for i in järjend:
        i.destroy()
    pilt_nupp.pack()
    nimi.pack(pady=5)

#Nupud teises aknas??
    #jätkamis nupp
jätka= customtkinter.CTkButton(app, text='Vali uus pilt',
                                        font= font3, command=üleslaadimine,
                                        height=30, width=120)
jätka.pack()

    #Inimese nimi
x="Agnes"
info= "on väsinud"
nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)

def pildi_funkt():
    tekst= customtkinter.CTkLabel(app, text=f"{info}", font=font3)
    tekst.pack(pady=3)



#pildi_kast= customtkinter.CTkImage()
my_image = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\krull\Desktop\Media\Photoshop\valter.png"),
                                  dark_image=Image.open(r"C:\Users\krull\Desktop\Media\Photoshop\valter.png"),
                                  size=(530, 350))

pilt_nupp = customtkinter.CTkButton(app, image=my_image, text="",  command=lambda:(pildi_funkt()))


edasi_nupp= customtkinter.CTkButton(app, text="Edasi", height=30, width=100, 
                                    command=lambda:(kustuta([edasi_nupp, upload_button, pealkiri_1])),
                                    )
edasi_nupp.pack()



#run gui
app.mainloop()
