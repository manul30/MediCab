from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
class Control_de_molestias():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("750x350")
        self.molestias=[]
        #-----------------------------------------------------------
        #Imagenes
        img1 = ImageTk.PhotoImage(Image.open("musculos_final_2.png"))
        self.panel1 = Label(self.root, image=img1)
        self.panel1.place(x=50, y=5)
        img2 = ImageTk.PhotoImage(Image.open("musculos_final_3.png"))
        self.panel2 = Label(self.root, image=img2)
        self.panel2.place(x=300, y=5)
        img3 = ImageTk.PhotoImage(Image.open("musculos_final_1.png"))
        self.panel3 = Label(self.root, image=img3)
        self.panel3.place(x=550, y=15)
        #---------------------------------------------------------------
        #Botones
        #---------------------------------------------------------------
        #Primera_imagen
        self.Boca = Button(self.root,width=4,height=1, text="Boca", font=("Raleway",8), bg="White", fg="black", command=self.cambiar_color_Boca)
        self.Boca.place(x=50, y=10)
        self.Ojos= Button(self.root, width=4, height=1, text="Ojos", font=("Raleway", 8), bg="White", fg="black",command=self.cambiar_color_Ojos)
        self.Ojos.place(x=180, y=10)
        self.Pecho = Button(self.root, width=4, height=1, text="Pecho", font=("Raleway", 8), bg="White", fg="black",
                           command=self.cambiar_color_Pecho)
        self.Pecho.place(x=200, y=85)
        self.Muñeca = Button(self.root, width=5, height=1, text="Muñeca", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Muñeca)
        self.Muñeca.place(x=20, y=160)
        self.Palma = Button(self.root, width=4, height=1, text="Palma", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Palma)
        self.Palma.place(x=50, y=230)
        self.Estomago = Button(self.root, width=7, height=1, text="Estomago", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Estomago)
        self.Estomago.place(x=200, y=130)
        self.Pulgar = Button(self.root, width=7, height=1, text="Pulgar", font=("Raleway", 8), bg="White",
                               fg="black",
                               command=self.cambiar_color_Pulgar)
        self.Pulgar.place(x=220, y=193)
        self.Dedo = Button(self.root, width=7, height=1, text="Dedo", font=("Raleway", 8), bg="White",
                             fg="black",
                             command=self.cambiar_color_Dedo)
        self.Dedo.place(x=180, y=220)
        self.Rodilla = Button(self.root, width=7, height=1, text="Rodilla", font=("Raleway", 8), bg="White",
                             fg="black",
                             command=self.cambiar_color_Rodilla)
        self.Rodilla.place(x=200, y=270)
        #Segunda imagen
        self.Oreja = Button(self.root, width=4, height=1, text="Oreja", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Oreja)
        self.Oreja.place(x=410, y=23)
        self.Cuello = Button(self.root, width=4, height=1, text="Cuello", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Cuello)
        self.Cuello.place(x=409, y=50)
        self.Hombro = Button(self.root, width=5, height=1, text="Hombro", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Hombro)
        self.Hombro.place(x=440, y=80)
        self.Codo = Button(self.root, width=5, height=1, text="Codo", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Codo)
        self.Codo.place(x=440, y=125)
        self.Nalga = Button(self.root, width=5, height=1, text="Nalga", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Nalga)
        self.Nalga.place(x=435, y=170)
        self.Talon= Button(self.root, width=5, height=1, text="Talon", font=("Raleway", 8), bg="White", fg="black",
                           command=self.cambiar_color_Talon)
        self.Talon.place(x=400, y=315)
        #Imagen Tres
        self.Frente = Button(self.root, width=4, height=1, text="Frente", font=("Raleway", 8), bg="White", fg="black",
                          command=self.cambiar_color_Frente)
        self.Frente.place(x=660, y=23)
        self.Nariz = Button(self.root, width=4, height=1, text="Nariz", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Nariz)
        self.Nariz.place(x=650, y=60)
        self.Cadera = Button(self.root, width=5, height=1, text="Cadera", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Cadera)
        self.Cadera.place(x=665, y=150)
        self.Antebrazo = Button(self.root, width=8, height=1, text="Antebrazo", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Antebrazo)
        self.Antebrazo.place(x=500, y=150)
        self.Muslo = Button(self.root, width=8, height=1, text="Muslo", font=("Raleway", 8), bg="White",
                                fg="black",
                                command=self.cambiar_color_Muslo)
        self.Muslo.place(x=520, y=220)
        self.Canilla = Button(self.root, width=8, height=1, text="Canilla", font=("Raleway", 8), bg="White",
                            fg="black",
                            command=self.cambiar_color_Canilla)
        self.Canilla.place(x=520, y=290)
        self.Tobillo = Button(self.root, width=8, height=1, text="Tobillo", font=("Raleway", 8), bg="White",
                              fg="black",
                              command=self.cambiar_color_Tobillo)
        self.Tobillo.place(x=520, y=320)
        self.root.mainloop()
        
        print(self.molestias)
    #---------------------------------------------------------------------
    #Funciones da cambiar el color
    def cambiar_color_Boca(self):
            self.Boca.configure(bg="Yellow")
            self.molestias.append("Boca")
    def cambiar_color_Ojos(self):
        self.Ojos.configure(bg="#32CD32")
        self.molestias.append("Ojos")
    def cambiar_color_Pecho(self):
        self.Pecho.configure(bg="#00FFFF")
        self.molestias.append("Pecho")
    def cambiar_color_Estomago(self):
        self.Estomago.configure(bg="Red")
        self.molestias.append("Estomago")
    def cambiar_color_Muñeca(self):
        self.Muñeca.configure(bg="#FF00FF")
        self.molestias.append("Estomago")
    def cambiar_color_Palma(self):
        self.Palma.configure(bg="Blue")
        self.molestias.append("Palma")
    def cambiar_color_Pulgar(self):
        self.Pulgar.configure(bg="Yellow")
        self.molestias.append("Pulgar")
    def cambiar_color_Dedo(self):
        self.Dedo.configure(bg="#32CD32")
        self.molestias.append("Dedo")
    def cambiar_color_Rodilla(self):
        self.Rodilla.configure(bg="#FF00FF")
        self.molestias.append("Rodilla")
    def cambiar_color_Oreja(self):
        self.Oreja.configure(bg="#00FFFF")
        self.molestias.append("Oreja")
    def cambiar_color_Cuello(self):
        self.Cuello.configure(bg="Blue")
        self.molestias.append("Cuella")
    def cambiar_color_Hombro(self):
        self.Hombro.configure(bg="#32CD32")
        self.molestias.append("Hombro")
    def cambiar_color_Codo(self):
        self.Codo.configure(bg="#FF00FF")
        self.molestias.append("Codo")
    def cambiar_color_Nalga(self):
        self.Nalga.configure(bg="Red")
        self.molestias.append("Nalga")
    def cambiar_color_Talon(self):
        self.Talon.configure(bg="Yellow")
        self.molestias.append("Talon")
    def cambiar_color_Frente(self):
        self.Frente.configure(bg="#FF00FF")
        self.molestias.append("Frente")
    def cambiar_color_Nariz(self):
        self.Nariz.configure(bg="Red")
        self.molestias.append("Nariz")
    def cambiar_color_Antebrazo(self):
        self.Antebrazo.configure(bg="#00FFFF")
        self.molestias.append("Antebrazo")
    def cambiar_color_Cadera(self):
        self.Cadera.configure(bg="Yellow")
        self.molestias.append("Cadera")
    def cambiar_color_Muslo(self):
        self.Muslo.configure(bg="Blue")
        self.molestias.append("Muslo")
    def cambiar_color_Canilla(self):
        self.Canilla.configure(bg="#32CD32")
        self.molestias.append("Canilla")
    def cambiar_color_Tobillo(self):
        self.Tobillo.configure(bg="Red")
        self.molestias.append("Tobillo")
app=Control_de_molestias()


