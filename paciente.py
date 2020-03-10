
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:48:00 2020

@author: raquel
"""

from datos import Datos
from fichas import FichaRevision

class Paciente(Datos):
    def __init__(self,_id_num,_nombre,_direccion,_ciudad,_cp,_telefono,_email,_grupo_sanguineo):
        super().__init__(_nombre,_direccion,_ciudad,_cp,_telefono,_email)
        self.set_id_num(_id_num)
        self.set_grupo_sanguineo(_grupo_sanguineo)
        self.__revmed=[] #lista RM
        
    def set_id_num(self,_id_num):
        self.__id_num=_id_num
    def set_grupo_sanguineo(self,_grupo_sanguineo):
        self.__grupo_sanguineo=_grupo_sanguineo
    def set_revmed(self,_revmed,_cod,_fecha,_med,_espec):
        self.__revmed=_revmed
        
    def get_id_num(self):
        return self.__id_num
    def get_grupo_sanguineo(self):
        return self.__grupo_sanguineo
    def get_revmed(self):
        return self.__revmed
    
    id_num=property(get_id_num,set_id_num)
    grupo_sanguineo=property(get_grupo_sanguineo,set_grupo_sanguineo)
    revmed=property(get_revmed,set_revmed)
    
    def muestra_datos(self):
        nombre,direccion,ciudad,cp,telefono,email=self.obtener_datos()
        return [self.id_num,nombre,direccion,ciudad,cp,telefono,email,self.grupo_sanguineo,self.muestra_revisiones()]
    
    def muestra_revisiones(self):
        llista_rev=[]
        for i in self.revmed:
           llista_rev.append(i.muestra_datos())
        return llista_rev
    
    def tiene_revision(self,cod,fecha,espec,med):
        fr=FichaRevision(cod,fecha) #creo objeto de la clase fichas
        f=fr.tiene_diagnostico(espec,med)
        self.revmed.append(fr) #añado en la lista revmed el objeto con todos sus atributos
        return self.revmed
