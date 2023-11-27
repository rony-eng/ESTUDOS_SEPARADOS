import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de Login")
janela.iconbitmap("") #coloca um icone de sua preferencia, com a extenção .ico
janela.resizable(False, False)

#trabalhanndo com a imagem da tela
img = PhotoImage(file="ftlogin.jpg") #colocar uma imagem
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de login", text_font=("Roboto"))
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="")

janela.mainloop()