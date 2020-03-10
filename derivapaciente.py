#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:53:44 2020

@author: raquel
"""

class DerivaPaciente():
    def __init__(self,_nommed,_fecha,_especialidad):
        self.set_nommed(_nommed)
        self.set_fecha(_fecha)
        self.set_especialidad(_especialidad)
    
    def set_nommed(self,_nommed):
        self.__nommed=_nommed
    def set_fecha(self,_fecha):
        self.__fecha=_fecha
    def set_especialidad(self,_especialidad):
        self.__especialidad=_especialidad
    
    def get_nommed(self):
        return self.__nommed
    def get_fecha(self):
        return self.__fecha
    def get_especialidad(self):
        return self.__especialidad
    
    nommed=property(get_nommed,set_nommed)
    fecha=property(get_fecha,set_fecha)
    especialidad=property(get_especialidad,set_especialidad)