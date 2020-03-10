#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:50:37 2020

@author: raquel
"""

class Especialidad():
    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre
    
#    def set_codigo(self,_codigo):
#        self.__codigo=_codigo
#    def set_nombre(self,_nombre):
#        self.__nombre=_nombre
#    
#    def get_codigo(self):
#        return self.__codigo
#    def get_nombre(self):
#        return self.__nombre
#    
#    codigo=property(get_codigo,set_codigo)
#    nombre=property(get_nombre,set_nombre)
    
    def regresa_nombre(self): #unico método que devuelve ambos atributos
        return self.nombre
    def muestra_datos(self):
        return [self.nombre,self.codigo]