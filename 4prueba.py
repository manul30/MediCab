# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 13:07:26 2021

@author: Manuel
"""

#DATOS RANDOM
import random

import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use('ggplot')
x_data=[]
y_data=[]
data_importante=[]
estatura=random.randint(160,180)+random.randint(-1,1)*random.random()
temperatura=random.randint(33,40)+random.randint(-1,1)*random.random()



figure=pyplot.figure()
#plt.ylim(estatura-10,estatura+10)
plt.ylim(temperatura-10,temperatura+10)

line, =pyplot.plot_date(x_data,y_data,'-')

t = datetime.now().time()
seconds = (t.hour * 60 + t.minute) * 60 + t.second

def grafico(frame):
    #asdasdfdasafasfadsfad
    #asdadadfasdadfasdd
    x_data.append(datetime.now())
    #y_data.append(estatura+random.random()*random.randint(-1,1))  #estatura
    #aux=datetime.now().time()
    num=temperatura+random.randint(-1,1)*random.random()*np.sin(2)
    
    data_importante.append(num)
    y_data.append(num)
    #try:
    #    y_data.append(num)
    #    if len(y_data)>50:
    #        y_data.pop(0)
    #except:
    #        pass
    if len(y_data)>50:
            x_data.pop(0)
            y_data.pop(0)
            
    line.set_data(x_data,y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
       
    #return line,

a=FuncAnimation(figure, grafico, interval=100)
pyplot.show()    




# 60 100 PR
# spO 95-99

'''
import matplotlib.pyplot as plt
import numpy as np 
import random

a=[]
for k,v in zip([1,-1],[0.02,0.98]):
    a+=[k]*int(v*100)

t=np.linspace(0,100,2000).tolist()
x=[]
y=[]
w=100

factor=np.array([])

for i in t:
    aa=np.cos(2*i)+0.5
    if aa<=0:

        x.append(0)
        y.append(0*np.sin(i))
    else:
        x.append(aa)
        y.append(aa*np.sin(w/20*i)*random.random()+0.5)
    
plt.ylim(-10,10)
plt.plot(t,x)
plt.plot(t,y)



'''

"""import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def B0f():
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(4*x)
    ax.clear()
    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('$y(x)=sin(4x)$')
    line.draw()
    
def B1f():
    x = np.linspace(0,2*np.pi,100)
    y = np.cos(4*x)
    ax.clear()
    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('$y(x)=cos(4x)$')
    line.draw()
    
def B2f():
    x = np.linspace(0,2*np.pi,100)
    y = np.exp(-0.5*x)*np.sin(4*x)
    ax.clear()
    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('$y(x)=e^{-0.5x}sin(4x)$')
    line.draw()

def B3f():
    x = np.linspace(0,10,100)
    y = np.exp(x)
    ax.clear()
    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('y(x)')
    ax.set_title('$y(x) = e^{x}$')
    line.draw()
    
def B4f():
    def gaussian(x, mu, sig):
        return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)
    x = np.linspace(0,10,100)
    y = gaussian(x,5,1.3)
    ax.clear()
    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('y(x)')
    ax.set_title('$y(x) = Gaussian(x,5,1.3)$')
    line.draw()

#--- Raiz ---
root = tk.Tk()
root.geometry('940x450')
root.title("Tkinter + Matplotlib")
#------------

#-- Frames ---
left_frame = tk.Frame(root)
left_frame.place(relx=0.03, rely=0.05, relwidth=0.25, relheight=0.9)

right_frame = tk.Frame(root, bg='#C0C0C0', bd=1.5)
right_frame.place(relx=0.3, rely=0.05, relwidth=0.65, relheight=0.9)
#---------------

#--- Botones ---
RH = 0.19

B0 = tk.Button(left_frame,text="SIN(4x)",command = B0f)
B0.place(relheight=RH, relwidth=1)

