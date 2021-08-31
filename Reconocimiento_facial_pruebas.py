#Codigo para hacer videos OPEN CV
"""
import cv2
captura=cv2.VideoCapture('videoSalida.avi')
#0 no tengo nada
#salida=cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
#Numero de imagenes por segundo"20"
while(captura.isOpened()):
    ret, imagen=captura.read()
    #Si manda imagen True si no manda imagen False
    if(ret==True):
        cv2.imshow('video',imagen)#Video mostrar
        #salida.write(imagen)
        if cv2.waitKey(30) & 0xFF==ord('s'):#OxFF(64 BITS COMPUTADORA) y teclas para parar
            #1 para tiempo de procesamiento
            break
    else:break
captura.release()#Finalizar captura
#salida.realese()
cv2.destroyAllWindows()
"""
#DETECCION DE ROSTROS
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
faceClassif=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Clasificador
while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#Tranformamos en escala a grises
    faces=faceClassif.detectMultiScale(gray,1.3,5)
#scaleFactor=1.1,minNeighbors=5,,minSize=(175,175),maxSize=(300,300))
#Reduccion de imagen scaleFactor(Piramide de imagenes)
# minNeighbors: Numero minimo de rectangulos para detectar un rostro
#Valores muy bajos (falsos positivos)
# minSize tamaño minimo del objeto
# maxSize tamaño maximo del objeto
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




