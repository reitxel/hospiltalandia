#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:48:00 2020

@author: raquel
"""
from datos import Datos
from fichas import FichaRevision
#relacion con paciente

class Enfermera(Datos):
    def __init__(self,_id_num,_nombre,_direccion,_ciudad,_cp,_telefono,_email,_password,_categoria):
        super().__init__(_nombre,_direccion,_ciudad,_cp,_telefono,_email)
        self.set_id_num(_id_num)
        self.set_password(_password)
        self.set_categoria(_categoria)
        
    def set_id_num(self,_id_num):
        self.__id_num=_id_num
    def set_password(self,_password):
        self.__password=_password
    def set_categoria(self,_categoria):
        self.__categoria=_categoria
        
    def get_id_num(self):
        return self.__id_num
    def get_password(self):
        return self.__password
    def get_categoria(self):
        return self.__categoria
    
    id_num=property(get_id_num,set_id_num)
    password=property(get_password,set_password)
    categoria=property(get_categoria,set_categoria)
    
    def muestra_datos(self):
        nombre,direccion,ciudad,cp,telefono,email=self.obtener_datos()
        return [self.id_num,nombre,direccion,ciudad,cp,telefono,email,self.categoria]
    
    def asigna_revision(self,p,fecha,dic_medicas):
        revmed=p.muestra_revisiones()
        #revmed=p.revmed()
        if len(revmed)==0: #si la lista esta vacia quiere decir que no hay revisiones para ese paciente
            especialidad='Médico de familia'
        else:
            ultima_rev=revmed[-1] #revision anterior? pero tener en cuanta entre listas co cosas y una lista de objetos
            diagnosticos=ultima_rev.diag# llista con todos los diagnosticos
            diag=diagnosticos[-1]#ultimo diagnostico de todos
            print(diag)
            if diag.derivado==True:
                deriva=diag.derivado#accedo al objeto DerivaPaciente 
                especialidad=deriva.muestra_espe()  #muestro la especialidad de la derivacion     
            elif diag.derivado==False:
                especialidad=diag.especialidad
                
        for i in dic_medicas:#recorro el dic de medicos y guardo en una lista los medicos con la especialidad deseada
            if especialidad in dic_medicas[i].muestra_datos():
                #print (dic_medicas[i].pacrev())
                if dic_medicas[i].regresa_numpac()<=10:
                    med=dic_medicas[i].regresa_nombre()
                    medico=dic_medicas[i]
                    break
        revmed=p.tiene_revision(len(revmed)+1,fecha,med,especialidad)  #codigo se forma secuencial, uno mas que el anterior   
        medico.tiene_pacnorev(p)
        return revmed
 

