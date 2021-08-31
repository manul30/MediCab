# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:54:20 2021

@author: Manuel
"""

import pandas as pd
import numpy as np
import datetime
import random as r

X=pd.DataFrame()
areas=['ANESTESIOLOGIA',
'CIRUGÍA GENERAL Y DIGESTIVA',
'LABORATORIOS CLINICOS',
'CARDIOLOGIA',
'CIRUGÍA ORTOPEDICA Y TRAUMATOLOGIA',
'RADIODIAGNÓSTICO',
'CUIDADOS INTENSIVOS',
'DERMATOLOGIA',
'FARMACIA',
'DIGESTIVO',
'GINECOLOGÍA Y OBSTETRICIA',
'MEDICINA PREVENTIVA',
'HEMATOLOGIA',
'OFTALMOLOGIA',
'MEDICINA INTERNA',
'OTORRINOLARIONGOLOGIA',
'NEFROLOGIA',
'UROLOGIA',
'NEUMOLOGIA',
'ONCOLOGIA',
'PEDIATRIA/NEONATOLOGIA',
'REHABILITACION',
'URGENCIAS']

nombre=['Laura','Diego','Martin','Sandra','Federico','Luis']
apellido=['Martinez','Garcia','Yamamoto','Paredes','Sanchez','Quispe','Altamirano','Rodriguez','Lopez','Diaz']

doctor=[r.choice(nombre)+' '+r.choice(apellido)+' '+r.choice(apellido) for i in range(10)]

sede={'Clinica Good Hope':'AV. MALECON BALTA N° 956, MIRAFLORES, LIMA, LIMA','Clinica Los Andes':'CALLE ASUNCION N° 177, MIRAFLORES, LIMA, LIMA','Clinica Miraflores':'AV. JOSE ANTONIO ENCINAS N° 141, MIRAFLORES, LIMA, LIMA','Clinica Neuroquirugica Alvarez':'AV. ALFREDO BENAVIDES N° 2965, MIRAFLORES, LIMA, LIMA','CLinica Maison de Sante Del Este':'AV. PROLONGACIÓN ALFREDO BENAVIDES N° 5362 URB. LAS GARDENIAS, SANTIAGO DE SURCO, LIMA, LIMA','Clinica Padre Luis Tezza':'AV. EL POLO N° 570, SANTIAGO DE SURCO, LIMA, LIMA','Clinica San Pablo Sede Surco':'AV. EL POLO N° 789, SANTIAGO DE SURCO, LIMA, LIMA'}


ax=str(datetime.datetime.now()).split()[0].split('-')
año,mes,dia=ax

X['Doctor']=[r.choice(doctor) for i in range(500)]
X['Area']=[r.choice(areas) for i in range(500)]
X['Sede']=[r.choice(list(sede.keys())) for i in range(500)]
X['Dir']=[sede[i] for i in X['Sede']]


X.to_csv('citas.csv')














