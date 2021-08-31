# Tutoriales
# Santiago
import tkinter as tk
from tkinter import ttk
# ------------------------------------------------------------------------
# Ventana_principal_llamada_root(No corre hasta llamarla con root.mainloop()
from tkinter.ttk import Label

"""root = tk.Tk()
# Forma sencilla de crear un texto
Nombre_Cabineitor = ttk.Label(root, text="Cabineitor :V")
Nombre_Cabineitor.grid(row=0, column=0)  # Para poner el texto en la ventana pack().Luego se hara con grid()

# --------------------------------------------------------------------------------
# Caja donde guardo información
Ingreso_codigo = ttk.Label(root, text="")
Ingreso_codigo.grid(row=1, column=0, columnspan=3)
# columnspan o rowspan permiten hacer widgets de "grosor" de N columas o filas
# Es como la posicion de una caja dentro de una caja
# Caja de tipo string
codigo_de_usuario = tk.StringVar()
Entrada_1 = ttk.Entry(root, width=20, textvariable=codigo_de_usuario)
Entrada_1.grid(row=0, column=1)
Entrada_1.focus()  # Para que parpadee:V


# Funcion para que al hacer click te muestre en la pantalla un texto
def funcion_tocame():
    Ingreso_codigo.configure(text="Bienvenido {}".format(codigo_de_usuario.get()))


boton_ingrese = ttk.Button(root, text="Ingrese", command=funcion_tocame)
# Creando el boton para ingresar codigo
boton_ingrese.grid(row=0, column=2, padx=(10, 50))
# Obs: Indicaba_posicion(Padding)
# Mirar padx como "padding en x externo"
boton_salir = ttk.Button(root, text="Salir", command=quit)
boton_salir.grid(row=0, column=3)
# Creando boton para salir
# -----------------------------------------------------------------------------
#MANEJO SENCILLO DE BOTONES Y "ENTRY" EN TKINTER
#------------------------------------------------------------------------
#Es fundamental tener widgets interactivos para el programa, como los botoes y entry fields.
#Ambos se deben crear primero y luego posicionar por alguno de los dos sistemas (grid/pack)


#Es util-para indicar el path cuando trabajemos con "png", "jpg"y "ico"
import os
#--------------------------------COMIENZA LA CREACION DE LA VENTANA DE TRABAJO----------------------------------

#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("PERSONALIZACION VENTANA TKINTER")

#Se agregan las dimensiones deseadas de la ventana de trabajo
root.geometry( "1000x500" )

#Se agrega el icono de la ventana de trabajo, el cual tambien se indica en la parte superior a la izquierda
#...se debe tener el icono en formato "ico" en la misma carpeta de trabajo (sino, indicar path absoluto)
root.iconbitmap( "{}\\ICON_2.ico".format( os.getcwd() ) )

#Imagenes
# proceso tambien incluye redimensionar la imagen a los pixeles deseados, en este caso a con redondeo del porcentaje
# total de la pantalla...(con Image.ANTIALIAS) img_1 = ImageTk.PhotoImage( Image.open("FOTO_1.jpg").resize( (
# math.floor(w*0.1),math.floor(h*0.2)),Image.ANTIALIAS ) )
img_1 = ImageTk.PhotoImage( Image.open("FOTO_1.jpg").resize( (500,200),Image.ANTIALIAS ) )
#Se crea la imagen sobre widget de Label, con parametro "image"
cuadro_img_1 = tk.Label( root, image = img_1 )
#Se agrega visualmente en el grid o lugar donde se desee mostrar
cuadro_img_1.grid( column = 0, row = 0)
#Despegable
#Se debe crear variable asociada al menu respectivo...(para indicar elegido respectivo)

elegido_menu_1 = tk.StringVar(root)
elegido_menu_1.set("ELEGIR PROYECTO")
#Se crea el menu y luego se coloca en root...
#...OJO: CREAR MENU A PARTIR DE VECTOR:
VECTOR = []
for i in range( 50 ):
    VECTOR.append( str(i+1) + ". PROYECTO ALGO" )
#TRUCO: importar modulo ttk desde tkinter (ver al inicio), para tener un dropdownmenu mucho mejor y que tenga scrollbar (en caso de ser muchos proyectos)
menu_1 = ttk.Combobox( root, textvariable = elegido_menu_1, values = VECTOR )
menu_1.grid(row = 1, column = 3)
#Se ejecuta el "mainloop" que permite correr el codigo de la ventana correctamente
root.mainloop()"""
# Los Frames son una especie de "contenedores" que facilitaran la organizacion visual...
# ... el objetivo es que se organice visualmente el programa con ayuda de Frames que a su vez...
# ... se disponen en la ventana principal de trabajo (que la hemos llamado root)
# Es decir:
# Permite crear Frames dentro del root, para organizacion mas sencilla, algo asi:
# ROOT:
# **************************************************************
# *                                                            *
# *                                                            *
# *                        FRAME 1                             *
# *                                                            *
# *                                                            *
# *                                                            *
# *                                                            *
# **************************************************************
# *                            *                               *
# *                            *                               *
# *                            *                               *
# *                            *                               *
# *        FRAME 2             *             FRAME 3           *
# *                            *                               *
# *                            *                               *
# *                            *                               *
# *                            *                               *
# *                            *                               *
# **************************************************************


