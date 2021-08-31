# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:04:15 2021

@author: Manuel
"""
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from fpdf import FPDF
from scipy.io import loadmat
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import cv2.data.haarcascades

#Pandas para leer el csv

class PDF(FPDF):
    pass
    def logo(self, name,x,y,w,h):
        self.image(name,x,y,w,h)
    
    def text(self,name):
        with open(name,'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)
        self.set_text_color(76.0,32.0,250.0)
        self.set_font('Arial','',12)
        self.multi_cell(0,10,txt)
        
    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_text_color(2020,50,50)
        self.set_font('Arial','B',16)
        self.cell(w=210.0,h=40.0 ,align='C', txt=title, border=0)
    
class INTERFAZ(tk.Tk):   #Interfaz principal
    def __init__(self,*args,**kwargs):  #Constructor
        super().__init__(*args,**kwargs)   #Heredando de Tk()

        self.title("INTERFAZ CABINEITOR")    #Titulo y dimension de ventana
        self.geometry("1000x600")
        self.Apellido=""                      #Variables de usuario para acceder desde cualquier frame hija
        self.Nombre=""
        self.Correo=""
        self.Contrasena=""
        self.Edad=0
        self.Sexo=""
        self.Altura=0
        self.Temperatura=0
        self.Estatura=0
        self.Peso=0
        self.PR=0
        self.Ox=0
        self.Cita=""
        self.Especialidad=""
        self.Medico=""
        self.Fecha=""
        self.Sede=""
        
        self.pantalla = tk.Frame()            #Frame principal
        self.pantalla.grid(sticky = "nsew")

        self.todos_los_frames = dict()         #Diccionario de los Frames(clases hijas) a usar
        
        #Creacion de los frames hijos
        # ---------------------------------------------------------------------------------------------
        self.todos_los_frames['Foto'] = Foto(container=self.pantalla, controller=self)
        self.todos_los_frames['Foto'].grid(row=0, column=0, sticky='nsew')
        self.todos_los_frames['Inicio'] = Inicio(container=self.pantalla, controller=self)
        self.todos_los_frames['Inicio'].grid(row=0, column=0, sticky='nsew')
        # -----------------------------------------------------------------------------------------------------
        self.todos_los_frames['Bienvenida'] = Bienvenida(container = self.pantalla, controller = self)
        self.todos_los_frames['Mario'] = Mario(container = self.pantalla, controller = self)
        #self.todos_los_frames['Inicio'] = Inicio(container = pantalla, controller = self)
        self.todos_los_frames['Ayuda'] = Ayuda(container = self.pantalla, controller = self)
        self.todos_los_frames['Citas'] = Citas(container = self.pantalla, controller = self)
        self.todos_los_frames['Seguro'] = Seguro(container = self.pantalla, controller = self)
        self.todos_los_frames['ACitas'] = ACitas(container = self.pantalla, controller = self)
        self.todos_los_frames['Historial'] = Historial(container = self.pantalla, controller = self)
        self.todos_los_frames['Control'] = Control(container = self.pantalla, controller = self)
        #-------------------------------------------------------------------------------------
        self.todos_los_frames['ControlAltura'] = ControlAltura(container=self.pantalla, controller=self)
        self.todos_los_frames['ControlAltura'].grid(row=0, column=0, sticky='nsew')
        self.todos_los_frames['ControlPeso'] = ControlPeso(container=self.pantalla, controller=self)
        self.todos_los_frames['ControlPeso'].grid(row=0, column=0, sticky='nsew')
        self.todos_los_frames['ControlTemperatura'] = ControlTemperatura(container=self.pantalla, controller=self)
        self.todos_los_frames['ControlTemperatura'].grid(row=0, column=0, sticky='nsew')
        self.todos_los_frames['Control_Oximetro'] = Control_Oximetro(container=self.pantalla, controller=self)
        self.todos_los_frames['Control_Oximetro'].grid(row=0, column=0, sticky='nsew')
        self.todos_los_frames['ControlMolestias'] = ControlMolestias(container=self.pantalla, controller=self)
        self.todos_los_frames['ControlMolestias'].grid(row=0, column=0, sticky='nsew')
        #----------------------------------------------------------------------------------
        self.todos_los_frames['Bienvenida'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['Mario'].grid(row = 0, column = 0, sticky = 'nsew')
        #self.todos_los_frames['Inicio'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['Ayuda'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['Citas'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['Seguro'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['ACitas'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['Historial'].grid(row = 0, column = 0, sticky = 'nsew')
        self.todos_los_frames['Control'].grid(row = 0, column = 0, sticky = 'nsew')
        self.show_frame('Bienvenida')                  #Mostrar en primer plano el primer frame hijo
        
        
    def show_frame(self,contenedor_llamado):            #Método para mostrar en primer plano cualquier frame hijo

        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise() 
    
    def mandar(self,mensaje):
    
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
    
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        s.starttls()
        mail = "cabineitor.informa@gmail.com"
        passw = "cabineitor@123"
        toaddr = self.Correo
        cc = ""
    
        s.login(mail, passw)
        plantilla_inicio = """\
        <html>
           <body>
             Hola estimado(a) usuario(a) \n Se le hace envío de las constancia de cita y/o reporte de salud
           </body>
        </html>
        """
        msg = MIMEMultipart()
    
        msg['From'] = mail
    
        msg['To'] = toaddr
        if cc != "":
            msg['CC'] = cc
    
        msg['Subject'] = mensaje
        msg.attach(MIMEText(plantilla_inicio, 'html'))
        #-----------------------------------------------------
        path = "./prueba.pdf"
        attachment = open(path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        p.add_header('Content-Disposition', "attachment; filename=Reporte "+self.Nombre+self.Apellido+".pdf")
        encoders.encode_base64(p)
        msg.attach(p)
        s.send_message(msg)
        s.quit()

    def reporte_salud(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.image('CABINEITOR.png',-5,-10,60,60)
        pdf.image('pacifico.png',145,5,55,20)
        pdf.set_font('Times', 'B',20)
        pdf.set_fill_color(0, 0, 255)
        pdf.cell(190,30,"",0,1)
        pdf.cell(190, 10, "REPORTE DE CONTROL DE SALUD",0, 10,"C")

        pdf.set_font('Times','',12)
        pdf.cell(180,20,"Fecha: "+str(datetime.now()).split()[0],0,10,"C")
        pdf.cell(100, 10, "Paciente: "+self.Nombre+" "+self.Apellido, 1, 0)
        pdf.cell(40, 10, "Sexo: "+self.Sexo, 1, 0)
        pdf.cell(45, 10, "Edad: "+str(int(self.Edad)), 1, 1)
        pdf.cell(62,10,"Estatura (cm): "+str(self.Estatura),1,0)
        pdf.cell(61,10,"Peso (kg): "+str(self.Peso),1,0)
        pdf.cell(62,10,"Temperatura (°C): "+str(self.Temperatura),1,1)
        pdf.cell(92,10,"Frecuencia de pulso: "+str(self.PR),1,0)
        pdf.cell(93,10,"Nivel de oxígeno en la sangre (%): "+str(self.Ox),1,1)
        pdf.output('prueba.pdf','F')
        self.mandar("Reporte de Salud")
        
    def cons_cita(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.image('CABINEITOR.png',-5,-10,60,60)
        pdf.image('pacifico.png',145,5,55,20)
        pdf.set_font('Times', 'B',20)
        pdf.set_fill_color(0, 0, 255)
        pdf.cell(190,30,"",0,1)
        pdf.cell(190, 10, "CONSTANCIA DE RESERVA DE CITA",0, 10,"C")

        pdf.set_font('Times','',12)
        pdf.cell(180,20,"Fecha de emisión: "+str(datetime.now()).split()[0],0,10,"C")
        pdf.cell(100, 20, "Paciente: "+self.Nombre+" "+self.Apellido, 0, 1)
        pdf.cell(40, 20, "Sexo: "+self.Sexo, 0, 1)
        pdf.cell(45, 20, "Edad: "+str(int(self.Edad)), 0, 1)
        pdf.cell(62,20,"Especialidad: "+self.Especialidad,0,1)
        pdf.cell(61,20,"Medico(a): "+self.Medico,0,1)
        pdf.cell(62,20,"Sede: "+self.Sede,0,1)
        pdf.cell(180,20,"Dirección: "+list(Cita.iloc[list(Cita['Sede']==self.Sede)]['Dir'])[0],0,1)
        pdf.cell(62,40,"Fecha de consulta / cita: "+self.Fecha,0,1)
        
        pdf.set_font('Times', 'B',20)
        pdf.cell(180,20,"GRACIAS POR SU PREFERENCIA",0,1,"C")
        
        pdf.output('prueba.pdf','F')
        self.mandar("Contancia de Reseva de Cita")   
        
class Bienvenida(tk.Frame):      #Primera clase de frame

    def __init__(self, container, controller,*args, **kwargs):   #Constructor, se pasa controller como la clase padre, para acceder al método ShowFrame

        super().__init__(container, *args, **kwargs)             #Heredando
        self.config(bg = "gray",width=1000,height=600)

        #logo,sus dimensiones y archivo

        logo_label=tk.Label(self,bg="black")
        logo_label.place(x=500,y=280,anchor="center")
        logo=Image.open("CABINEITOR.png")
        logo=ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label_empezar = tk.Label( self, text = "Toque para empezar ...", font = ("Raleway",12),bg = "white" )
        label_empezar.place(x=500,y=500,anchor="center")
        
        self.bind("<Button-1>",lambda x:controller.show_frame( 'Mario' ))
        logo_label.bind("<Button-1>",lambda x:controller.show_frame( 'Mario' ))
        label_empezar.bind("<Button-1>",lambda x:controller.show_frame('Mario' ))

class Mario(tk.Frame):              # Segunda clase de frame hijo

    def __init__(self, container, controller,*args, **kwargs):   #Constructor, se pasa controller como la clase padre, para acceder al método ShowFrame

        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)           #Dando dimensiones a el frame

        self.controller=controller                             #definiendo el controlador, ya que es usado por el primer frame pero no el segundo
        self.codigo_usuario = tk.StringVar()                   #Entrada de texto de usuario
        #self.codigo_usuario.set("Código de seguro")
        self.contrasena=tk.StringVar()
        #self.contrasena.set("Contraseña")
        
        #fondo, dimensiones, escalas y archivo

        logo_label=tk.Label(self)
        logo_label.place(x=0,y=0)
        logo=Image.open("logueo.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        

        label_DNI = tk.Label( self, text = "Ingrese su código y contraseña del seguro afiliado:", font = ("Raleway",12) )
        label_DNI.place(x=500,y=350,anchor="center")

        self.Esp_Entrada = ttk.Entry( self, textvariable = self.codigo_usuario )            #Ubicacion de label y entrada de texto
        #self.Esp_Entrada.insert(END,"Codigo de seguro")
        self.Esp_Entrada.focus()
        self.Esp_Entrada.place(x=425,y=380)

        self.Esp_Contra = ttk.Entry( self, textvariable = self.contrasena, show="*" )            #Ubicacion de label y entrada de texto
        self.Esp_Contra.place(x=425,y=410)        
    
        label_codigo=tk.Label(self,text="Código: ",font=("Raleway",11))
        label_codigo.place(x=360,y=390,anchor="center")
    
        label_contra=tk.Label(self,text="Contraseña: ",font=("Raleway",11))
        label_contra.place(x=375,y=420,anchor="center")
    
        boton_continuar = ttk.Button( self, text = "CONTINUAR", command =  lambda: [self.verificar,controller.show_frame('Foto')] )   # Boton de continuar
        boton_continuar.place(x=425,y=450)
        boton_continuar.bind( "<Return>",self.verificar)
        
        label_=tk.Label(self,text="Presione para continuar ",font=("Raleway",10))
        label_.place(x=320,y=460,anchor="center")
        
        self.label_adver=tk.Label(self, textvariable="",font=("Raleway",12),fg="red")  # Label de advertencia de error
        self.label_adver.place(x=400,y=470)

    def verificar(self,*args,**kwargs):           # Método para verificar si el usuario está registrado y pasar al inicio

        if self.codigo_usuario.get().isdigit() and sum(Data['Codigo']==int(self.codigo_usuario.get()))>0:
               aux=Data[Data['Codigo']==int(self.codigo_usuario.get())]
               aux=aux.iloc[0]
               if aux['Contraseña']==self.contrasena.get():
                   self.controller.Apellido=aux['Apellido']
                   self.controller.Nombre=aux['Nombre']
                   self.controller.Correo=aux['Correo']
                   self.controller.Contrasena=aux['Contraseña']
                   self.controller.Edad=aux['Edad']
                   self.controller.Sexo=aux['Sexo']
                   self.Esp_Entrada.delete(0,"end")
                   self.Esp_Contra.delete(0,"end")
                   self.controller.todos_los_frames['Inicio'] = Inicio(container = self.controller.pantalla, controller = self.controller)
                   self.controller.todos_los_frames['Inicio'].grid(row=0,column=0,sticky="nsew")
                   self.controller.show_frame('Inicio')
                   self.label_adver.configure(text="")
               else:
                   self.label_adver.configure(text="Ha ocurrido un error, vuelva a ingresar su código")

        else:
            self.label_adver.configure(text="Ha ocurrido un error, vuelva a ingresar su código")

class Inicio(tk.Frame):
     def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller

        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("inicio.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        cerrar_sesion=tk.Button(self, text="Cerrar sesion", font="Raleway", bg="#212121",fg="white")
        cerrar_sesion.place(x=10,y=10)

        cerrar_sesion.bind("<Button-1>",lambda x:controller.show_frame( 'Bienvenida' ))

        self.nombre_label=tk.Label(self, text="Hola, "+ self.controller.Nombre +" "+self.controller.Apellido , font="Raleway", fg="#212121")
        self.nombre_label.place(x=500,y=10)

        self.saludo_label=tk.Label(self, text="Bienvenido a CABINEITOR \n \n ¿Qué deseas hacer?" , font="Raleway", fg="#212121")
        self.saludo_label.place(x=100,y=50)
    
        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
        
        consultar_cita_btn=tk.Button(self,text="Consultar citas",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('Citas'))
        consultar_cita_btn.place(x=800,y=100)
        
        contactar_seguro_btn=tk.Button(self,text="Contacte a su seguro",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('Seguro'))
        contactar_seguro_btn.place(x=800,y=200)

        agende_cita_btn=tk.Button(self,text="Agende una cita",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('ACitas'))
        agende_cita_btn.place(x=800,y=300)

        historial_btn=tk.Button(self,text="Ver historial clínico",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('Historial'))
        historial_btn.place(x=800,y=400)

        control_btn=tk.Button(self,text="Empezar control de salud",font="Raleway",bg="green",fg="black",command=lambda:controller.show_frame('Control'))
        control_btn.place(x=800,y=500)
        
        correo_btn=tk.Button(self,text="Mandar reporte a correo",font="Raleway",bg="cyan",fg="black",command=lambda:controller.reporte_salud())
        correo_btn.place(x=500,y=500)




class Ayuda(tk.Frame):
    
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "gray",width=1000,height=600)

        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label=tk.Label(self,text="Sección de Ayuda",font=("Raleway",16))
        label.place(x=400,y=50)
        
        label2=tk.Label(self,text="Bienvenido a la sección de ayuda. Aquí se presentan las preguntas más frecuentes \n sobre CABINEITOR. Por favor, lea con atención y siga las instrucciones",font=("Raleway",11))
        label2.place(x=200,y=150)
        
        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)

        labelgrande=tk.Label(self,text="¿Qué es CABINEITOR? \n CABINEITOR es un robot creado para tener un control de salud sobre los usuarios con el fin de prevenir diversas enfermedades. \n De esta manera, cuenta con cuatro sensores que miden la temperatura, la altura, peso y el nivel de oxígeno en la sangre. \n Adicionalmente se auto desinfecta y cuenta con el servicio de agendar una cita médica con un doctor. \n \n ¿Cada cuánto tiempo se tendré una cita en CABINEITOR? \n  La programación se da aproximadamente cada semana. Para más información consulté en la interfaz de inicio de CABINEITOR en CONSULTAR CITAS. \n En caso se presentará algún inconveniente para acceder a la información envié un correo cabineitor.informa@gmail.com \n \n ¿Cuál es el tiempo de respuesta cuando agendo una cita médica en CABINEITOR? \n El tiempo de respuesta para agendar una cita médica dependerá únicamente de su seguro. Se aconseja contactar a su seguro para más información. \n \n ¿Qué hago si la información de mí control de salud no llego a mi correo? \n 	En caso se presentará que la información del control de salud no llegará a su correo envié un correo a cabineitor.informa@gmail.com	. \n El equipo de asistencia de CABINEITOR lo atenderá lo más pronto posible. \n \n ¿Qué hacer en caso de emergencia asociado con uno de los sensores? \n CABINEITOR cuenta con un botón rojo de emergencia el cual se encuentra ubicado en la parte inferior izquierda de la pantalla ",font=("Raleway",10))
        labelgrande.place(x=75,y=200)

class Citas(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "gray",width=1000,height=600)
        self.controller=controller

        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label=tk.Label(self,text="Sección de Citas",font=("Raleway",16))
        label.place(x=400,y=50)

        label2=tk.Label(self,text="En este apartado, puede visualizar las siguientes citas programadas en su historial clínico:",font=("Raleway",12))
        label2.place(x=200,y=150)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)

        ayuda_btn=tk.Button(self,text="Agendar nueva cita",font="Raleway",bg="cyan",fg="black",command=lambda:controller.show_frame('ACitas'))
        ayuda_btn.place(x=450,y=300)
        
        if(self.controller.Especialidad != ""):
            ayuda_btn.place(x=1000,y=1000)
            self.label7=tk.Label(self,text="Especialidad : "+self.controller.Especialidad,font=("Raleway",12))
            self.label7.place(x=10,y=200)
            self.label8=tk.Label(self,text="Sede : "+ self.controller.Sede,font=("Raleway",12))
            self.label8.place(x=10,y=230)
            self.label11=tk.Label(self,text="Dirección : "+list(Cita.iloc[list(Cita['Sede']==self.controller.Sede)]['Dir'])[0],font=("Raleway",12))
            self.label11.place(x=10,y=260)
            self.label9=tk.Label(self,text="Medico : "+ self.controller.Medico,font=("Raleway",12))
            self.label9.place(x=10,y=290)
            self.label10=tk.Label(self,text="Fecha : "+ self.controller.Fecha ,font=("Raleway",12))
            self.label10.place(x=10,y=320)
            ayuda_btn=tk.Button(self,text="Agendar nueva cita",font="Raleway",bg="cyan",fg="black",command=lambda:controller.show_frame('ACitas'))
            ayuda_btn.place(x=450,y=400)
              
        
class Seguro(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label=tk.Label(self,text="Contacte a su compañia de seguro",font=("Raleway",16),bg="yellow")
        label.place(x=350,y=50)

        label=tk.Label(self,text="Sede principal",font=("Raleway",16))
        label.place(x=100,y=280)

        label2=tk.Label(self,text=" A continuación, se le muestra los medios de contacto del seguro al que se encuentra afiliado:",font=("Raleway",12))
        label2.place(x=200,y=100)

        label3=tk.Label(self,text= " • Dirección: Av. Juan de Arona 830, San Isidro - Lima 27",font=("Raleway",12))
        label3.place(x=100,y=325)
        
        label4=tk.Label(self,text= " • Teléfono: (511)518-4000",font=("Raleway",12))
        label4.place(x=100,y=350)
        
        label5=tk.Label(self,text= " • Fax: (511)518-4295/518-4299",font=("Raleway",12))
        label5.place(x=100,y=375)
        
        logo_label=tk.Label (self)
        logo_label.place(x=600,y=260)
        logo=Image.open("emergencia.png")
        logo = logo.resize((280, 150))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        logo_label=tk.Label (self)
        logo_label.place(x=430,y=140)
        logo=Image.open("pacifico.jpg")
        logo = logo.resize((150, 50))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        
        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)

class ACitas(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller
        self.var1=tk.StringVar(self)        
        self.var1.set("Presione para elegir")
        
        self.var2=tk.StringVar(self)        
        self.var2.set("Presione para elegir")
        
        self.var3=tk.StringVar(self)        
        self.var3.set("Presione para elegir")
        
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label=tk.Label(self,text="Agende una cita",font=("Raleway",16))
        label.place(x=400,y=50)
 
        label2=tk.Label(self,text="Por favor, llene sus datos a continuación para agendar una cita:",font=("Raleway",12))
        label2.place(x=200,y=100)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)

        doctores=list(dict.fromkeys(Cita['Doctor']))       
        sedes=list(dict.fromkeys(Cita['Sede']))       
        area=list(dict.fromkeys(Cita['Area']))       
        
        label3=tk.Label(self,text="Doctor :",font=("Raleway",12))
        label3.place(x=750,y=150)

        op_Doctor=tk.OptionMenu(self,self.var1,*doctores)
        op_Doctor.place(x=700,y=200)
        
        label4=tk.Label(self,text="Sede/Clinica :",font=("Raleway",12))
        label4.place(x=450,y=150)
        
        op_Sede=tk.OptionMenu(self,self.var2,*sedes)
        op_Sede.place(x=400,y=200)

        label50=tk.Label(self,text="Especialidad :",font=("Raleway",12))
        label50.place(x=150,y=150)

        op_Esp=tk.OptionMenu(self,self.var3,*area)
        op_Esp.place(x=100,y=200)

        label60=tk.Label(self,text="Al presionar CONTINUAR, se agenda la fecha más proxima disponible para su atención",font=("Raleway",10))
        label60.place(x=300,y=275)

        boton_continuar = ttk.Button( self, text = "CONTINUAR", command = self.verificar )   # Boton de continuar
        boton_continuar.place(x=425,y=250)
        boton_continuar.bind( "<Button-1>",self.verificar)

        self.label_adver=tk.Label(self, textvariable="",font=("Raleway",12),fg="red")  # Label de advertencia de error
        self.label_adver.place(x=400,y=300)

    def verificar(self,*args,**kwargs):           # Método para verificar si el usuario está registrado y pasar al inicio

        if self.var1.get()=="Presione para elegir" or self.var2.get()=="Presione para elegir" or self.var3.get()=="Presione para elegir":            
            self.label_adver.configure(text="Por favor, llene correctamente los cuadros")
              
        else:            
            
            label5=tk.Label(self,text="Usted a elegido la siguiente cita :",font=("Raleway",12))
            label5.place(x=10,y=350)
            año,mes,dia=str(datetime.now()).split()[0].split('-')
            self.controller.Fecha=str(int(dia)+random.randint(0,15))+"-"+mes+"-"+año
            self.controller.Medico=self.var1.get()
            self.controller.Sede=self.var2.get()
            self.controller.Especialidad=self.var3.get()
        
            self.label7=tk.Label(self,text="Especialidad : "+self.var3.get(),font=("Raleway",12))
            self.label7.place(x=10,y=390)
            self.label8=tk.Label(self,text="Sede : "+ self.var2.get(),font=("Raleway",12))
            self.label8.place(x=10,y=420)
            self.label9=tk.Label(self,text="Medico : "+ self.var1.get(),font=("Raleway",12))
            self.label9.place(x=10,y=450)
            self.label10=tk.Label(self,text="Fecha : "+ self.controller.Fecha ,font=("Raleway",12))
            self.label10.place(x=10,y=480)
                
            self.men=tk.Label(self,text="Si desea cambiar la fecha u otra opción de la cita, por favor, volver a presionar el botón 'CONTINUAR' ",font=("Raleway",12), fg='blue')
            self.men.place(x=10,y=510)
            
            self.controller.todos_los_frames['Citas']=Citas(self.controller.pantalla,self.controller)
            self.controller.todos_los_frames['Citas'].grid(row = 0, column = 0, sticky = 'nsew')
            self.controller.show_frame('ACitas')
            
            boton_correo = tk.Button( self, text = "Confirmar y enviar constancia a correo electrónico",font="Raleway", bg="cyan",fg="black", command = lambda: self.controller.cons_cita())
            boton_correo.place(x=600,y=550)
            
class Historial(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)

        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label=tk.Label(self,text="Historial Clinico",font=("Raleway",16))
        label.place(x=400,y=50)

        label2=tk.Label(self,text="Aquí puede ver su historial clínico desde que se afilio a su seguro privado de salud:",font=("Raleway",12))
        label2.place(x=200,y=150)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)
        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)

class Control(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller
        
        
        logo_label=tk.Label(self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        robot_label=tk.Label(self)
        robot_label.place(x=400,y=200)
        robot=Image.open("robot.png")
        robot = robot.resize((300,353))
        robot = ImageTk.PhotoImage(robot)
        robot_label.configure(image=robot)
        robot_label.image=robot
        
        label=tk.Label(self,text="Control de Salud",font=("Raleway",16))
        label.place(x=400,y=50)

        label=tk.Label(self,text="A continuacion, se procederá a la toma de resultados de altura, peso, temperatura, oxígeno en la sangre.\n Por favor, seleccione las opciones de control que requiera en la parte izquierda y lea las instrucciones. Gracias.",font=("Raleway",12))
        label.place(x=100,y=100)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
        
        Medicion_Altura=tk.Button(self,text="Altura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlAltura'))
        Medicion_Altura.place(x=50,y=200)

        Medicion_Peso=tk.Button(self,text="Peso",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlPeso'))
        Medicion_Peso.place(x=50,y=270)

        Medicion_Temperatura=tk.Button(self,text="Temperatura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlTemperatura'))
        Medicion_Temperatura.place(x=50,y=340)

        Medicion_Oximetro = tk.Button(self, text="Oximetro" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('Control_Oximetro'))
        Medicion_Oximetro.place(x=50, y=410)

        molestias = tk.Button(self, text="Molestias" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('ControlMolestias'))
        molestias.place(x=50, y=480)
        
        verde_label=tk.Label(self)
        verde_label.place(x=850,y=500)
        verde=Image.open("flechaverde.png")
        verde = verde.resize((100,100))
        verde = ImageTk.PhotoImage(verde)
        verde_label.configure(image=verde)
        verde_label.image=verde
        
        label=tk.Label(self,text="Siguiente",font=("Raleway",16))
        label.place(x=750,y=530)
        
        verde_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlAltura' ))
             
class ControlAltura(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller

        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        ad=tk.Label(self,text="Por favor, ubíquese al centro de la cabina sobre la superficie de la balanza \n como se muestra en la imagen inferior",font=("Raleway",12))
        ad.place(x=300,y=150)
        
        ima_label=tk.Label (self)
        ima_label.place(x=350,y=200)
        ima=Image.open("ultrasonico.jpg")
        ima = ima.resize((190, 300))
        ima = ImageTk.PhotoImage(ima)
        ima_label.configure(image=ima)
        ima_label.image=ima
        
        ima2_label=tk.Label (self)
        ima2_label.place(x=540,y=200)
        ima2=Image.open("balanza.jpg")
        ima2 = ima2.resize((190, 300))
        ima2 = ImageTk.PhotoImage(ima2)
        ima2_label.configure(image=ima2)
        ima2_label.image=ima2


        label=tk.Label(self,text="Medicion de altura",font=("Raleway",16))
        label.place(x=400,y=50)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Control'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
        
        Medicion_Altura=tk.Button(self,text="Altura",font="Raleway",bg="green",fg="white",command=lambda:controller.show_frame('ControlAltura'))
        Medicion_Altura.place(x=50,y=200)

        Medicion_Peso=tk.Button(self,text="Peso",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlPeso'))
        Medicion_Peso.place(x=50,y=270)

        Medicion_Temperatura=tk.Button(self,text="Temperatura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlTemperatura'))
        Medicion_Temperatura.place(x=50,y=340)

        Medicion_Oximetro = tk.Button(self, text="Oximetro" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('Control_Oximetro'))
        Medicion_Oximetro.place(x=50, y=410)

        molestias = tk.Button(self, text="Molestias" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('ControlMolestias'))
        molestias.place(x=50, y=480)
        
        verde_label=tk.Label(self)
        verde_label.place(x=850,y=500)
        verde=Image.open("flechaverde.png")
        verde = verde.resize((100,100))
        verde = ImageTk.PhotoImage(verde)
        verde_label.configure(image=verde)
        verde_label.image=verde
        
        label=tk.Label(self,text="Siguiente",font=("Raleway",16))
        label.place(x=750,y=530)

        label2=tk.Label(self,text="Atrás",font=("Raleway",16))
        label2.place(x=310,y=530)
        
        roja_label=tk.Label(self)
        roja_label.place(x=200,y=500)
        roja=Image.open("flecharoja.png")
        roja = roja.resize((100,100))
        roja =ImageTk.PhotoImage(roja)
        roja_label.configure(image=roja)
        roja_label.image=roja
        
        verde_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlPeso' ))
        roja_label.bind("<Button-1>",lambda x:controller.show_frame( 'Control' ))  
 
        logo_label.bind("<Button-1>",lambda x: self.graficar())
        logo_label.bind("<Button-2>",lambda x: self.get_result())
        
    def get_result(self):
        
        self.canvas2.destroy()
        print(id(self.controller), " Controlador ControlAltura funcion")
        y_data=[]
        estatura=random.randint(160,180)+random.randint(-1,1)*random.random()
        y_data.append(estatura+random.random()*random.randint(-1,1))
        
        
        self.controller.Estatura=round(np.mean(y_data),2)
        
        self.canvas=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas.place(x=200,y=150)
        
        self.canvas.create_text(350,175,font=("Raleway",20),text="Altura: "+str(self.controller.Estatura)+" cm",fill="white")
        
    
    def graficar(self):
        
        self.canvas2=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas2.place(x=200,y=150)
        self.canvas2.create_text(350,300,font=("Raleway",16),text="Obteniendo resultados \n Por favor, espere ...",fill="white")
        
        framesNum = 80 # Numero de frames que tiene el gif, si no lo conoces ir haciendo tentativos.
        
        frames = [tk.PhotoImage(file="loading1.gif", format='gif -index %i' %(i)) for i in range(framesNum)]
        
        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == framesNum:
                ind = 0
            self.canvas2.create_image(275, 125, image=frame,anchor='nw')
            self.after(10, update, ind) # Numero que regula la velocidad del gif
        self.after(0, update, 0)
    
class ControlPeso(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller
        
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        ad=tk.Label(self,text="Por favor, ubíquese al centro de la cabina sobre la superficie de la balanza \n como se muestra en la imagen inferior",font=("Raleway",12))
        ad.place(x=300,y=150)
        
        ima_label=tk.Label (self)
        ima_label.place(x=350,y=200)
        ima=Image.open("ultrasonico.jpg")
        ima = ima.resize((190, 300))
        ima = ImageTk.PhotoImage(ima)
        ima_label.configure(image=ima)
        ima_label.image=ima
        
        ima2_label=tk.Label (self)
        ima2_label.place(x=540,y=200)
        ima2=Image.open("balanza.jpg")
        ima2 = ima2.resize((190, 300))
        ima2 = ImageTk.PhotoImage(ima2)
        ima2_label.configure(image=ima2)
        ima2_label.image=ima2


        label=tk.Label(self,text="Control de Peso",font=("Raleway",16))
        label.place(x=400,y=50)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Control'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
        
        Medicion_Altura=tk.Button(self,text="Altura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlAltura'))
        Medicion_Altura.place(x=50,y=200)

        Medicion_Peso=tk.Button(self,text="Peso",font="Raleway",bg="green",fg="white",command=lambda:controller.show_frame('ControlPeso'))
        Medicion_Peso.place(x=50,y=270)

        Medicion_Temperatura=tk.Button(self,text="Temperatura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlTemperatura'))
        Medicion_Temperatura.place(x=50,y=340)

        Medicion_Oximetro = tk.Button(self, text="Oximetro" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('Control_Oximetro'))
        Medicion_Oximetro.place(x=50, y=410)

        molestias = tk.Button(self, text="Molestias" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('ControlMolestias'))
        molestias.place(x=50, y=480)
        
        verde_label=tk.Label(self)
        verde_label.place(x=850,y=500)
        verde=Image.open("flechaverde.png")
        verde = verde.resize((100,100))
        verde = ImageTk.PhotoImage(verde)
        verde_label.configure(image=verde)
        verde_label.image=verde

        roja_label=tk.Label(self)
        roja_label.place(x=200,y=500)
        roja=Image.open("flecharoja.png")
        roja = roja.resize((100,100))
        roja =ImageTk.PhotoImage(roja)
        roja_label.configure(image=roja)
        roja_label.image=roja
        
        label=tk.Label(self,text="Siguiente",font=("Raleway",16))
        label.place(x=750,y=530)

        label2=tk.Label(self,text="Atrás",font=("Raleway",16))
        label2.place(x=310,y=530)
        
        verde_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlTemperatura' ))
        roja_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlAltura' ))       
        
        logo_label.bind("<Button-1>",lambda x: self.graficar())
        logo_label.bind("<Button-2>",lambda x: self.get_result())
    
    def get_result(self):
        
        self.canvas2.destroy()
        y_data=[]
        peso=random.randint(50,100)+random.randint(-1,1)*random.random()
        y_data.append(peso+random.random()*random.randint(-1,1))
        
        self.controller.Peso=round(np.mean(y_data),2)
        
        self.canvas=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas.place(x=200,y=150)
        
        self.canvas.create_text(350,175,font=("Raleway",20),text="Peso: "+str(self.controller.Peso)+" kg",fill="white")
        
        
        
    def graficar(self):
        
        self.canvas2=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas2.place(x=200,y=150)
        self.canvas2.create_text(350,300,font=("Raleway",16,"italic"),text="Obteniendo resultados \n Por favor, espere ...",fill="white")
        
        framesNum = 80 # Numero de frames que tiene el gif, si no lo conoces ir haciendo tentativos.
        
        frames = [tk.PhotoImage(file="loading1.gif", format='gif -index %i' %(i)) for i in range(framesNum)]
        
        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == framesNum:
                ind = 0
            self.canvas2.create_image(275, 125, image=frame,anchor='nw')
            self.after(10, update, ind) # Numero que regula la velocidad del gif
        #canvas2.pack()
        self.after(0, update, 0)
        
class ControlTemperatura(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        ad=tk.Label(self,text="Por favor, levante su cabeza a la altura de la caja superior \n como se muestra en la imagen inferior",font=("Raleway",12))
        ad.place(x=300,y=150)
        
        ima_label=tk.Label (self)
        ima_label.place(x=350,y=200)
        ima=Image.open("term_infra.jpg")
        ima = ima.resize((350, 300))
        ima = ImageTk.PhotoImage(ima)
        ima_label.configure(image=ima)
        ima_label.image=ima
        
        
        label=tk.Label(self,text="Control de Temperatura",font=("Raleway",16))
        label.place(x=400,y=50)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Control'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
    
        Medicion_Altura=tk.Button(self,text="Altura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlAltura'))
        Medicion_Altura.place(x=50,y=200)

        Medicion_Peso=tk.Button(self,text="Peso",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlPeso'))
        Medicion_Peso.place(x=50,y=270)

        Medicion_Temperatura=tk.Button(self,text="Temperatura",font="Raleway",bg="green",fg="white",command=lambda:controller.show_frame('ControlTemperatura'))
        Medicion_Temperatura.place(x=50,y=340)

        Medicion_Oximetro = tk.Button(self, text="Oximetro" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('Control_Oximetro'))
        Medicion_Oximetro.place(x=50, y=410)

        molestias = tk.Button(self, text="Molestias" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('ControlMolestias'))
        molestias.place(x=50, y=480)
        
        verde_label=tk.Label(self)
        verde_label.place(x=850,y=500)
        verde=Image.open("flechaverde.png")
        verde = verde.resize((100,100))
        verde = ImageTk.PhotoImage(verde)
        verde_label.configure(image=verde)
        verde_label.image=verde

        roja_label=tk.Label(self)
        roja_label.place(x=200,y=500)
        roja=Image.open("flecharoja.png")
        roja = roja.resize((100,100))
        roja =ImageTk.PhotoImage(roja)
        roja_label.configure(image=roja)
        roja_label.image=roja
        
        label=tk.Label(self,text="Siguiente",font=("Raleway",16))
        label.place(x=750,y=530)

        label2=tk.Label(self,text="Atrás",font=("Raleway",16))
        label2.place(x=310,y=530)
        
        verde_label.bind("<Button-1>",lambda x:controller.show_frame( 'Control_Oximetro' ))
        roja_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlPeso' ))
        
        logo_label.bind("<Button-1>",lambda x: self.graficar())
        logo_label.bind("<Button-2>",lambda x: self.get_result())
    
    def get_result(self):
        
        self.canvas2.destroy()
        y_data=[]
        temperatura=random.randint(36,38)+random.randint(-1,1)*random.random()
        y_data.append(temperatura+random.random()*random.randint(-1,1))
        
        
        self.controller.Temperatura=round(np.mean(y_data),2)
        
        self.canvas=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas.place(x=200,y=150)
        
        self.canvas.create_text(350,175,font=("Raleway",20),text="Temperatura: "+str(self.controller.Temperatura)+" °C",fill="white")

    
    
    def graficar(self):
        
        self.canvas2=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas2.place(x=200,y=150)
        self.canvas2.create_text(350,300,font=("Raleway",16,"italic"),text="Obteniendo resultados \n Por favor, espere ...",fill="white")
        
        framesNum = 80 # Numero de frames que tiene el gif, si no lo conoces ir haciendo tentativos.
        
        frames = [tk.PhotoImage(file="loading1.gif", format='gif -index %i' %(i)) for i in range(framesNum)]
        
        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == framesNum:
                ind = 0
            self.canvas2.create_image(275, 125, image=frame,anchor='nw')
            self.after(10, update, ind) # Numero que regula la velocidad del gif
        #canvas2.pack()
        self.after(0, update, 0)
                 
class Control_Oximetro(tk.Frame):
    
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        self.controller=controller
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        ad=tk.Label(self,text="Por favor, coloque su dedo en el oxímetro al lado derecho de la pantalla \n como se muestra en la imagen superior",font=("Raleway",12))
        ad.place(x=300,y=150)
        
        oxi_label=tk.Label (self)
        oxi_label.place(x=300,y=200)
        oxi=Image.open("oximetro.jpg")
        oxi = oxi.resize((510,300))
        oxi = ImageTk.PhotoImage(oxi)
        oxi_label.configure(image=oxi)
        oxi_label.image=oxi

        label=tk.Label(self,text="Control de Oxigeno en la sangre",font=("Raleway",16))
        label.place(x=400,y=50)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Control'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
    
        Medicion_Altura=tk.Button(self,text="Altura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlAltura'))
        Medicion_Altura.place(x=50,y=200)

        Medicion_Peso=tk.Button(self,text="Peso",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlPeso'))
        Medicion_Peso.place(x=50,y=270)

        Medicion_Temperatura=tk.Button(self,text="Temperatura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlTemperatura'))
        Medicion_Temperatura.place(x=50,y=340)

        Medicion_Oximetro = tk.Button(self, text="Oximetro" , font="Raleway", bg="green", fg="white", command=lambda: controller.show_frame('Control_Oximetro'))
        Medicion_Oximetro.place(x=50, y=410)

        molestias = tk.Button(self, text="Molestias" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('ControlMolestias'))
        molestias.place(x=50, y=480)
        
        verde_label=tk.Label(self)
        verde_label.place(x=850,y=500)
        verde=Image.open("flechaverde.png")
        verde = verde.resize((100,100))
        verde = ImageTk.PhotoImage(verde)
        verde_label.configure(image=verde)
        verde_label.image=verde

        roja_label=tk.Label(self)
        roja_label.place(x=200,y=500)
        roja=Image.open("flecharoja.png")
        roja = roja.resize((100,100))
        roja =ImageTk.PhotoImage(roja)
        roja_label.configure(image=roja)
        roja_label.image=roja
        
        label=tk.Label(self,text="Siguiente",font=("Raleway",16))
        label.place(x=750,y=530)

        label2=tk.Label(self,text="Atrás",font=("Raleway",16))
        label2.place(x=310,y=530)
        
        verde_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlMolestias' ))
        roja_label.bind("<Button-1>",lambda x:controller.show_frame( 'ControlTemperatura' ))

        logo_label.bind("<Button-1>",lambda x: self.graficar())
        logo_label.bind("<Button-2>",lambda x: self.get_result())
    
    def get_result(self):
        
        self.canvas2.destroy()
        x=loadmat("100m.mat")
        ecg=(x['val']-0)/200
        ecg=np.transpose(ecg)
        fs=random.randint(50,110)
        ts=1/fs
        t=np.linspace(0,np.size(ecg),np.size(ecg))*ts
        t=t[t<=20]
        ecg=ecg[range(len(t))]
        ox=random.randint(92,102)
        self.frame2 = tk.Frame(self, bg='#031E32', bd=1.5)
        self.frame2.place(x=200,y=150)
        self.frame2.config(width=705,height=350)
        #self.canvas.create_text(350,175,font=("Raleway",20),text="Temperatura: "+str(self.controller.Temperatura)+" °C",fill="white")
        self.grafica = tk.Frame(self, bg='#031E32', bd=1.5)
        self.grafica.place(x=200,y=150)
        self.grafica.config(width=700,height=350)
        self.figure = plt.Figure(figsize=(7,2), dpi=100, frameon=True)
        x = t
        y = ecg
        self.ax = self.figure.add_subplot()
        self.ax.grid(True)
        self.line = FigureCanvasTkAgg(self.figure, self.grafica)
        self.line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        self.controller.PR=fs
        self.controller.Ox=ox
        
        self.ax.plot(x,y), self.ax.grid(True)
        self.ax.set_title('Frecuencia de pulso')
        self.line.draw()   
        
        self.l_pr=tk.Label(self,text='PR :'+str(fs),font=("Raleway",16),bg='#031E32',fg='white')
        self.l_pr.place(x=375,y=400)
        self.l_sp=tk.Label(self,text='SpO2 (%):'+str(ox),font=("Raleway",16),bg='#031E32',fg='white')
        self.l_sp.place(x=575,y=400)
        
        
    def graficar(self):
        
        self.canvas2=tk.Canvas(self,width=700, height=350,bg='#031E32')
        self.canvas2.place(x=200,y=150)
        self.canvas2.create_text(350,300,font=("Raleway",16,"italic"),text="Obteniendo resultados \n Por favor, espere ...",fill="white")
        
        framesNum = 80 # Numero de frames que tiene el gif, si no lo conoces ir haciendo tentativos.
        
        frames = [tk.PhotoImage(file="loading1.gif", format='gif -index %i' %(i)) for i in range(framesNum)]
        
        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == framesNum:
                ind = 0
            self.canvas2.create_image(275, 125, image=frame,anchor='nw')
            self.after(10, update, ind) # Numero que regula la velocidad del gif
        self.after(0, update, 0)
    
class ControlMolestias(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config(bg = "black",width=1000,height=600)
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        musculos_label=tk.Label (self)
        musculos_label.place(x=200,y=100)
        musculos=Image.open("musculos.jpg")
        musculos = musculos.resize((700, 400))
        musculos = ImageTk.PhotoImage(musculos)
        musculos_label.configure(image=musculos)
        musculos_label.image=musculos

        label=tk.Label(self,text="Control de molestias",font=("Raleway",25))
        label.place(x=400,y=50)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Control'))
        atras_btn.place(x=10,y=10)

        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)

        Medicion_Altura=tk.Button(self,text="Altura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlAltura'))
        Medicion_Altura.place(x=50,y=200)

        Medicion_Peso=tk.Button(self,text="Peso",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlPeso'))
        Medicion_Peso.place(x=50,y=270)

        Medicion_Temperatura=tk.Button(self,text="Temperatura",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('ControlTemperatura'))
        Medicion_Temperatura.place(x=50,y=340)

        Medicion_Oximetro = tk.Button(self, text="Oximetro" , font="Raleway", bg="#212121", fg="white", command=lambda: controller.show_frame('Control_Oximetro'))
        Medicion_Oximetro.place(x=50, y=410)

        molestias = tk.Button(self, text="Molestias" , font="Raleway", bg="green", fg="white", command=lambda: controller.show_frame('ControlMolestias'))
        molestias.place(x=50, y=480)
                
        verde_label=tk.Label(self)
        verde_label.place(x=850,y=500)
        verde=Image.open("flechaverde.png")
        verde = verde.resize((100,100))
        verde = ImageTk.PhotoImage(verde)
        verde_label.configure(image=verde)
        verde_label.image=verde

        roja_label=tk.Label(self)
        roja_label.place(x=200,y=500)
        roja=Image.open("flecharoja.png")
        roja = roja.resize((100,100))
        roja =ImageTk.PhotoImage(roja)
        roja_label.configure(image=roja)
        roja_label.image=roja
        
        label=tk.Label(self,text="Finalizar",font=("Raleway",16))
        label.place(x=750,y=530)
        
        label2=tk.Label(self,text="Atrás",font=("Raleway",16))
        label2.place(x=310,y=530)
        
        verde_label.bind("<Button-1>",lambda x:controller.show_frame( 'Inicio' ))
        roja_label.bind("<Button-1>",lambda x:controller.show_frame( 'Control_Oximetro' ))

#from datetime import datetime
class Foto(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller=controller
        self.config(bg="gray", width=1000, height=600)
        logo_label = tk.Label(self)
        logo_label.place(x=0, y=0)
        logo = Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image = logo
        label1 = tk.Label(self, text="A continuacion se le tomara una foto para confirmar su asistencia", font=("Raleway", 14))
        label1.place(x=65, y=70)
        label2 = tk.Label(self, text="Presione (Iniciar) para Iniciar la camara.",
                         font=("Raleway", 14))
        label2.place(x=65, y=140)
        label3= tk.Label(self,
                         text="Parese frente a la camara hasta que vea el recuadro verde.",
                         font=("Raleway", 14))
        label3.place(x=65, y=210)
        label4 = tk.Label(self,
                          text="Presione (Tomar foto)",
                          font=("Raleway", 14))

        label4.place(x=65, y=280)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        def deteccion_facilal(frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceClassif.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return frame
        def visualizar():
            global cap
            if cap is not None:
                ret, frame = cap.read()
                if ret == True:
                    frame = imutils.resize(frame, width=800)
                    deteccion_facilal(frame)
                    n=0
                    tomar_foto(frame,n)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    im = Image.fromarray(frame)
                    img = ImageTk.PhotoImage(image=im)
                    lblVideo.configure(image=img)
                    lblVideo.image = img
                    lblVideo.after(10, visualizar)
                else:
                    lblVideo.image = ""
                    cap.release()
        def iniciar():
            global cap
            cap = cv2.VideoCapture(0)
            visualizar()
        def tomar_foto(frame,n):
            n=n+1
            if(n==1):
                fecha=str(datetime.now().strftime('%Y-%m-%d %H-%M') )
                cv2.imwrite("C:\\Users\\Manuel\\Documents\\GitHub\\Proyecto\\Fotos\\"+fecha+".png",frame)
        def finalizar():
            cap.release()
        Iniciar = tk.Button(self, text="Iniciar",font=("Raleway", 14), width=30, command=iniciar)
        Iniciar.place(x=60, y=20)
        Finalizar = tk.Button(self, text="Tomar Foto",font=("Raleway", 14), width=30, command=lambda: [finalizar(),controller.show_frame('Inicio')])
        Finalizar.place(x=500, y=20)
        lblVideo = tk.Label(self)
        lblVideo.place(x=65, y=75)

Data=pd.read_csv("Base_de_datos.csv")#leer datos
Cita=pd.read_csv("citas.csv")
root = INTERFAZ()

root.mainloop()

