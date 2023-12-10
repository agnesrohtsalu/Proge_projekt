import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter
import face_recognition

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# List of descriptions
descriptions = {
    "Agnes": "Description for Agnes.",
    "Obama": "USA ikooniline presindent",
    # Add more entries as needed
}

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Näotuvastus")

font = customtkinter.CTkFont("Comic Sans MS", 70)
font2 = customtkinter.CTkFont("Calibri", 40)
font3 = customtkinter.CTkFont("Calibri", 25)

pealkiri_1 = customtkinter.CTkLabel(app, text="Tuvasta inimene", height=100, font=font)
pealkiri_1.pack(padx=10, pady=10)


def üleslaadimine():
    filename = filedialog.askopenfilename()
    print('Valitud:', filename)
    tuvasta_isik(filename)


def tuvasta_isik(pildi_tee):
    known_image = face_recognition.load_image_file("/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama.jpg")
    unknown_image = face_recognition.load_image_file(pildi_tee)

    try:
        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        if results[0]:
            kustuta([edasi_nupp, upload_button, pealkiri_1])
            nimi.pack(pady=5)
            pildi_funkt(pildi_tee)
        else:
            print("Isikut ei tuvastatud")

    except IndexError:
        print("Nägu ei leitud pildilt")


def kustuta(järjend):
    for i in järjend:
        i.destroy()
    pilt_nupp.pack()
    nimi.pack(pady=5)


upload_button = customtkinter.CTkButton(app, text='Lae üles inimese pilt',
                                        font=font2, command=üleslaadimine,
                                        height=100, width=600)
upload_button.pack(pady=20)


x = "Agnes"
info = "on väsinud"
nimi = customtkinter.CTkLabel(app, text=f"{x}", font=font2)


def pildi_funkt(pildi_tee):
    # Get the person's name from the file path
    person_name = pildi_tee.split("/")[-1].split(".")[0]
    
    # Display the description if available, otherwise a default message
    description = descriptions.get(person_name, "No description available.")
    
    tekst = customtkinter.CTkLabel(app, text=description, font=font3)
    tekst.pack(pady=3)


my_image = customtkinter.CTkImage(light_image=Image.open(r"/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama.jpg"),
                                  size=(530, 350))

pilt_nupp = customtkinter.CTkButton(app, image=my_image, text="", command=lambda: (pildi_funkt("/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama.jpg")))

edasi_nupp = customtkinter.CTkButton(app, text="Edasi", height=30, width=100,
                                     command=lambda: (kustuta([edasi_nupp, upload_button, pealkiri_1])),
                                     )
edasi_nupp.pack()

app.mainloop()
