#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:50:28 2020

@author: raquel
"""

class Diagnostico():
    def __init__(self,_especialidad,_enfermedad,_observaciones,_nommed):
        self.set_especialidad(_especialidad)
        self.set_enfermedad(_enfermedad)
        self.set_observaciones(_observaciones)
        self.__receta=[] #lista con recetas medicas
        self.set_nommed(_nommed)
        
    def set_especialidad(self,_especialidad):
        self.__especialidad=_especialidad
    def set_enfermedad(self,_enfermedad):
        self.__enfermedad=_enfermedad
    def set_observaciones(self,_observaciones):
        self.__observaciones=_observaciones
    def set_receta(self,_receta):
        self.__receta=_receta
    def set_nommed(self,_nommed):
        self.__nommed=_nommed
    
    def get_especialidad(self):
        return self.__especialidad
    def get_enfermedad(self):
        return self.__enfermedad
    def get_observaciones(self):
        return self.__observaciones
    def get_receta(self):
        return self.__receta
    def get_nommed(self):
        return self.__nommed
    
    especialidad=property(get_especialidad,set_especialidad)
    enfermedad=property(get_enfermedad,set_enfermedad)
    observaciones=property(get_observaciones,set_observaciones)
    receta=property(get_receta,set_receta)
    nommed=property(get_nommed,set_nommed)
    
    def muestra_datos(self):
        return [self.especialidad,self.enfermedad,self.observaciones,self.nommed]