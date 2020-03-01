#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:47:58 2020

@author: raquel
"""
from datos import Datos #hereda de la clase Datos

class Medica(Datos):
    def __init__(self,_id_num,_nombre,_direccion,_ciudad,_cp,_telefono,_email,_especialidad,_password):
        super().__init__(_nombre,_direccion,_ciudad,_cp,_telefono,_email) #llamada a los atributos del constructor de la clase de la que hereda
        self.set_id_num(_id_num)
        self.set_especialidad(_especialidad)
        self.set_password(_password)
        self.__pacrev=[]#no atendidos
        self.__pacnorev=[]#revision pendiente
    
    def set_id_num(self,_id_num):
        self.__id_num=_id_num
    def set_especialidad(self,_especialidad):
        self.__especialidad=_especialidad
    def set_password(self,_password):
        self.__password=_password
    def set_pacrev(self,_pacrev):
        self.__pacrev=_pacrev
    def set_pacnorev(self,_pacnorev):
        self.__pacnorev=_pacnorev

    def get_id_num(self):
        return self.__id_num
    def get_especialidad(self):
        return self.__especialidad
    def get_password(self):
        return self.__password
    def get_pacrev(self):
        return self.__pacrev
    def get_pacnorev(self):
        return self.__pacnorev
    
    id_num=property(get_id_num,set_id_num)
    especialidad=property(get_especialidad,set_especialidad)
    password=property(get_password,set_password)
    pacrev=property(get_pacrev,set_pacrev)
    pacnorev=property(get_pacnorev,set_pacnorev)
    
    def muestra_datos(self):
        nombre,direccion,ciudad,cp,telefono,email=self.obtener_datos() #llamada al método de la clase de la que hereda y guardando lo que devulve en sus respectivas variables
        return [self.id_num,nombre,direccion,ciudad,cp,telefono,self.especialidad] 