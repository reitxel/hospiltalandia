#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:49:22 2020

@author: raquel
"""
from diagnostico import Diagnostico

class FichaRevision():
    def __init__(self,_codigo,_fecha):
        self.set_codigo(_codigo)
        self.set_fecha(_fecha)
        self.__diag=[]#lista diagnostico vacía, le iré añadiendo después objetos del tipo diagnostico, no se considera atributo
        
    def set_codigo(self,_codigo):
        self.__codigo=_codigo
    def set_fecha(self,_fecha):
        self.__fecha=_fecha
    def set_diag(self,_diag,_med,_espec):
        self.__diag=_diag
        
    def get_codigo(self):
        return self.__codigo
    def get_fecha(self):
        return self.__fecha
    def get_diag(self):
        return self.__diag
        
    codigo=property(get_codigo,set_codigo)
    fecha=property(get_fecha,set_fecha)
    diag=property(get_diag,set_diag)
    
    def muestra_datos(self):
        return [self.codigo,self.fecha,self.muestra_diag()]
    
    def muestra_diag(self):
        llista_diag=[]
        for i in self.diag:
            llista_diag.append(i.muestra_datos())
        return llista_diag
    
    def tiene_diagnostico(self,espec,med):  #me crea un objeto del tipo diagnostico y me lo añade a la lista diag con todos us atributos
        d=Diagnostico(espec,None,None,med)
        self.diag.append(d)
    
    
       
    
    