B1 = tk.Button(left_frame,text="COS(4x)",command = B1f)
B1.place(rely=(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

B2 = tk.Button(left_frame,text="EXP(-0.5x)SIN(x)",command = B2f)
B2.place(rely= 2*(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

B3 = tk.Button(left_frame,text="EXP(x)",command = B3f)
B3.place(rely= 3*(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

B4 = tk.Button(left_frame,text="Gaussian(x)",command = B4f)
B4.place(rely= 4*(0.1 + RH*0.54) ,relheight=RH, relwidth=1)
#------------

#--- Agregar figura ---
figure = plt.Figure()
ax = figure.add_subplot(111)
ax.grid(True),ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
line = FigureCanvasTkAgg(figure, right_frame)
line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#----------------------

root.mainloop()"""



"""
import collections
import tkinter as tk

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import font as tkFont
import numpy as np


class VentanaSeñales(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        plt.style.use('dark_background')
        self.frame_graficas = tk.Frame(self, bg="#6E6E6E")
        self._figure_1, self._ax1 = plt.subplots()
        self._figure_1_canvas = FigureCanvasTkAgg(
            self._figure_1, master=self.frame_graficas
            )
        self._figure_2, self._ax2 = plt.subplots()
        self._figure_2_canvas = FigureCanvasTkAgg(
            self._figure_2, master=self.frame_graficas
            )
        self._figure_3, self._ax3 = plt.subplots()
        self._figure_3_canvas = FigureCanvasTkAgg(
            self._figure_3, master=self.frame_graficas
            )

        self.frame_graficas.grid_columnconfigure(0, weight=1, uniform="fig")
        self.frame_graficas.grid_columnconfigure(1, weight=1, uniform="fig")
        self.frame_graficas.grid_columnconfigure(2, weight=1, uniform="fig")

        self._figure_1_canvas.get_tk_widget().grid(
            row=0, column=0, padx=(10, 30), pady=(30, 30),
            sticky="nsew"
            )
        self._figure_2_canvas.get_tk_widget().grid(
            row=0, column=1, padx=(10, 30), pady=(30, 30),
            sticky="nsew"
            )
        self._figure_3_canvas.get_tk_widget().grid(
            row=0, column=2, padx=(10, 30), pady=(30, 30),
            sticky="nsew"
            )

        
        self.frame_botones = tk.Frame(self, bg="#151515")
        
        self.btn_iniciar = tk.Button(
            self.frame_botones, bg="#7401DF", fg="#FFBF00",
            activebackground="#8258FA", font=('Courier', 16),
            text="Iniciar", command=self.iniciar_animación
            )
        self.btn_pausar = tk.Button(
            self.frame_botones, bg="#7401DF", fg="#FFBF00",
            activebackground="#8258FA", font=('Courier', 16),
            text="  Pausa  ", command=self.pausar_animación, state=tk.DISABLED
            )
        self.btn_iniciar.pack(
            side="left", padx=(100, 100), pady=(100, 100),
            fill="y", expand=True
            )
        self.btn_pausar.pack(
            side="left", padx=(100, 100), pady=(100, 100),
            fill="y", expand=True
            )
        

        self._anim1 = None
        self._anim2 = None
        self._anim3 = None

        self.frame_graficas.pack(fill="both", expand=True)
        self.frame_botones.pack(fill="x")
        self._init_axes()

    def _init_axes(self):

        self._ax1.set_title('Signal')
        self._ax1.set_xlabel("Time")
        self._ax1.set_ylabel("Amplitude")
        self._ax1.set_xlim(0, 100)
        self._ax1.set_ylim(-1, 1)

        self._ax2.set_title('Signal2')
        self._ax2.set_xlabel("Time")
        self._ax2.set_ylabel("Amplitude")
        self._ax2.set_xlim(0, 100)
        self._ax2.set_ylim(-1, 1)

        self._ax3.set_title('Signal3')
        self._ax3.set_xlabel("Time")
        self._ax3.set_ylabel("Amplitude")
        self._ax3.set_xlim(0, 100)
        self._ax3.set_ylim(-1, 1)


    def iniciar_animación(self):

        def animate(values):
            value=values
            data.append(value)
            lines.set_data(range(0, 100), data)
            return lines

        def animate2(values):
            value=values
            data2.append(value)
            lines2.set_data(range(0, 100), data2)
            return lines2

        def animate3(values):
            value=values
            data3.append(value)
            lines3.set_data(range(0, 100), data3)
            return lines3

        def data_gen():
            for k in range(100):
                t = k / 100
                yield 0.5 * np.sin(40 * t) * np.exp(-2 * t)

        def data_gen2():
            for k in range(100):
                t = k / 100
                yield 0.5 * np.sin(60 * t)

        def data_gen3():
            for k in range(100):
                t = k / 100
                yield 0.5 * np.cos(60 * t)

        if self._anim1 is None:
            lines = self._ax1.plot([], [], color='#80FF00')[0]
            lines2 = self._ax2.plot([], [], color='#80FF00')[0]
            lines3 = self._ax3.plot([], [], color='#80FF00')[0]

            data = collections.deque([0] * 100, maxlen=100)
            data2 = collections.deque([0] * 100, maxlen=100)
            data3 = collections.deque([0] * 100, maxlen=100)

            self._anim1 = animation.FuncAnimation(
                self._figure_1, animate, data_gen, interval=5
                )
            self._anim2 = animation.FuncAnimation(
                self._figure_2, animate2, data_gen2, interval=5
                )
            self._anim3 = animation.FuncAnimation(
                self._figure_3, animate3, data_gen3, interval=5
                )

            self._figure_1_canvas.draw()
            self._figure_2_canvas.draw()
            self._figure_3_canvas.draw()

            self.btn_pausar.configure(state=tk.NORMAL)
            self.btn_iniciar.configure(text="Detener")
        else:
            self._ax1.lines = []  
            self._ax2.lines = []
            self._ax3.lines = []
            self.btn_pausar.configure(state=tk.DISABLED, text="  Pausa  ")
            self.btn_iniciar.configure(text="Iniciar")
            self._anim1 = self._anim2 = self._anim3 = None


    def pausar_animación(self):
        if self.btn_pausar["text"] == "  Pausa  ":
            self._anim1.event_source.stop()
            self._anim2.event_source.stop()
            self._anim3.event_source.stop()
            self.btn_pausar.configure(text="Continuar")

        else:
            self._anim1.event_source.start()
            self._anim2.event_source.start()
            self._anim3.event_source.start()
            self.btn_pausar.configure(text="  Pausa  ")



if __name__ == "__main__":
    root = tk.Tk()
    VentanaSeñales(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
"""


