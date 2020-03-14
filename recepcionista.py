#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:47:29 2020

@author: raquel
"""
from datos import Datos

class Recepcionista(Datos):
    def __init__(self,_id_num,_nombre,_direccion,_ciudad,_cp,_telefono,_email,_turno,_password):
        super().__init__(_nombre,_direccion,_ciudad,_cp,_telefono,_email)
        self.set_id_num(_id_num)
        self.set_turno(_turno)
        self.set_password(_password)
        
    def set_id_num(self,_id_num):
        self.__id_num=_id_num
    def set_turno(self,_turno):
        self.__turno=_turno
    def set_password(self,_password):
        self.__password=_password
        
    def get_id_num(self):
        return self.__id_num
    def get_turno(self):
        return self.__turno
    def get_password(self):
        return self.__password
    
    id_num=property(get_id_num,set_id_num)
    turno=property(get_turno,set_turno)
    password=property(get_password,set_password)
    
    def muestra_datos(self):
        nombre,direccion,ciudad,cp,telefono,email=self.obtener_datos()
        return [self.id_num,nombre,direccion,ciudad,cp,telefono,email,self.turno]
    
    def informa(self,nom,dic_pacientes): #método que me informa del paciente que especifique por nombre, similar a 'mpaciente' de la práctica anterior
        lista_pacientes=[]
        for i in dic_pacientes: 
            if nom in dic_pacientes[i].regresa_nombre():
                lista_pacientes.append(dic_pacientes[i])
        return lista_pacientes

    
    def altas(self,dic,obj,ident): #mirar cuando aplicamos si me acepta tantos parametros
        dic[ident]=obj
