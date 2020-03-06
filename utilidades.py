#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:50:20 2020

@author: raquel
"""
#importamos las librerías pandas y random
import pandas as pd 
import random 

#llamamos a las clases Medica, Paciente, Especialidad, Enfermera y Recepcionista
from medica import Medica
from paciente import Paciente
from especialidad import Especialidad
from enfermera import Enfermera
from recepcionista import Recepcionista
from medicamento import Medicamento

class Utilidades():
    def crea_password(self,nombre,apell,telf): #tendra como inputs el nombre, apellido y telf de la persona
        password=nombre[0].lower()+nombre[1]+apell[0].lower()+apell[1]+telf[-2]+telf[-1] #comprobar si hay espacios entre los numeros de telefono
        return password
        
    def lectura(self,especialidad,info,medicina): #tiene como parametros los dos archivos .csv
        especialidad=pd.read_csv(especialidad,sep=';',encoding='latin-1') #lectura para el vocabulario español
        info=pd.read_csv(info,sep=';',encoding='latin-1')
        medicina=pd.read_csv(medicina,sep=';',encoding='latin-1')
        
        dic_especialidades={} #creo diccinarios vacios
        dic_medicas={} 
        dic_pacientes={}
        dic_enfermeras={}
        dic_recepcionistas={}
        dic_medicamentos={}
        
        #CREACIÓN DICCIONARIO ESPECIALIDADES
        for row in especialidad.itertuples(): #recorro el archivo
            dic_especialidades[row.Codigo]=Especialidad(row.Codigo,row.Nombre) #palabre clave es el nombre de la especialidad y los elementos son el nombre y el código
        
        #CREACCION DICCIONARIO PACIENTES, MÉDICAS, ENFERMERAS Y RECEPCIONISTAS
        grupo_sanguineo=('AB+','AB-','A+','A-','B+','B-','0+','0-') #tupla  con los grupos sanguineos
        cat=[] #lista vacía donde iremos introduciendo las categorias de las enfermeras
        jefas=3
        practicantes=5
        
        turnos=['1:matutino','2:verspertino','3:nocturno','4:rotatorio'] #turnos de recepcionaistas
        turno=0
        
        id_m=0 #identificadores medica, pacientes, enfermeras y recepcionistas
        id_p=0        
        id_e=0
        id_r=0 
        espec=0
        
        for row in info.itertuples(): #recorro el archivo .csv
            #establezco 5 condiciones para diferenciar entre los 5 tipos que hay en el archivo
            #medicas
            if row.Tipo=='M':
                id_m+=1 #voy sumando 1 a cada interacción de la condición
                nombre=row.Nombre+' '+row.Apellido #guardo en la variable nombre tanto el Nombre como el Apellido de la persona separados por un espacio
                password=self.crea_password(row.Nombre,row.Apellido,row.Telefono) 
                #distribución de las espcecialidades en orden 
                if espec<len(dic_especialidades.keys()): #que recorro el diccionario
                    especialidad=list(dic_especialidades.keys())[espec]
                    espec+=1 #le voy sumando uno y va cambiando la posición que le vpy asignando del diccionario
                else:
                    espec=0 #una vez que haya recorrido todo el diccionario pongo la variable en cero para que vuela a empezar
                    especialidad=list(dic_especialidades.keys())[espec]
                    espec=1
                m=Medica(id_m,nombre,row.Direccion,row.Ciudad,row.CP,row.Telefono,row.Email,especialidad,password) #objeto de la clase Medica con sus atributos correpondientes
                dic_medicas[id_m]=m #identificador como clave y objeto con toda la información como elemento
            #pacientes
            elif row.Tipo=='P': #mismo procedimiento para pacientes
                id_p+=1
                nombre=row.Nombre+' '+row.Apellido
                p=Paciente(id_p,nombre,row.Direccion,row.Ciudad,row.CP,row.Telefono,row.Email,random.choice(grupo_sanguineo))
                dic_pacientes[id_p]=p
            #enfermeras
            elif row.Tipo=='E':
                id_e+=1
                nombre=row.Nombre+' '+row.Apellido
                password=self.crea_password(row.Nombre,row.Apellido,row.Telefono)                
                #repartir las categorias entre las enfermeras
                categorias=['P:practicante','J:enfermera junior','M:enfermera senior','JE:jefa de enfermeras'] #categorias de enfermeras
                #asignación de las categorías de las enfermeras, solo puede haber 3 jefas y 5 practicantes
                if len(cat)<jefas*len(categorias): #pongo de límite hasta las 12 posiciones ya que ahi es cuando se cumple que haya 3 jefas
                    for i in range(len(categorias)):
                        cat.append(categorias[i]) #voy añadiendo a una lista vacía las diferentes categorías y una vez que la tenga completa iré rellenando el diccionario con lasdiferentes posiciones de esta lista
                elif jefas*len(categorias)<len(cat)<practicantes*len(categorias): #pongo de limite 20 posicinoes ya que así ya habrá 5 practicantes
                    categorias.remove('JE:jefa de enfermeras') #elemino la categoría jefa para que no me la siga añadiendo a la lista
                    for i in range(len(categorias)):
                        cat.append(categorias[i])
                else: 
                    categorias.remove('JE:jefa de enfermeras')
                    categorias.remove('P:practicante') #vuelvo a eliminar jefa y tamb´ién practicante para que solo me añada las restantes que queden
                    for i in range(len(categorias)):
                        cat.append(categorias[i])
                e=Enfermera(id_e,nombre,row.Direccion,row.Ciudad,row.CP,row.Telefono,row.Email,password,cat[id_e-1])
                dic_enfermeras[id_e]=e
            #recepcionistas
            elif row.Tipo=='R':
                id_r+=1
                nombre=row.Nombre+' '+row.Apellido
                password=self.crea_password(row.Nombre,row.Apellido,row.Telefono)                
                if turno<4: #tengo 4 opciones de turno diferente, las posiciones de la lista empiezan en cero
                    #voy asignando los 4 turnos disponibles que hay y una vez que llegue a 4, pongo la varible como cero y que me vuelva a recorrer la lista
                    r=Recepcionista(id_r,nombre,row.Direccion,row.Ciudad,row.CP,row.Telefono,row.Email,turnos[turno],password)
                    turno+=1
                elif turno>=4:
                    turno=0
                    r=Recepcionista(id_r,nombre,row.Direccion,row.Ciudad,row.CP,row.Telefono,row.Email,turnos[turno],password)
                    turno=1
                dic_recepcionistas[id_r]=r
            #hospital
            elif row.Tipo=='H': #informacion hospital
                lista_hosp=[row.Nombre,row.Direccion,row.Ciudad,row.CP,row.Telefono] #lista con la información referente al hospital
        
        for row in medicina.itertuples():
            dic_medicamentos[row.Codigo]=Medicamento(row.Codigo,row.Principio_Activo,row.Marca,row.Laboratorio)
                
        return dic_especialidades,dic_medicas,dic_pacientes,dic_enfermeras,dic_recepcionistas,dic_medicamentos,lista_hosp #el método me devuelve los 3 diccionarios más la lista de info hospital
