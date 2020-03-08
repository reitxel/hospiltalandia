#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:50:28 2020

@author: raquel
"""
from derivadaciente import DerivaPaciente
from recetas import RecetaMedica

class Diagnostico():
    def __init__(self,_especialidad,_enfermedad,_observaciones,_nommed,_derivado=False):#defino aqui el boleano como false para que asi lo pueda modificar luego
        self.set_especialidad(_especialidad)
        self.set_enfermedad(_enfermedad)
        self.set_observaciones(_observaciones)
        self.__receta=[] #lista con recetas medicas
        self.set_nommed(_nommed)
        self.set_deriva=[]
        self.set_derivado(_derivado)
        
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
    def set_deriva(self,_deriva):
        self.__deriva=_deriva
    def set_derivado(self,_derivado):
        self.__derivado=_derivado
    
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
    def get_deriva(self):
        return self.__deriva
    def get_derivado(self):
        return self.__derivado
    
    especialidad=property(get_especialidad,set_especialidad)
    enfermedad=property(get_enfermedad,set_enfermedad)
    observaciones=property(get_observaciones,set_observaciones)
    receta=property(get_receta,set_receta)
    nommed=property(get_nommed,set_nommed)
    deriva=property(get_deriva,set_deriva)
    derivado=property(get_derivado,set_derivado)
    
    def muestra_datos(self):
        return [self.especialidad,self.enfermedad,self.observaciones,self.nommed]
    
    def DerivaP(self,nommed,fecha,espe):#creo el objeto de derivacion del paciente
        deriv=DerivaPaciente[nommed,fecha,espe]
        return deriv
    def gen_recep(self,medic,dosis):
        recet=RecetaMedica[medic,dosis]
        return recet
    def consulta_med:# mirar si existeix especialidat aixo no crec que serveixi la veritat
        
    def consulta_espe#aixo igual que 
        