# ------------------------------------------------------------------------

# Frames
''''#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("FRAMES")

#IMPORTANTE: observar que cada Frame se agrega al root
#Se crea el Frame 1 (contenedor 1 de la ventana), indicando el parent (root)
Frame_1 = ttk.Frame(root)
Frame_1.pack(side = "top", fill = "both", expand = True)

#Se crea el Frame 2 (contenedor 2 de la ventana), indicando el parent (root)
Frame_2 = ttk.Frame(root)
Frame_2.pack(side = "left", fill = "both", expand = True)

#Se crea el Frame 3 (contenedor 3 de la ventana), indicando el parent (root)
Frame_3 = ttk.Frame(root)
Frame_3.pack(side = "left", fill = "both", expand = True)

#Se agregan widets al Frame_1
L1 = tk.Label( Frame_1, text = "TEXTO EN FRAME 1", bg = "black",fg = "white" )
L1.pack(side = "top",expand = True, fill = "both")
L2 = tk.Label( Frame_1, text = "TEXTO EN FRAME 1", bg = "black",fg = "yellow" )
L2.pack(side = "top",expand = True, fill = "both")
L3 = tk.Label( Frame_1, text = "TEXTO EN FRAME 1", bg = "black",fg = "red" )
L3.pack(side = "top",expand = True, fill = "both")

#Se agregan widets al Frame_2
L4 = tk.Label( Frame_2, text = "TEXTO EN FRAME 2", bg = "white",fg = "black" )
L4.pack(side = "top",expand = True, fill = "both")
L5 = tk.Label( Frame_2, text = "TEXTO EN FRAME 2", bg = "white",fg = "blue" )
L5.pack(side = "top",expand = True, fill = "both")

#Se agregan widets al Frame_3
L6 = tk.Label( Frame_3, text = "TEXTO EN FRAME 3", bg = "yellow",fg = "black" )
L6.pack(side = "top",expand = True, fill = "both")
L7 = tk.Label( Frame_3, text = "TEXTO EN FRAME 3", bg = "yellow",fg = "green" )
L7.pack(side = "top",expand = True, fill = "both")

#Se ejecuta el "mainloop" que permite correr el codigo de la ventana correctamente
root.mainloop()
#Santiago Garcia Arango, 16 Enero 2020
# SE TRABAJA CON FORMA DE ORGANIZAR GUI TIPO GRID
#-------------------------------------------------------------------------------
#GRID: es como una matriz interna compuesta por filas y columnas

#IMPORTANTE:
#Hacer que columna o fila "N" tenga un peso de 1, es decir, que se lleve el espacio...
#...maximo, relativo de "1", con respectos a las otras columnas.
#tener en cuenta que por defecto, el peso es 0 para todas las columnas/filas.
#Tambien se puede configurar que el peso sea 2,3,4,etc...
#OJO: esto nos permite que al expandir programa, se expanda la columna/fila correctamente
#root.columnconfigure( N , weight = 1)
#root.rowconfigure( N , weight = 1)


#-------------------------------------------------------------------------------
#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("GRID")

#Se da un color de fondo predeterminado
root.configure( bg = "black" )

#Se configuran todas las columnas de trabajo con mismo peso, para facilidad al expandir
root.columnconfigure( 0, weight =1 )
root.columnconfigure( 1, weight =1 )
root.columnconfigure( 2, weight =1 )
root.columnconfigure( 3, weight =1 )
#Forma cool rapida de hacerlo: (a traves de tupla)
root.columnconfigure( (0,1,2,3), weight =1 )



#Se creea label para indicar que es la fila cero
#OJO: Ver "columnspan", para indicar que este widget ocupa multiples columnas
#OJO: ver color indicado de forma HEX
#OJO: ver "sticky" como forma de llevar fondo completo al tamanno del widget (north,south,east,west)
texto_0 = tk.Label( root, text = ".........ESTA ES LA FILA CERO..........",bg = "#00FFFF" )
texto_0.grid(row =0, column =0, columnspan = 4 , sticky = "nsew")

#Se crea label encargada de indicar que el usuario ingrese el nombre
texto_1 = tk.Label( root, text = "Ingrese su nombre: ", bg = "black", fg = "white" )
texto_1.grid(row =1, column =0 )

#Se crea label para luego interactuar con ella al tocar boton
texto_2 = tk.Label( root, text = " ", bg = "black", fg = "yellow" )
#Nota: columnspan o rowspan permiten hacer widgets de "grosor" de N columas o filas
texto_2.grid(row =2, column =0,columnspan = 3 )

#Se crea Entry Field (para ingresar info por el usuario)
#FUNDAMENTAL: crear "tk.StringVar()" para manejo de Entry fields
nombre_usuario = tk.StringVar()
entrada = ttk.Entry( root,width = 20, textvariable = nombre_usuario )
entrada.grid( row = 1, column =1 , sticky = "ew")
#OJO: truco interesante: hacer que el usuario ya tenga el "mouse" listo para escribir:
entrada.focus()

#Se crean dos botones, uno para imprimir algo en terminal y otro para salirse
#WARNING: "command" permite hacer funcion al tocar boton, pero NO se pone entre parentesis...
#... de lo contrario NO funcionaria al tocarla, sino al inicializar...
#NOTA: Se debe crear funcion del boton, antes de crearlo

def funcion_tocame():
    #Se cambia texto de label, con ayuda de "condigure()"
    #Ver forma de obtener info de Entry asociado al nombre...
    #...es a traves de la variable "nombre_usuario", llamando a "get()"
    texto_2.configure( text = "Gracias por tocarme {}".format(nombre_usuario.get()) )

#Importante: si queremos que boton "se agrande/amplie" con expandir ventan, aplicar "sticky"
b_1 = ttk.Button( root, text = "TOCAME" , command = funcion_tocame)
b_1.grid(row =1, column = 2, padx = (10,30), sticky = "ew")
#Mirar padx como "padding en x externo"
#Tambien existe ipadx comom "internal padding en x"

b_2 = ttk.Button(root, text = "SALIR", command = quit)
b_2.grid(row = 1, column = 3)
root.mainloop()
#Santiago Garcia Arango, 16 Enero 2020
#CORRER VENTANAS EN HIGH DEFINITION (HD)
#----------------------------------------------------------------------------------------
#Se efectua asi (Solo sirve en Windows 10):

#ESTO ES LO NUEVO:
#----------------------------------------------------------------------------------------
#Se intenta traer libreria de estilos visuales HD gracias al DPI Awareness
#(Correr esta linea de codigo al inicio)
#SIEMPRE CORRER LINEA EN "TRY", porque esta funcionalidad NO EXISTE en linux ni mac
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
#----------------------------------------------------------------------------------------
#Ahora lo siguiente es el mismo codigo del ejemplo anterior (comparar calidad visual)

#Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

#Se agrega estilo sencillo
font_1 = ("Verdana",12,"bold")
font_2 = ("Verdana",10)



#Se crea la ventana principal en donde se guardara la info y se mostrara todo
root = tk.Tk()

#Se agrega el titulo a la ventana de trabajo, para mostrar en la parte superior
root.title("GRID")

#Se da un color de fondo predeterminado
root.configure( bg = "black" )

#Se configuran todas las columnas de trabajo con mismo peso, para facilidad al expandir
root.columnconfigure( 0, weight =1 )
root.columnconfigure( 1, weight =1 )
root.columnconfigure( 2, weight =1 )
root.columnconfigure( 3, weight =1 )
#Forma cool rapida de hacerlo: (a traves de tupla)
root.columnconfigure( (0,1,2,3), weight =1 )



#Se creea label para indicar que es la fila cero
#OJO: Ver "columnspan", para indicar que este widget ocupa multiples columnas
#OJO: ver color indicado de forma HEX
#OJO: ver "sticky" como forma de llevar fondo completo al tamanno del widget (north,south,east,west)
texto_0 = tk.Label( root, text = ".........ESTA ES LA FILA CERO..........",bg = "#00FFFF", font = font_1)
texto_0.grid(row =0, column =0, columnspan = 4 , sticky = "nsew")

#Se crea label encargada de indicar que el usuario ingrese el nombre
texto_1 = tk.Label( root, text = "Ingrese su nombre: ", bg = "black", fg = "white", font =font_2 )
texto_1.grid(row =1, column =0 )

#Se crea label para luego interactuar con ella al tocar boton
texto_2 = tk.Label( root, text = " ", bg = "black", fg = "yellow", font =font_2 )
#Nota: columnspan o rowspan permiten hacer widgets de "grosor" de N columas o filas
texto_2.grid(row =2, column =0,columnspan = 3 )

#Se crea Entry Field (para ingresar info por el usuario)
#FUNDAMENTAL: crear "tk.StringVar()" para manejo de Entry fields
nombre_usuario = tk.StringVar()
entrada = ttk.Entry( root,width = 20, textvariable = nombre_usuario , font = font_2)
entrada.grid( row = 1, column =1 , sticky = "ew")
#OJO: truco interesante: hacer que el usuario ya tenga el "mouse" listo para escribir:
entrada.focus()

#Se crean dos botones, uno para imprimir algo en terminal y otro para salirse
#WARNING: "command" permite hacer funcion al tocar boton, pero NO se pone entre parentesis...
#... de lo contrario NO funcionaria al tocarla, sino al inicializar...
#NOTA: Se debe crear funcion del boton, antes de crearlo

def funcion_tocame():
    #Se cambia texto de label, con ayuda de "condigure()"
    #Ver forma de obtener info de Entry asociado al nombre...
    #...es a traves de la variable "nombre_usuario", llamando a "get()"
    texto_2.configure( text = "Gracias por tocarme {}".format(nombre_usuario.get()) )

#Importante: si queremos que boton "se agrande/amplie" con expandir ventan, aplicar "sticky"
b_1 = ttk.Button( root, text = "TOCAME" , command = funcion_tocame)
b_1.grid(row =1, column = 2, padx = (10,30), sticky = "ew")
#Mirar padx como "padding en x externo"
#Tambien existe ipadx comom "internal padding en x"

b_2 = ttk.Button(root, text = "SALIR", command = quit)
b_2.grid(row = 1, column = 3)
root.mainloop()
# SE CREAN COMBOBOXES
# ----------------------------------------------------------------------------------------
# Son los menus desplegables, que a su vez nos indican info importante de lo seleccionado...
# ...por el usuario. Es importante crearlas y acceder a lo que tienen en todo momento.
# Ver codigo para entender funcionamiento

# ----------------------------------------------------------------------------------------
# EJEMPLO:
# Programa que maneja 2 comboboxes al tiempo, donde la info del segundo depende de la seleccion del primero
# Luego, se obtiene info de ambos combobox y se muestra eleccion usuario en terminal
# IMPORTANTE VER FORMA DE OBTENER INFO DE SELECCION COMBOBOX...
# IMPORTANTE ENTENDER COMO EJECUTAR ACCION AL SELECCIONAR OPCION DE COMBOBOX...
# IMPORTANTE VER COMO RESETEAR VALOR POR DEFECTO (NULO) DE COMBOBOX.

# Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk

# Se intenta traer libreria de estilos visuales HD gracias al DPI Awareness
# SIEMPRE CORRER LINEA EN "TRY", porque esta funcionalidad NO EXISTE en linux ni mac
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Se crea ventana principal
root = tk.Tk()

# Se agrega titulo, geometria y Evitar redimensionar
root.title("COMBOBOXES")
root.geometry("1200x700")
root.resizable(0, 0)

# Se agrega estilo de labels
font = ("Verdana", 12)

# Se debe crear variable para manejo de inifo seleccionada en combobox 1 y combobox 2
# Siempre que se quiera acceder a esta variable (asociada a la seleccion), se debe llamar...
# ... a seleccion_combobox_1.get()   o     seleccion_combobox_2.get()
seleccion_combobox_1 = tk.StringVar(root)
seleccion_combobox_2 = tk.StringVar(root)

# Se crea texto para indicar lo que se debe elegir en combobox 1 y 2
texto_1 = tk.Label(root, text="Elija el barrio donde vive: ", font=font)
texto_1.grid(row=0, column=0, sticky="w")
texto_2 = tk.Label(root, text="Elija su CC favorito del barrio: ", font=font)
texto_2.grid(row=1, column=0, sticky="w")

# Se crea combobox 1
vector_barrios = ["Poblado", "Laureles", "Belen", "Envigado"]
menu_barrios = ttk.Combobox(root, textvariable=seleccion_combobox_1, values=vector_barrios, state="readonly")
menu_barrios.grid(row=0, column=1)

# Se crea combobox 2
menu_cc = ttk.Combobox(root, textvariable=seleccion_combobox_2, values=[], state="readonly")
menu_cc.grid(row=1, column=1)


# Se crea funcion que se encarga de manejar el item elegido en combobox 1
# Siempre colocar "event"...
# OJO: SIEMPRE que se desee llamar funcion al seleccionar info de combobox, se llama asi:
# ... NombreCombobox.bind("<<ComboboxSelected>>", NombreFuncionARealizar)  ---> ojo: llamar luego de definir funcion, sino es error
def modificar_combobox_2(event):
    # Se obtiene nombre de lo que se encuentra seleccionado actualmente en combobox1
    seleccion = seleccion_combobox_1.get()
    # Se agregan opciones del combobox 2 para que usuario pueda elegir segun primera eleccion de combobox 1
    if seleccion == "Poblado":
        menu_cc.config(values=["Santafe", "Oviedo", "El Tesoro", "Sandiego", "La Visitacion", "Del Este"])
        # OJO: de esta forma que evita que info erronea quede seleccionada en combobox (clear seleccion de combobox2)
        menu_cc.set("")
    elif seleccion == "Laureles":
        menu_cc.config(values=["Viva Laureles", "Unicentro", "La 70 Mall", "Mall Laureles"])
        # OJO: de esta forma que evita que info erronea quede seleccionada en combobox (clear seleccion de combobox2)
        menu_cc.set("")

    elif seleccion == "Belen":
        menu_cc.config(values=["La Mota", "Granvia Mall", "Los Molinos", "Mall Belen", "Arkadia", "Belensito Mall"])
        menu_cc.set("")

    elif seleccion == "Envigado":
        menu_cc.config(values=["Viva Envigado", "La Frontera Mall", "Sao Paulo", "Parque Envigado", "Mall San Lucas",
                               "City Plaza"])
        menu_cc.set("")


# OJO: ESTO DE ACA ABAJO ES LA MAGIA DE HACER ALGO AL SELECCIONAR...
# SIEMPRE QUE SE CREE FUNCION, SE INDICA QUE EL COMBOBOX REALIICE LA FUNCION ASI:
menu_barrios.bind("<<ComboboxSelected>>", modificar_combobox_2)


# Ahora creamos funcion que funcione al seleccionar combobox2, como registro de info total (de ambos)
def mostrar_info_al_seleccionar_combobox_2(event):
    # Se valida que el usuario haya elegido algo nuevo en combobox 2 (diferente a nulo)
    if menu_cc.current() != -1:
        # Se muestran dos formas de obtener info (una es seleccion y otra es index o posicion asociada al vector inicial de valores)
        seleccion_1 = seleccion_combobox_1.get()
        seleccion_1_index = menu_barrios.current()

        seleccion_2 = seleccion_combobox_2.get()
        seleccion_2_index = menu_cc.current()

        # Se elimina lo seleccionado en ambos combobox, para que no queden mostrandose erroneamente
        menu_cc.set("")
        menu_barrios.set("")
        # Se resetean las opciones del combobox2 a nulas
        menu_cc.config(values=[])
        # Se devuelve la info total de lo elegido por el usuario al elegir segundo combobox
        print("\nSELECCION USUARIO: ")
        print(" {}({}) __ {}({})".format(seleccion_1, seleccion_1_index, seleccion_2, seleccion_2_index))
# RECORDAR QUE ESTAS FUNCIONES SOLO CORREN SI SE DEFINE LA ACCION AL SELECCIONAR INFO (ASI:)
menu_cc.bind("<<ComboboxSelected>>", mostrar_info_al_seleccionar_combobox_2)

# Se ejecuta ventana de trabajo
root.mainloop()'''
# Santiago Garcia Arango, 17 Enero 2020
# MANEJO DE TKINTER MAS AVANZADO, CON PROGRAMACION ORIENTADA A OBJETOS
# ------------------------------------------------------------------------
'''
El objetivo de esta etapa es aprender a manejar correctamente Tkinter con ayuda
de las herramientas y logica enfocada a la Programacion Orientada a Objetos.
Esto nos permitira crear aplicaciones con mayores profundidades y capacidades,
manteniendo un orden basado en clases.
Ademas, se explicara la forma de aprovechar la herencia de Tkinter, para manejar
lo que habiamos manejado como "root", ahora como la clase principal, y las otras
clases seran las encargadas de llevar la info de las otras "ventanas" de la app.

# ------------------------------------------------------------------------

# Se intenta traer libreria de estilos visuales HD gracias al DPI Awareness
# SIEMPRE CORRER LINEA EN "TRY", porque esta funcionalidad NO EXISTE en linux ni mac
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk


# Se crea clase que reemplaza/genera el mismo efecto del "root", asi:
# Aprovechandonos de la herencia, al crear la clase, se hereda de tk.Tk, esto...
# ... tendra grandes beneficios, porque:
# 1. Se agrega funcionalidades y variables internas a la clase, que tk.Tk NO tienen.
# 2. Al llamar a algo que sea directamente de tk.Tk, lo busca en APP, y luego lo busca en tk.Tk...
# ...permitiendo facilitar el uso de esta funcionalidad de tkinter y a la vez, tener metodos/atributos extras.
class APP(tk.Tk):
    def __init__(self):#Inicializacion
        # OJO: Se debe inicializar no solamente APP, sino la inicializacion de tk.Tk, para garantizar la inicializacion...
        # ... correcta de de tkinter y su respectiva funcion "Tk".
        # Notar que antes haciamos root = tk.Tk() , ahora se hace lo mismo, a traves de inicializar la clase (mismo proceso).
        # Esto nos permitira almacenar todo en la APP, con ventajas enormes, que veremos mas adelante
        super().__init__()
        # NOTA: Esta inicializacion con super() --> de herencia de tk.Tk, es exctamente lo mismo que decir:
        # ... self = tk.Tk()
        # ... la razon de esto es porque toda inicializacion que pase en objeto, se procesa en "self"!!!
        # es decir, de ahora en adelante, self se puede ver como la misma ventana que siempre hemos llamado root = tk.Tk()
        # Ahora, aprovechandose de esta herencia e inicializacion, se puede llamar self.________ como si self fuera root.
        self.title("TEST")
        self.state("zoomed")

        L1 = tk.Label(self, text="PRIMER LABEL EN VENTANA CON POO APLICADA", font=("Times New Roman", 14, "bold"),
                      bg="#00FFFF", fg="blue")
        L1.pack(expand=True, fill="both")


# Se crea clase... (a la vez se esta creando la ventana asociada, gracias a la herencia de tk.Tk)
# NOTA: luego de crear clase, tambien se pueden ejecutar funciones de tk.Tk, como  se ve abajo (por si se necesita, es bueno saberlo)
root = APP()

# se ejecuta el maniloop para que APP (que contiene toda la info de tk.Tk(), corra correctamente y se muestre ventana con info)
root.mainloop()'''
# MANEJO DE TKINTER MAS AVANZADO, CON PROGRAMACION ORIENTADA A OBJETOS (FRAMES)
# COOL: poder hacer que al presionar "Enter", suceda algo (lo que sea)
# ------------------------------------------------------------------------
'''
Luego de ver codigo "1", con explicacion de metodologia para POO con tkinter,
se continua metodologia para extender a nuevos Frames en tkinter con POO.
IMPORTANTE:
Recordemos que los Frames siempre tienen una estructura de este tipo:
F = tk.Frame( root )
Es decir, esto nos dice dos cosas importantes a tener en cuenta al crear frames con POO:
1. Nuestros Frames creados en clases, deberan heredar todo desde tk.Frame
2. Nuestros Frames creados en clases, deben recibir como parametros, un "contenedor",
el cual es llamado normalmente root, pero puede ser realmente otros frames tambien.
Estos dos puntos se explican abajo en el ejemplo practico de estas cosas a tener en cuenta

# ------------------------------------------------------------------------
# EJEMPLO: Se crea app con explicacion de Frames, basandose en POO


# Se ejecuta intento de trabajar ventanas en HD, solo disponible en Windows (por eso el "try-except")
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Se importan librerias de trabajo
import tkinter as tk
from tkinter import ttk
import tkinter.font as font


# Siguiendo info del codigo anterior, se ejecuta igualmente... (si no se entiende ver codigo para explicacion)
class APP(tk.Tk):
    # OJO: Notar que pasamos "*args" y "**kwargs", porque podrian ser necesarios (recordar pasarlos a inicializacion de tk.Tk)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se aprovecha que "self" ya es la ventana principal y se agrega titulo respectivo
        self.title("TKINTER CON FRAME Y POO")
        # Se busca que Ventana se mantenga central y correcta a traves de:
        self.columnconfigure(0, weight=1)
        # Se crea Frame_1, la cual debemos logicamente, indicar donde se debe posicionar (en este caso en self, osea "root")
        # OJO: Recordar que no solamente se crea, sino que se debe posicionar (en este caso con pack()  )
        self.F_1 = Frame_1(self)
        self.F_1.pack(expand=True, fill="both")
        # FORMA DE DAR FUNCION DEL BOTON, CON ENTER, SIEMPRE COLOCAR "bindings" en ROOT (tk.Tk)
        # IMPORTANTE: Al agregar bindings (acciones como las de enter), SE EXIGE AGREGAR "*args" a funcion, para que entienda el evento...
        # ... gracias la funcion, con parametros disponible, de lo contrario, no funciona el enter como comando de activacion
        # Este bind es para llamar a funcion "saludarme", ubicada en clase de F_1, como metodo (encargado de cambiar Label) al presionar "Enter"
        self.bind("<Return>", self.F_1.saludarme)
        # Este bind es para llamar a funcion "saludarme", ubicada en clase de F_1, como metodo (encargado de cambiar Label) al presionar "Enter Numerico"
        self.bind("<KP_Enter>", self.F_1.saludarme)


# OJO( CREACION DE FRAMES):
# Se crean como clases con herencia de tk.Frame (para acceder inmediatamente a la clase Frame)
# NOTA: Si bien creamos Frame, recordemos que hace falta "llamarla", de lo contrario, no se crea ni se hace efectiva
class Frame_1(tk.Frame):
    # Se inicializan, recibiendo de parametro self y container (el container es en donde esta ubicado el Frame)
    # Recordemos que este container sera entonces un parametro que debemos incluir, al llamar a clase.
    # Se pueden incluir los *args y **kwargs, como parametros extra disponibles
    def __init__(self, container, *args, **kwargs):
        # Para inicializar Frame y que se entienda la clase como un Frame, tambien se inicializa desde la herencia:
        # NOTA: NO olvidar pasar el parametro tambien, de lo contrario, no se comprende donde localizar el Frame creado
        # Luego de hacer esto, recordar que "self" es equivalente a decir el Frame_1, que es en donde agregaremos widgets
        super().__init__(container, *args, **kwargs)
        self.configure(bg="yellow", padx=50, pady=10)

        # Agregamos Widgets, con la ventaja de poder agregarlos en "self"(Frame_1)-->tk.Frame , que a su vez, estara en root(APP)-->tk.Tk
        # Variable para texto del usuario, el objetivo es poder obtener la info de Entry (E_1)
        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label(self, text="MI PRIMER FRAME CON POO Y TKINTER", font=("Times New Roman", 14, "bold"),
                       bg="yellow", fg="blue")
        L_1.grid(row=0, column=0, columnspan=4, sticky="n")
        L_2 = tk.Label(self, text="Ingrese Nombre: ", font=("Times New Roman", 12), bg="yellow")
        L_2.grid(row=1, column=0, sticky="w")

        # Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        E_1 = ttk.Entry(self, textvariable=self.entrada_usuario)
        E_1.focus()
        E_1.grid(row=1, column=1, columnspan=2, padx=(0, 10))
        # OJO: mirar B_1, es boton, que su command activa un metodo interno de la clase. Esto es maravilloso.
        # esto nos permitira acceder a metodos en clases, al interactuar con widgets. Es mas organizado segun clase (Frame)
        B_1 = ttk.Button(self, text="SALUDARME", command=self.saludarme)
        B_1.grid(row=1, column=3, sticky="e")

        # OJO: este label es variable, por lo que lo creamos con "self.", para poder acceder a el con metodos de la clase
        self.L_3 = tk.Label(self, textvariable="", font=("Times New Roman", 12, "bold"), bg="yellow")
        self.L_3.grid(row=2, column=0, columnspan=4, sticky="nsew")

    # OJO: Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    # ...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure(text="Hola {}.".format(self.entrada_usuario.get()))


# Se crea APP como tal (aprovechandonos de la clase creada)
root = APP()

# Cambiar "font" por defecto a todo (ojo con forma de importar libreria arriba)
font.nametofont("TkDefaultFont").configure(size=12, underline=True)

# Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas
root.mainloop()'''
# Reconocimiento facial
import cv2
import os

dataPath = 'D:\Ciclo 4\PI 2\Reconocimiento facial'  # Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

# face_recognizer = cv2.face.EigenFaceRecognizer_create()
# face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
# face_recognizer.read('modeloEigenFace.xml')
# face_recognizer.read('modeloFisherFace.xml')
face_recognizer.read('modeloLBPHFace.xml')

# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('Video.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
        '''
        # EigenFaces
        if result[1] < 5700:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

        # FisherFace
        if result[1] < 500:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        '''
        # LBPHFace
        if result[1] < 70:
            cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
