#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:52:51 2020

@author: raquel
"""

class Medicamento(object):
    def __init__(self,_codigo,_princ_activ,_marca,_laboratorio):
        self.set_codigo(_codigo)
        self.set_princ_activ(_princ_activ)
        self.set_marca(_marca)
        self.set_laboratorio(_laboratorio)
        
    def set_codigo(self,_codigo):
        self.__codigo=_codigo
    def set_princ_activ(self,_princ_activ):
        self.__princ_activ=_princ_activ
    def set_marca(self,_marca):
        self.__marca=_marca
    def set_laboratorio(self,_laboratorio):
        self.__laboratorio=_laboratorio
        
    def get_codigo(self):
        return self.__codigo
    def get_princ_activ(self):
        return self.__princ_activ
    def get_marca(self):
        return self.__marca
    def get_laboratorio(self):
        return self.__laboratorio
    
    codigo=property(get_codigo,set_codigo)
    princ_activ=property(get_princ_activ,set_princ_activ)
    marca=property(get_marca,set_marca)
    laboratorio=property(get_laboratorio,set_laboratorio)

    def muestra_datos(self):
        return [self.codigo,self.nombre]

