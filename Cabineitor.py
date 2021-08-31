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

import cv2
import imutils
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from datetime import datetime
import numpy as np
from fpdf import FPDF
from scipy.io import loadmat


#Pandas para leer el csv

def cast_float(string):
    aux=string[1:len(string)-1]
    aux=aux.split(', ')
    ax=[]
    for i in aux:
        ax.append(float(i))
    return ax

def cast_str(string):
    aux=string[1:len(string)-1].split("', '")
    aux[0]=aux[0][1:]
    aux[len(aux)-1]=aux[len(aux)-1][:-1]
    return aux
    
    
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

        self.title("INTERFAZ MEDICAB")    #Titulo y dimension de ventana
        self.geometry("1000x600")
        self.Apellido=""                      #Variables de usuario para acceder desde cualquier frame hija
        self.Nombre=""
        self.Correo=""
        self.Contrasena=""
        self.Edad=0
        self.Sexo=""
        self.Altura=0
        self.Temperatura=                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       0
        self.Estatura=0
        self.Peso=0
        self.PR=0
        self.Ox=0
        self.Cita=""
        self.Especialidad=""
        self.Medico=""
        self.Fecha=""
        self.Sede=""
        self.HPeso=0
        self.HFecha=[]
        self.HFP=[]
        self.HOx=[]
        self.IMC=[]
        self.imc=0
        self.HTemp=0
        self.HEst=0
        self.molestias=[]
        self.index=0
        self.Codigo=0
        self.FechaC=""
        
        self.pantalla = tk.Frame()            #Frame principal
        self.pantalla.grid(sticky = "nsew")

        self.todos_los_frames = dict()         #Diccionario de los Frames(clases hijas) a usar
        
        #Creacion de los frames hijos
        
        self.todos_los_frames['Foto'] = Foto(container=self.pantalla, controller=self)
        self.todos_los_frames['Foto'].grid(row=0, column=0, sticky='nsew')
        self.todos_los_frames['Inicio'] = Inicio(container=self.pantalla, controller=self)
        self.todos_los_frames['Inicio'].grid(row=0, column=0, sticky='nsew')

        #----------------------------------------------------------------------------------------------------
        
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
        mail = "medicab.informa@gmail.com"
        passw = "medicab123"
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
        pdf.cell(180,20,"Fecha: "+self.Fecha,0,10,"C")
        pdf.cell(100, 10, "Paciente: "+self.Nombre+" "+self.Apellido, 1, 0)
        pdf.cell(40, 10, "Sexo: "+self.Sexo, 1, 0)
        pdf.cell(45, 10, "Edad: "+str(int(self.Edad)), 1, 1)
        pdf.cell(62,10,"Estatura (cm): "+str(self.Estatura),1,0)
        pdf.cell(61,10,"Peso (kg): "+str(round(self.Peso,2)),1,0)
        pdf.cell(62,10,"Temperatura (°C): "+str(self.Temperatura),1,1)
        pdf.cell(50,10,"Frecuencia de pulso: "+str(self.PR),1,0)
        pdf.cell(75,10,"Nivel de oxígeno en la sangre (%): "+str(self.Ox),1,0)
        pdf.cell(60,10,"Indice de Masa Corporal: "+str(round(self.imc,2)),1,1)
        pdf.cell(180,15,"A continuación, se presenta la evolución de sus índices de salud en los ultimos meses:",0,1)
        
        pdf.set_font('Times','B',12)
        pdf.ln(7)
        pdf.cell(180,10,'Indice de Masa Corporal (IMC):',0,1,'L')
        
        pdf.set_font('Times','',12)
        pdf.cell(180,5,"- Si su IMC es inferior a 18.5, esta dentro de",0,1,'L')
        pdf.cell(180,5,"  los valores correspondientes a 'bajo peso'.",0,1,'L')
        pdf.ln(3)
        pdf.cell(180,5,"- Si su IMC es entre 18.5 y 24.9, esta dentro",0,1,'L')
        pdf.cell(180,5,"  de los valores 'normales' o de peso saludable.",0,1,'L')
        pdf.ln(3)
        pdf.cell(180,5,"- Si su IMC es entre 25.0 y 29.9, esta dentro",0,1,'L')
        pdf.cell(180,5,"  de los valores correspondientes a 'sobrepeso'.",0,1,'L')
        pdf.ln(3)
        pdf.cell(180,5,"- Si su IMC es 30.0 o superior, esta dentro de",0,1,'L')
        pdf.cell(180,5,"  los valores de 'obesidad'.",0,1,'L')
        
        pdf.set_font('Times','B',12)
        pdf.ln(35)
        pdf.cell(180,10,'Saturacion de Oxigeno en la Sangre:',0,1,'L')
        pdf.set_font('Times','',12)
        pdf.cell(180,5,"- Se considera que el porcentaje adecuado de",0,1,'L')
        pdf.cell(180,5,"  oxígeno en sangre es de entre el 95% - 100%",0,1,'L')
        pdf.ln(3)
        pdf.cell(180,5,"- Si su saturacion se encuentra por debajo del 90%,",0,1,'L')
        pdf.cell(180,5,"  se produce 'hipoxemia'",0,1,'L')
        
        x=cast_str(self.HFecha)
        x=[i[0:5] for i in x]
        y1=cast_float(self.IMC)
        y2=cast_float(self.HOx)
        y3=cast_float(self.HFP)
        
        fig=plt.figure()
        plt.ion()
        plt.plot(x,y1)
        plt.title("Índice de Masa Corporal (últimos 3 meses)")
        plt.xlabel("Fechas")
        plt.ylim(10,50)
        plt.ioff()
        plt.savefig("Nivel_IMC.png",bbox_inches='tight')
        plt.close(fig)
        
        fig=plt.figure()
        plt.ion()
        plt.plot(x,y2)
        plt.title("Saturación de Oxigeno (%) (últimos 3 meses)")
        plt.xlabel("Fechas")
        plt.ylim(80,120)
        plt.ioff()
        plt.savefig("Nivel_Oxi.png",bbox_inches='tight')
        plt.close(fig)
        
        fig=plt.figure()
        plt.ion()
        plt.plot(x,y3)
        plt.title("Pulso de Frecuencia Cardiaca promedio (últimos 3 meses)")
        plt.xlabel("Fechas")
        plt.ylim(40,120)
        plt.ioff()
        plt.savefig("Nivel_FR.png",bbox_inches='tight')
        plt.close(fig)
        
        pdf.image('Nivel_IMC.png',110,120,90,70)
        pdf.image('Nivel_Oxi.png',110,200,90,70)
        pdf.add_page()
        pdf.image('CABINEITOR.png',-5,-10,60,60)
        pdf.image('pacifico.png',145,5,55,20)
        pdf.image('Nivel_FR.png',110,40,90,70)
        
        pdf.set_font('Times','B',12)
        pdf.ln(40)
        pdf.cell(180,10,'Frecuencia de Pulso por minuto:',0,1,'L')
        pdf.set_font('Times','',12)
        pdf.cell(180,5,"- Una frecuencia cardíaca en reposo normal para los",0,1,'L')
        pdf.cell(180,5,"  adultos oscila entre 60 y 100 latidos por minuto",0,1,'L')
        pdf.ln(3)
        pdf.cell(180,5,"- Una frecuencia mayor a 100 pulsos por minuto",0,1,'L')
        pdf.cell(180,5,"  puede recurrir a una 'taquicardia'",0,1,'L')
        pdf.ln(3)
        pdf.cell(180,5,"- Una frecuencia menor a 60 pulsos por minuto",0,1,'L')
        pdf.cell(180,5,"  puede recurrir a una 'bradicardia'",0,1,'L')
        pdf.ln(30)
        
        pdf.set_font('Times','B',12)
        pdf.cell(180,5,"Recomendaciones :",0,1,'L')
        pdf.set_font('Times','',12)
        pdf.cell(180,5,"- Recordar que este reporte de salud NO DIAGNOSTICA enfermedades o sintomas en pacientes.",0,1,'L')
        pdf.cell(180,5,"- En caso de identificar anormalidades, se recomienda agendar una cita con un médico.",0,1,'L')
        
        
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
        
        
class Bienvenida(tk.Frame):      # Primera clase de frame

    def __init__(self, container, controller,*args, **kwargs):   #Constructor, se pasa controller como la clase padre, para acceder al método ShowFrame

        super().__init__(container, *args, **kwargs)             #Heredando
        self.config(bg = "gray",width=1000,height=600)
        self.controller=controller
        #logo,sus dimensiones y archivo

        logo_label=tk.Label(self,bg="black")
        logo_label.place(x=500,y=280,anchor="center")
        logo=Image.open("CABINEITOR.png")
        logo=ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label_empezar = tk.Label( self, text = "Toque para empezar ...", font = ("Raleway",12),bg = "white" )
        label_empezar.place(x=500,y=500,anchor="center")
        
        self.bind("<Button-1>",lambda x:self.Pasar())
        logo_label.bind("<Button-1>",lambda x:self.Pasar())
        label_empezar.bind("<Button-1>",lambda x:self.Pasar())
        
    def Pasar(self):
        self.controller.Apellido=""              #Variables de usuario para acceder desde cualquier frame hija
        self.controller.Nombre=""
        self.controller.Correo=""
        self.controller.Contrasena=""
        self.controller.Edad=0
        self.controller.Sexo=""
        self.controller.Altura=0
        self.controller.Temperatura=0
        self.controller.Estatura=0
        self.controller.Peso=0
        self.controller.PR=0
        self.controller.Ox=0
        self.controller.Cita=""
        self.controller.Especialidad=""
        self.controller.Medico=""
        self.controller.Fecha=""
        self.controller.Sede=""
        self.controller.HPeso=0
        self.controller.HFecha=[]
        self.controller.HFP=[]
        self.controller.HOx=[]
        self.controller.IMC=[]
        self.controller.imc=0
        self.controller.HTemp=0
        self.controller.HEst=0
        self.controller.molestias=[]
        self.controller.index=0
        self.controller.show_frame('Mario')
        
        
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
    
        boton_continuar = tk.Button( self, text = "CONTINUAR", command = self.verificar )   # Boton de continuar
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
               if self.contrasena.get()=="contraseña":
                   self.controller.index=Data.index[Data['Codigo']==int(self.codigo_usuario.get())].tolist()[0]
                   self.controller.Apellido=aux['Apellido']
                   self.controller.Nombre=aux['Nombre']
                   self.controller.Correo=aux['Correo']
                   self.controller.Contrasena="contraseña"
                   self.controller.Codigo=self.codigo_usuario.get()
                   self.controller.Edad=aux['Edad']
                   self.controller.Sexo=aux['Sexo']
                   self.Esp_Entrada.delete(0,"end")
                   self.Esp_Contra.delete(0,"end")
                   self.controller.todos_los_frames['Inicio'] = Inicio(container = self.controller.pantalla, controller = self.controller)
                   self.controller.todos_los_frames['Inicio'].grid(row=0,column=0,sticky="nsew")
                   self.controller.show_frame('Inicio')
                   self.controller.HFecha=aux['HFecha']
                   self.controller.HOx=aux['HOx']
                   self.controller.HFP=aux['HFP']
                   self.controller.IMC=aux['IMC']
                   self.controller.HPeso=aux['HPeso']
                   self.controller.HEst=aux['Estatura']
                   self.controller.HTemp=aux['Temp']
                   self.controller.Estatura=aux['Estatura']
                   self.controller.Temperatura=aux['Temp']
                   self.controller.Peso=cast_float(aux['HPeso'])[-1]
                   self.controller.Ox=cast_float(aux['HOx'])[-1]
                   self.controller.PR=cast_float(aux['HFP'])[-1]
                   self.controller.Fecha=cast_str(aux['HFecha'])[-1]
                   self.controller.imc=self.controller.Peso/(self.controller.Estatura/100)**2
                   self.label_adver.configure(text="")
                   self.controller.show_frame('Foto')
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

        self.saludo_label=tk.Label(self, text="Bienvenido a MEDICAB \n \n ¿Qué deseas hacer?" , font="Raleway", fg="#212121")
        self.saludo_label.place(x=100,y=50)
    
        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
        
        consultar_cita_btn=tk.Button(self,text="Consultar citas",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('Citas'))
        consultar_cita_btn.place(x=800,y=100)
        
        contactar_seguro_btn=tk.Button(self,text="Contacte a su seguro",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('Seguro'))
        contactar_seguro_btn.place(x=800,y=200)

        agende_cita_btn=tk.Button(self,text="Agende una cita",font="Raleway",bg="gray",fg="black",command=lambda:controller.show_frame('ACitas'))
        agende_cita_btn.place(x=800,y=300)

        historial_btn=tk.Button(self,text="Ver historial clínico",font="Raleway",bg="gray",fg="black",command= self.ing_historial)
        historial_btn.place(x=800,y=400)
        
        control_btn=tk.Button(self,text="Empezar control de salud",font="Raleway",bg="green",fg="black",command=self.control)
        control_btn.place(x=800,y=500)
        
        correo_btn=tk.Button(self,text="Mandar reporte a correo",font="Raleway",bg="cyan",fg="black",command=lambda:self.controller.reporte_salud())
        correo_btn.place(x=500,y=500)
    
    #correo_btn=tk.Button(self,text="Mandar reporte a correo",font="Raleway",bg="cyan",fg="black",command=self.mandar_repor())
        
    
     #def mandar_repor(self):
     #   self.controller.reporte_salud()
     #   self.l=tk.Label(self, text="Se envió con éxito" , font="Raleway", fg="#212121")
     #   self.l.place(x=500,y=550)
        
        
     def ing_historial(self):
        self.controller.todos_los_frames['Historial']=Historial(self.controller.pantalla,self.controller)
        self.controller.todos_los_frames['Historial'].grid(row = 0, column = 0, sticky = 'nsew')
        self.controller.show_frame('Historial')

     def control(self):
        self.controller.todos_los_frames['ControlAltura']=ControlAltura(self.controller.pantalla,self.controller)
        self.controller.todos_los_frames['ControlPeso']=ControlPeso(self.controller.pantalla,self.controller)
        self.controller.todos_los_frames['ControlTemperatura']=ControlTemperatura(self.controller.pantalla,self.controller)
        self.controller.todos_los_frames['Control_Oximetro']=Control_Oximetro(self.controller.pantalla,self.controller)
        self.controller.todos_los_frames['ControlMolestias']=ControlMolestias(self.controller.pantalla,self.controller)
        
        self.controller.todos_los_frames['ControlAltura'].grid(row = 0, column = 0, sticky = 'nsew')
        self.controller.todos_los_frames['ControlPeso'].grid(row = 0, column = 0, sticky = 'nsew')
        self.controller.todos_los_frames['ControlTemperatura'].grid(row = 0, column = 0, sticky = 'nsew')
        self.controller.todos_los_frames['Control_Oximetro'].grid(row = 0, column = 0, sticky = 'nsew')
        self.controller.todos_los_frames['ControlMolestias'].grid(row = 0, column = 0, sticky = 'nsew')
        
        self.controller.show_frame('Control')
             
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

        label=tk.Label(self,text="Sección de Ayuda",font=("Raleway",16),bg="yellow")
        label.place(x=400,y=50)
        
        label2=tk.Label(self,text="Bienvenido a la sección de ayuda. Aquí se presentan las preguntas más frecuentes \n sobre MEDICAB. Por favor, lea con atención y siga las instrucciones",font=("Raleway",11))
        label2.place(x=200,y=85)
        
        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)

        
        label3=tk.Label(self,text="• ¿Qué es MEDICAB?",font=("Raleway",12,"bold"))
        label3.place(x=75,y=130)        

        label4=tk.Label(self,text="• ¿Cada cuánto tiempo se tendré una cita en MEDICAB?",font=("Raleway",12,"bold"))
        label4.place(x=75,y=230)

        label5=tk.Label(self,text="• ¿Cuál es el tiempo de respuesta cuando agendo una cita médica en MEDICAB?",font=("Raleway",12,"bold"))
        label5.place(x=75,y=300)
        
        label6=tk.Label(self,text="• ¿Qué hago si la información de mí control de salud no llego a mi correo?",font=("Raleway",12,"bold"))
        label6.place(x=75,y=370)

        label7=tk.Label(self,text="• ¿Qué hacer en caso de emergencia asociado con uno de los sensores?",font=("Raleway",12,"bold"))
        label7.place(x=75,y=440)

        label31=tk.Label(self,text="MEDICAB es un robot creado para tener un control de salud sobre los usuarios con el fin de prevenir diversas enfermedades. De esta manera, \n cuenta con cuatro sensores que miden la temperatura, la altura, peso y el nivel de oxígeno en la sangre. Adicionalmente se auto desinfecta y \n cuenta con el servicio de agendar una cita médica con un doctor.                                                                                                                   ",font=("Raleway",10),anchor="w")
        label31.place(x=75,y=150)
        
        label41=tk.Label(self,text="La programación se da aproximadamente cada semana. Para más información consulté en la interfaz de inicio de MEDICAB en CONSULTAR CITAS. \n En caso se presentará algún inconveniente para acceder a la información envié un correo medicab.informa@gmail.com                                                ",font=("Raleway",10))
        label41.place(x=75,y=250)

        label51=tk.Label(self,text="El tiempo de respuesta para agendar una cita médica dependerá únicamente de su seguro. Se aconseja contactar a su seguro para más información.",font=("Raleway",10))
        label51.place(x=75,y=320)

        label61=tk.Label(self,text="En caso se presentará que la información del control de salud no llegará a su correo envié un correo a medicab.informa@gmail.com	. \n El equipo de asistencia de MEDICAB lo atenderá lo más pronto posible.                                                                                                                   ",font=("Raleway",10))
        label61.place(x=75,y=390)

        label71=tk.Label(self,text="MEDICAB cuenta con un botón rojo de emergencia el cual se encuentra ubicado en la parte inferior izquierda de la pantalla.",font=("Raleway",10))
        label71.place(x=75,y=460)

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

        label=tk.Label(self,text="Sección de Citas",font=("Raleway",16),bg="yellow")
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

        label=tk.Label(self,text="Sede principal",font=("Raleway",16),bg="yellow")
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

        label=tk.Label(self,text="Agende una cita",font=("Raleway",16),bg="yellow")
        label.place(x=400,y=50)
 
        label2=tk.Label(self,text="Por favor, seleccione las casillas a continuación para agendar una cita:",font=("Raleway",12))
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
        self.controller=controller
        
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo

        label=tk.Label(self,text="Historial Clinico",font=("Raleway",16),bg="yellow")
        label.place(x=400,y=50)

        label2=tk.Label(self,text="Aquí puede ver su historial clínico desde que se afilio a su seguro privado de salud:",font=("Raleway",12))
        label2.place(x=200,y=100)

        atras_btn=tk.Button(self,text="Atras",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Inicio'))
        atras_btn.place(x=10,y=10)
        ayuda_btn=tk.Button(self,text="Ayuda",font="Raleway",bg="#212121",fg="white",command=lambda:controller.show_frame('Ayuda'))
        ayuda_btn.place(x=900,y=10)
        
        if(self.controller.HFecha!=[]):
            label3=tk.Label(self,text="Datos de su último control de salud",font=("Raleway",12))
            label3.place(x=100,y=150)
            
            self.label10=tk.Label(self,text="• Fecha de último control : "+ self.controller.Fecha ,font=("Raleway",12))
            self.label10.place(x=50,y=200)
            self.label7=tk.Label(self,text="• Peso (kg): "+ str(round(self.controller.Peso,2)),font=("Raleway",12))
            self.label7.place(x=50,y=230)
            self.label8=tk.Label(self,text="• Temperatura (°C): "+ str(self.controller.Temperatura),font=("Raleway",12))
            self.label8.place(x=50,y=260)
            self.label9=tk.Label(self,text="• Estatura (cm) : "+str(self.controller.Estatura),font=("Raleway",12))
            self.label9.place(x=50,y=290)
            self.label02=tk.Label(self,text="• Nivel de Oxígeno en la sangre (%) : "+str(self.controller.Ox),font=("Raleway",12))
            self.label02.place(x=50,y=320)
            self.label03=tk.Label(self,text="• Frecuencia de Pulso : "+str(self.controller.PR),font=("Raleway",12))
            self.label03.place(x=50,y=350)
            
            if(self.controller.molestias!=[]):
                self.label04=tk.Label(self,text="• Se presentaron molestias en las siguientes \n partes del cuerpo: ",font=("Raleway",12))
                self.label04.place(x=50,y=400)
                message=""
                o=0
                for i in self.controller.molestias:
                    message=message+" - "+i
                    o+=1
                    if o==4:
                        message=message+" \n "
                        o=0
                        
                        
                self.label05=tk.Label(self,text=message,font=("Raleway",12))
                self.label05.place(x=50,y=450)
                
            x=cast_str(self.controller.HFecha)
            x=[i[0:5] for i in x]
            y=cast_float(self.controller.IMC)
            
            self.grafica = tk.Frame(self, bg='gray', bd=1)
            self.grafica.place(x=400,y=150)
            self.grafica.config(width=375,height=250)
            self.figure = plt.Figure(figsize=(6.5,2), dpi=100, frameon=True)
            
            self.ax = self.figure.add_subplot()
            self.ax.grid(True)
            self.line = FigureCanvasTkAgg(self.figure, self.grafica)
            self.line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
            
            self.ax.plot(x,y), self.ax.grid(True)
            self.ax.set_title('Indice de Masa Corporal (últimos 3 meses)')
            self.line.draw()
           
            x=cast_str(self.controller.HFecha)
            x=[i[0:5] for i in x]
            y=cast_float(self.controller.HOx)
            
            self.grafica = tk.Frame(self, bg='gray', bd=1)
            self.grafica.place(x=400,y=375)
            self.grafica.config(width=375,height=250)
            self.figure = plt.Figure(figsize=(6.5,2), dpi=100, frameon=True)
            
            self.ax = self.figure.add_subplot()
            self.ax.grid(True)
            self.line = FigureCanvasTkAgg(self.figure, self.grafica)
            self.line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
            
            self.ax.plot(x,y), self.ax.grid(True)
            self.ax.set_title('Nivel de oxígeno en la sangre (últimos 3 meses)')
            self.line.draw()           
            
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
        robot=Image.open("medicion.png")
        robot = robot.resize((300,353))
        robot = ImageTk.PhotoImage(robot)
        robot_label.configure(image=robot)
        robot_label.image=robot
        
        label=tk.Label(self,text="Control de Salud",font=("Raleway",16),bg="yellow")
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


        label=tk.Label(self,text="Medicion de altura",font=("Raleway",16),bg="yellow")
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
        
        verde_label=tk.Label(self,bg="#EBEBEB")
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


        label=tk.Label(self,text="Control de Peso",font=("Raleway",16),bg="yellow")
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
        
        
        label=tk.Label(self,text="Control de Temperatura",font=("Raleway",16),bg="yellow")
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

        label=tk.Label(self,text="Control de Oxigeno en la sangre",font=("Raleway",16),bg="yellow")
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
        self.controller=controller
        logo_label=tk.Label (self)
        logo_label.place(x=0,y=0)
        logo=Image.open("generico.png")
        logo = logo.resize((1000, 600))
        logo = ImageTk.PhotoImage(logo)
        logo_label.configure(image=logo)
        logo_label.image=logo
        
        label=tk.Label(self,text="Control de molestias",font=("Raleway",16),bg="yellow")
        label.place(x=400,y=50)
        
        label2=tk.Label(self,text="Por favor, pulse los botones correspondientes hacia las zonas en las que sienta \n alguna molestia muscular. En caso no sentir ninguna, presione FINALIZAR:",font=("Raleway",12))
        label2.place(x=300,y=100)

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
        
        verde_label.bind("<Button-1>", self.finalizar)
        roja_label.bind("<Button-1>",lambda x:controller.show_frame( 'Control_Oximetro' ))
        
        a=200
        b=150
        
        img1 = ImageTk.PhotoImage(Image.open("musculos_final_2.png"))
        panel1 = tk.Label(self, image=img1)
        panel1.place(x=50+a, y=5+b)
        panel1.image=img1
        img2 = ImageTk.PhotoImage(Image.open("musculos_final_3.png"))
        panel2 = tk.Label(self, image=img2)
        panel2.place(x=300+a, y=5+b)
        panel2.image=img2
        img3 = ImageTk.PhotoImage(Image.open("musculos_final_1.png"))
        panel3 = tk.Label(self, image=img3)
        panel3.place(x=550+a, y=15+b)
        panel3.image=img3
        #---------------------------------------------------------------
        #Botones
        #---------------------------------------------------------------
        #Primera_imagen
        self.Boca = tk.Button(self,width=4,height=1, text="Boca", font=("Raleway",8), bg="White", fg="black", command=self.cambiar_color_Boca)
        self.Boca.place(x=50+a, y=10+b)
        self.Ojos= tk.Button(self, width=4, height=1, text="Ojos", font=("Raleway", 8), bg="White", fg="black",command=self.cambiar_color_Ojos)
        self.Ojos.place(x=180+a, y=10+b)
        self.Pecho = tk.Button(self, width=4, height=1, text="Pecho", font=("Raleway", 8), bg="White", fg="black",
                           command=self.cambiar_color_Pecho)
        self.Pecho.place(x=200+a, y=85+b)
        self.Muñeca = tk.Button(self, width=5, height=1, text="Muñeca", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Muñeca)
        self.Muñeca.place(x=20+a, y=160+b)
        self.Palma = tk.Button(self, width=4, height=1, text="Palma", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Palma)
        self.Palma.place(x=50+a, y=230+b)
        self.Estomago = tk.Button(self, width=7, height=1, text="Estomago", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Estomago)
        self.Estomago.place(x=200+a, y=130+b)
        self.Pulgar = tk.Button(self, width=7, height=1, text="Pulgar", font=("Raleway", 8), bg="White",
                               fg="black",
                               command=self.cambiar_color_Pulgar)
        self.Pulgar.place(x=220+a, y=193+b)
        self.Dedo = tk.Button(self, width=7, height=1, text="Dedo", font=("Raleway", 8), bg="White",
                             fg="black",
                             command=self.cambiar_color_Dedo)
        self.Dedo.place(x=180+a, y=220+b)
        self.Rodilla = tk.Button(self, width=7, height=1, text="Rodilla", font=("Raleway", 8), bg="White",
                             fg="black",
                             command=self.cambiar_color_Rodilla)
        self.Rodilla.place(x=200+a, y=270+b)
        #Segunda imagen
        self.Oreja = tk.Button(self, width=4, height=1, text="Oreja", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Oreja)
        self.Oreja.place(x=410+a, y=23+b)
        self.Cuello = tk.Button(self, width=4, height=1, text="Cuello", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Cuello)
        self.Cuello.place(x=409+a, y=50+b)
        self.Hombro = tk.Button(self, width=5, height=1, text="Hombro", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Hombro)
        self.Hombro.place(x=440+a, y=80+b)
        self.Codo = tk.Button(self, width=5, height=1, text="Codo", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Codo)
        self.Codo.place(x=440+a, y=125+b)
        self.Nalga = tk.Button(self, width=5, height=1, text="Nalga", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Nalga)
        self.Nalga.place(x=435+a, y=170+b)
        self.Talon= tk.Button(self, width=5, height=1, text="Talon", font=("Raleway", 8), bg="White", fg="black",
                           command=self.cambiar_color_Talon)
        self.Talon.place(x=400+a, y=315+b)
        #Imagen Tres
        self.Frente = tk.Button(self, width=4, height=1, text="Frente", font=("Raleway", 8), bg="White", fg="black",
                          command=self.cambiar_color_Frente)
        self.Frente.place(x=660+a, y=23+b)
        self.Nariz = tk.Button(self, width=4, height=1, text="Nariz", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Nariz)
        self.Nariz.place(x=650+a, y=60+b)
        self.Cadera = tk.Button(self, width=5, height=1, text="Cadera", font=("Raleway", 8), bg="White", fg="black",
                            command=self.cambiar_color_Cadera)
        self.Cadera.place(x=665+a, y=150+b)
        self.Antebrazo = tk.Button(self, width=8, height=1, text="Antebrazo", font=("Raleway", 8), bg="White", fg="black",
                             command=self.cambiar_color_Antebrazo)
        self.Antebrazo.place(x=500+a, y=150+b)
        self.Muslo =tk. Button(self, width=8, height=1, text="Muslo", font=("Raleway", 8), bg="White",
                                fg="black",
                                command=self.cambiar_color_Muslo)
        self.Muslo.place(x=520+a, y=220+b)
        self.Canilla = tk.Button(self, width=8, height=1, text="Canilla", font=("Raleway", 8), bg="White",
                            fg="black",
                            command=self.cambiar_color_Canilla)
        self.Canilla.place(x=520+a, y=290+b)
        self.Tobillo = tk.Button(self, width=8, height=1, text="Tobillo", font=("Raleway", 8), bg="White",
                              fg="black",
                              command=self.cambiar_color_Tobillo)
        self.Tobillo.place(x=520+a, y=320+b)
        
        
        
        
        
    def cambiar_color_Boca(self):
        self.Boca.configure(bg="Yellow")
        self.controller.molestias.append("Boca")
    def cambiar_color_Ojos(self):
        self.Ojos.configure(bg="#32CD32")
        self.controller.molestias.append("Ojos")
    def cambiar_color_Pecho(self):
        self.Pecho.configure(bg="#00FFFF")
        self.controller.molestias.append("Pecho")
    def cambiar_color_Estomago(self):
        self.Estomago.configure(bg="Red")
        self.controller.molestias.append("Estomago")
    def cambiar_color_Muñeca(self):
        self.Muñeca.configure(bg="#FF00FF")
        self.controller.molestias.append("Estomago")
    def cambiar_color_Palma(self):
        self.Palma.configure(bg="Blue")
        self.controller.molestias.append("Palma")
    def cambiar_color_Pulgar(self):
        self.Pulgar.configure(bg="Yellow")
        self.controller.molestias.append("Pulgar")
    def cambiar_color_Dedo(self):
        self.Dedo.configure(bg="#32CD32")
        self.controller.molestias.append("Dedo")
    def cambiar_color_Rodilla(self):
        self.Rodilla.configure(bg="#FF00FF")
        self.controller.molestias.append("Rodilla")
    def cambiar_color_Oreja(self):
        self.Oreja.configure(bg="#00FFFF")
        self.controller.molestias.append("Oreja")
    def cambiar_color_Cuello(self):
        self.Cuello.configure(bg="Blue")
        self.controller.molestias.append("Cuella")
    def cambiar_color_Hombro(self):
        self.Hombro.configure(bg="#32CD32")
        self.controller.molestias.append("Hombro")
    def cambiar_color_Codo(self):
        self.Codo.configure(bg="#FF00FF")
        self.controller.molestias.append("Codo")
    def cambiar_color_Nalga(self):
        self.Nalga.configure(bg="Red")
        self.controller.molestias.append("Nalga")
    def cambiar_color_Talon(self):
        self.Talon.configure(bg="Yellow")
        self.controller.molestias.append("Talon")
    def cambiar_color_Frente(self):
        self.Frente.configure(bg="#FF00FF")
        self.controller.molestias.append("Frente")
    def cambiar_color_Nariz(self):
        self.Nariz.configure(bg="Red")
        self.controller.molestias.append("Nariz")
    def cambiar_color_Antebrazo(self):
        self.Antebrazo.configure(bg="#00FFFF")
        self.controller.molestias.append("Antebrazo")
    def cambiar_color_Cadera(self):
        self.Cadera.configure(bg="Yellow")
        self.controller.molestias.append("Cadera")
    def cambiar_color_Muslo(self):
        self.Muslo.configure(bg="Blue")
        self.controller.molestias.append("Muslo")
    def cambiar_color_Canilla(self):
        self.Canilla.configure(bg="#32CD32")
        self.controller.molestias.append("Canilla")
    def cambiar_color_Tobillo(self):
        self.Tobillo.configure(bg="Red")
        self.controller.molestias.append("Tobillo")
        
    def finalizar(self,*args,**kwargs):
        aux=cast_float(Data.at[self.controller.index,'HPeso'])[1:len(cast_float(Data.at[self.controller.index,'HPeso']))]
        aux.append(self.controller.Peso)
        Data.at[self.controller.index,'HPeso']=str(aux)
        
        aux=cast_float(Data.at[self.controller.index,'HOx'])[1:len(cast_float(Data.at[self.controller.index,'HOx']))]
        aux.append(self.controller.Ox)
        Data.at[self.controller.index,'HOx']=str(aux)
        
        aux=cast_float(Data.at[self.controller.index,'HFP'])[1:len(cast_float(Data.at[self.controller.index,'HFP']))]
        aux.append(self.controller.PR)
        Data.at[self.controller.index,'HFP']=str(aux)
        
        self.controller.imc=self.controller.Peso/(self.controller.Estatura/100)**2 
        aux=cast_float(Data.at[self.controller.index,'IMC'])[1:len(cast_float(Data.at[self.controller.index,'IMC']))]
        aux.append(self.controller.imc)
        Data.at[self.controller.index,'IMC']=str(aux)
        
        Data.at[self.controller.index,'Temp']=self.controller.Temperatura
        Data.at[self.controller.index,'Estatura']=self.controller.Estatura
                
        aux=cast_str(Data.at[self.controller.index,'HFecha'])[1:len(cast_str(Data.at[self.controller.index,'HFecha']))]
        aux.append(datetime.now().strftime("%d/%m/%Y"))
        Data.at[self.controller.index,'HFecha']=str(aux)
        
        
        self.controller.Fecha=datetime.now().strftime("%d/%m/%Y")
        
        self.controller.show_frame( 'Inicio' )
        
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
                fecha=str(datetime.now().strftime('%Y-%m-%d_%H-%M') )
                cv2.imwrite("C:/Users/Manuel/Documents/GitHub/Proyecto/Fotos/"+fecha+"_"+self.controller.Codigo+".png",frame)
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

#Data.to_csv('Base_de_datos.csv')





