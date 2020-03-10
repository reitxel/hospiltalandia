#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:49:33 2020

@author: raquel
"""
from datos import Datos #hereda de la clase Datos

class Hospital(Datos): #relación de herencia con Datos por ello la hereda como parametro
    def __init__(self,_nombre,_direccion,_ciudad,_cp,_telefono,_email,_dic_pacientes,_dic_medicas,_dic_especialidades,_dic_enfermeras,_dic_recepcionistas,_dic_medicamentos): #tiene como atributos los de Datos y los suyos propios
        super().__init__(_nombre,_direccion,_ciudad,_cp,_telefono,_email) #llamada al constructor de Datos
        self.set_pacientes(_dic_pacientes)
        self.set_medicas(_dic_medicas)
        self.set_especialidades(_dic_especialidades)
        self.set_enfermeras(_dic_enfermeras)
        self.set_recepcionistas(_dic_recepcionistas)
        self.set_medicamentos(_dic_medicamentos)
        
    def set_pacientes(self,_dic_pacientes):
        self.__pacientes=_dic_pacientes
    def set_medicas(self,_dic_medicas):
        self.__medicas=_dic_medicas
    def set_especialidades(self,_dic_especialidades):
        self.__especialidades=_dic_especialidades
    def set_enfermeras(self,_dic_enfermeras):
        self.__enfermeras=_dic_enfermeras
    def set_recepcionistas(self,_dic_recepcionistas):
        self.__recepcionistas=_dic_recepcionistas
    def set_medicamentos(self,_dic_medicamentos):
        self.__medicamentos=_dic_medicamentos
        
    def get_pacientes(self):
        return self.__pacientes
    def get_medicas(self):
        return self.__medicas
    def get_especialidades(self):
        return self.__especialidades
    def get_enfermeras(self):
        return self.__enfermeras
    def get_recepcionistas(self):
        return self.__recepcionistas
    def get_medicamentos(self):
        return self.__medicamentos
        
    pacientes=property(get_pacientes,set_pacientes)
    medicas=property(get_medicas,set_medicas)
    especialidades=property(get_especialidades,set_especialidades)
    enfermeras=property(get_enfermeras,set_enfermeras)
    recepcionistas=property(get_recepcionistas,set_recepcionistas)
    medicamentos=property(get_medicamentos,set_medicamentos)
        
    #METODOS DE ALTA: medica, paciente, enfermera, recepcionista, especialidad, medicamento
    def metodo_alta(self,obj,ident,recep,entrada):
        if entrada=='med':
            dic=self.medicas
        elif entrada=='pac':
            dic=self.pacientes
        elif entrada=='enf':
            dic=self.enfermeras
        elif entrada=='recep':
            dic=self.recepcionistas
        elif entrada=='espe':
            dic=self.especialidades
        elif entrada=='medicamento':
            dic=self.medicamentos
            
        recep.altas(dic,obj,ident) #llamada al método altas de recepcionistas tomando como parametro este objeto
                                    
    #METODO PARA MOSTRAR LISTAS DE MÉDICAS/PACIENTES/ESPECIALIDADES/ENFERMERAS/RECEPCIONISTAS/MEDICAMENTOS: mismo prodedimiento
    def muestra_info(self,lista_info,entrada): 
        if entrada=='pac':
            dic=self.pacientes
        elif entrada=='med':
            dic=self.medicas
        elif entrada=='recep':
            dic=self.recepcionistas
        elif entrada=='enf':
            dic=self.enfermeras
        elif entrada=='espe':
            dic=self.especialidades
        elif entrada=='medicamento':
            dic=self.medicamentos
            
        for i in dic: #recorro diccionario
            lista_info.append(dic[i].muestra_datos()) #voy añadiendo a la lista toda la info de las médicas del diccionario
        return lista_info #me devuelve la lista completa
            
    #METODOS DE CONSULTA: medica, paciente, enfermera, recepcionista, especiaidad, medicamento, recetas, derivaciones, medico por especialidad
    def consulta_dics(self,nom,lista_consulta,entrada):
        if entrada=='med':
            dic=self.medicas
        elif entrada=='recep':
            dic=self.recepcionistas
        elif entrada=='enf':
            dic=self.enfermeras
        elif entrada=='espe':
            dic=self.especialidades
#        elif entrada=='medicamento':
#            dic=self.medicamentos
        lista_consulta=[]
        for i in dic: #localizar un dato que no sea el campo clave del diccionario
            if nom in dic[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(dic[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta #me devuelve una lista con todos los datos de las medicas cuyo nombre coincida con algo de lo que se haya introducido por pantalla
    
    def consulta_paciente(self,nom,recep): #alusion a informa de recepcionista
        lista=[]
        for pac in recep.informa(nom,self.pacientes):
            lista.append(recep.informa(nom,self.pacientes)) #llamada al método informa de la clase recepccionista a través de un objeto de esta clase que toma como parámetro
        return lista
    
#    def consulta_derivacion(self):
        
    def consulta_med_espe(self,especialidad):
        lista_medesp=[]
        for i in self.medicas:#recorro el dic de medicos y miro que medicos tienen la especialidad puesta como input
            if especialidad in self.medicas[i].muestra_datos():
                print('None')
                lista_medesp.append([self.medicas[i].regresa_nombre(),self.medicas[i].regresa_numpac()])#si la espeicalida coincide meto el nombre y el numero de pacientes del medico en una lista
        return lista_medesp
    
    def consulta_recetas(self,nom): #nombre del paciente como parametro, pero tengo las recetas dentro de diagnostico
        
        espe_orden=[]
        for i in self.especialidades:
            espe_orden.append(self.dic_especialidades[i].nombre)
        espe_orden.sort(key=str)
        
        for i in self.pacientes:
            if nom in self.pacientes[i].regresa_nombre():
                pac=self.pacientes[i]
                rev=pac.revmed #me muestra el último componente de pacientes que se corresponde con la revisión médica
                lista_fechas_rev=[]
                
                for i in rev:
                    lista_fechas_rev.append(rev.fecha)
                lista_fechas_rev.sort(key=str) 
                dia=rev.diag
                recet=diag.receta
                
                #pasar a data time
                #mirar arc sort
                #mirar funcionalidad arc_sort
                #puedo llamar a atributos desde el sort
                
        for i in range(len(lista_fechas_rev)):
            recet[i]
                
                    
            
    #METODOS PARA LA BUSQUEDA DE MEDICAS/PACIENTES POR NUMERO IDENTIFICADOR: mismo prodedimiento para ambos 
    def consulta_ident(self,identificador,entrada): #parámetro de entrada por pantalla
        if entrada=='pac':
            dic=self.pacientes
        elif entrada=='med':
            dic=self.medicas
        elif entrada=='recep':
            dic=self.recepcionistas
        elif entrada=='enf':
            dic=self.enfermeras
        elif entrada=='medicamento':
            dic=self.medicamentos
        
        if identificador in dic.keys(): #condición de que el parametro introducido coincida con alguna clave del diccionario de médicas, que son los numeros identificadores
            return dic[identificador].muestra_datos() #me devuelve toda la información que corresponda al número en cuestión si existe

    def consulta_cod_espe(self,cod):
        for i in self.especialidades:
            if cod in self.especialidades[i].muestra_datos():
                return self.especialidades[i].muestra_datos()                
        
    def consulta_revmed_ident(self,identificador):
        if identificador in self.pacientes.keys():
            return self.pacientes[identificador].muestra_datos()[-1]