#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:48:00 2020

@author: raquel
"""
from datos import Datos
from fichas import FichaRevision
import random
#relacion con paciente

class Enfermera(Datos):
    def __init__(self,_id_num,_nombre,_direccion,_ciudad,_cp,_telefono,_email,_password,_categoria):
        super().__init__(_nombre,_direccion,_ciudad,_cp,_telefono,_email)
        self.set_id_num(_id_num)
        self.set_password(_password)
        self.set_categoria(_categoria)
        
    def set_id_num(self,_id_num):
        self.__id_num=_id_num
    def set_password(self,_password):
        self.__password=_password
    def set_categoria(self,_categoria):
        self.__categoria=_categoria
        
    def get_id_num(self):
        return self.__id_num
    def get_password(self):
        return self.__password
    def get_categoria(self):
        return self.__categoria
    
    id_num=property(get_id_num,set_id_num)
    password=property(get_password,set_password)
    categoria=property(get_categoria,set_categoria)
    
    def muestra_datos(self):
        nombre,direccion,ciudad,cp,telefono,email=self.obtener_datos()
        return [self.id_num,nombre,direccion,ciudad,cp,telefono,email,self.categoria]
    
    def asigna_revision(self,p,fecha,dic_medicas):
        revmed=p.muestra_revisiones()
        #revmed=p.revmed()
        lista_meds=[]
        lista_meds2=[]
        if len(revmed)==0: #si la lista esta vacia quiere decir que no hay revisiones para ese paciente
            for i in dic_medicas:
                if 'Médico de familia' in dic_medicas[i].muestra_datos():
                    lista_meds.append(dic_medicas[i].regresa_nombre())
            med=random.choice(lista_meds)
            revmed=p.tiene_revision(len(revmed)+1,fecha,med,'Médico de Familia')
        else:
            ultima_rev=revmed[-1] #revision anterior? pero tener en cuanta entre listas co cosas y una lista de objetos
            diag=ultima_rev[-1]
            especialidad=diag[0][0]
            for i in dic_medicas:
                if especialidad in dic_medicas[i].muestra_datos():
                    lista_meds2.append(dic_medicas[i].regresa_nombre())
            med=lista_meds2[0]
            revmed=p.tiene_revision(len(revmed)+1,fecha,med,especialidad)
            #miramos la revision anterior
            #codigo se forma secuencial, uno mas que el anterior
            #especialidad igual que la anterior
            #nombre del medico seraw el primero que aparezca con tal especialidad
        return revmed 
    
