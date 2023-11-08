import tkinter as tk
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#raam
app= customtkinter.CTk()
app.geometry("720x480")
app.title("Näotuvastus")

pealkiri_1= customtkinter.CTkLabel(app, text="Sisesta pilt: ")
pealkiri_1.pack(padx=10, pady= 10)

#faili sisestus
pildi_sisestus_kast= customtkinter.CTkEntry(app, width=100, height=50)
pildi_sisestus_kast.pack()

#run gui
app.mainloop()