#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:51:05 2020

@author: raquel
"""

class RecetaMedica():
    def __init__(self,_medicamento,_dosis):
        self.set_dosis(_dosis)
        self.set_medicamento(_medicamento)
        
    def set_dosis(self,_dosis):
        self.__dosis=_dosis
    def set_medicamento(self,_medicamento):
        self.__medicamento=_medicamento
    
    def get_dosis(self):
        return self.__dosis
    def get_medicamento(self):
        return self.__medicamento
    
    dosis=property(get_dosis,set_dosis)
    medicamento=property(get_medicamento,set_medicamento)
    
    def muestra_datos(self):
        return [self.medicamento,self.dosis]
    
    
