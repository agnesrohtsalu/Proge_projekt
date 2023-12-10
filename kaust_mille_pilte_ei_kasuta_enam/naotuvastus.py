import dlib
import face_recognition
import cv2
import tkinter as tk
import customtkinter 
from tkinter import filedialog
from PIL import Image

customtkinter.set_appearance_mode("dark")
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


    #Inimese nimi
x="Agnes"
info= "on väsinud"
nimi= customtkinter.CTkLabel(app, text=f"{x}", font=font2)

def pildi_funkt():
    tekst= customtkinter.CTkLabel(app, text=f"{info}", font=font3)
    tekst.pack(pady=3)


#pildi_kast= customtkinter.CTkImage()
my_image = customtkinter.CTkImage(light_image=Image.open(r"/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama.jpg"),
                                  size=(530, 350))

pilt_nupp = customtkinter.CTkButton(app, image=my_image, text="",  command=lambda:(pildi_funkt()))


edasi_nupp= customtkinter.CTkButton(app, text="Edasi", height=30, width=100, 
                                    command=lambda:(kustuta([edasi_nupp, upload_button, pealkiri_1])),
                                    )
edasi_nupp.pack()



#run gui
app.mainloop()

#algab agnese kood, mis pildilt kus on 2 naist annab ühe naise näo koos selle koordinaatidega"
image = face_recognition.load_image_file("/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    cv2.imshow("nagu", face_image)
cv2.waitKey(0)
#näotuvastuskood lõppeb 

cv2.destroyAllWindows() 