#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:51:02 2020

@author: raquel
"""

class Datos(object): #object o no poner nada significa que la clase no hereda de nada
    def __init__(self,_nombre,_direccion,_ciudad,_cp,_telefono,_email): #creación del constructor con sus atributos 
        self.set_nombre(_nombre)
        self.set_direccion(_direccion)
        self.set_ciudad(_ciudad)
        self.set_cp(_cp)
        self.set_telefono(_telefono)
        self.set_email(_email)
        
    def set_nombre(self,_nombre):
        self.__nombre=_nombre
    def set_direccion(self,_direccion):
        self.__direccion=_direccion
    def set_ciudad(self,_ciudad):
        self.__ciudad=_ciudad
    def set_cp(self,_cp):
        self.__cp=_cp
    def set_telefono(self,_telefono):
        self.__telefono=_telefono
    def set_email(self,_email):
        self.__email=_email
        
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_ciudad(self):
        return self.__ciudad
    def get_cp(self):
        return self.__cp
    def get_telefono(self):
        return self.__telefono
    def get_email(self):
        return self.__email
    
    nombre=property(get_nombre,set_nombre)
    direccion=property(get_direccion,set_direccion)
    ciudad=property(get_ciudad,set_ciudad)
    cp=property(get_cp,set_cp)
    telefono=property(get_telefono,set_telefono)
    email=property(get_email,set_email)

    def obtener_datos(self): #método que devuelve los atributos en forma de lista
        return [self.nombre,self.direccion,self.ciudad,self.cp,self.telefono,self.email]
    
    def regresa_nombre(self):
        return self.nombre.title()