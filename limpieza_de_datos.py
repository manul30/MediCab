# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:59:13 2021

@author: Manuel
"""

import pandas as pd
import random
import numpy as np
import datetime
import dateutil.relativedelta

DF=pd.read_csv("data.csv")

X=pd.DataFrame(DF[['Apellido','Nombre','Codigo','Edad','Sexo']])

correo='manuel.carita@utec.edu.pe'

X['Correo']=correo

X.iloc[104,5]='jairo.custodio@utec.edu.pe'


X=X.dropna()

X['Codigo']=X['Codigo'].astype(int)

X['Estatura']=0

X['HPeso']=0
X['HPeso']=X['HPeso'].astype('object')

X['HFecha']=0
X['HFecha']=X['HFecha'].astype('object')


X['HOx']=0
X['HOx']=X['HOx'].astype('object')


X['HFP']=0
X['HFP']=X['HFP'].astype('object')

X['IMC']=0
X['IMC']=X['IMC'].astype('object')

X['Temp']=0

X.reset_index(level=0,inplace=True)

X=X.drop(['index'], axis=1)

hoy=datetime.datetime.now()
#datetime.datetime(year, month, day)
inicio= hoy - dateutil.relativedelta.relativedelta(months=3)

for i in range(len(X)):
    aux1=[]
    aux2=[]
    aux3=[]
    aux4=[]
    for j in range(11):
        aux1.append(random.randint(50,80)+random.random()*random.randint(-5,5))
        prue=inicio + datetime.timedelta(seconds= int((hoy - inicio).total_seconds() * random.random()))
        aux2.append(prue)
        aux3.append(random.randint(92,102)) 
        aux4.append(random.randint(50,110))
        
    E=random.randint(150,180)
    X.at[i,'HPeso']=aux1
    aux2.sort()
    X.at[i,'HFecha']=[i.strftime("%d/%m/%Y") for i in aux2]
    X.at[i,'HOx']=aux3
    X.at[i,'HFP']=aux4
    X.at[i,'Estatura']=E
    X.at[i,'IMC']=list(np.array(X.at[i,'HPeso'])/(E/100)**2)
    X.at[i,'Temp']=random.randint(35,38)+random.randint(-1,1)*random.random()
    
X.to_csv('Base_de_datos.csv')


    













