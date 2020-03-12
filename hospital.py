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
        lista_recetas=[]
        for i in self.pacientes:
            if nom in self.pacientes[i].regresa_nombre():
                pac=self.pacientes[i].muestra_datos()
                revisiones=pac.revmed
                for a in revisiones:
                    diag=revisiones[a].diag
                    for j in diag:
                        if len(diag.receta)!=0:
                            lista_recetas.append(diag.receta)#encara que cada diag tingui mes dunar recepta, com que tindran les mateixes fechas i espes no 'desmonto' la llista
#        espe_orden=[]
#        for i in self.especialidades:
#            espe_orden.append(self.dic_especialidades[i].nombre)
#        espe_orden.sort(key=str)
        
        for i in self.pacientes:
            if nom in self.pacientes[i].regresa_nombre():
                pac=self.pacientes[i]
                rev=pac.revmed #me muestra el último componente de pacientes que se corresponde con la revisión médica
#                lista_fechas_rev=[]
#                
##                for i in rev:
##                    lista_fechas_rev.append(rev.fecha)
##                lista_fechas_rev.sort(key=str) 
                if len(rev)==0:
                    print('La paciente no tiene revisiones médicas aún')
                    
                else:
                    dia=rev.diag
                    recet=dia.receta
                    recet.sort(key=rev.fecha.datatime)
                    return recet
                #pasar a data time
                #mirar arc sort
                #mirar funcionalidad arc_sort
                #puedo llamar a atributos desde el sort
                
#        for i in range(len(lista_fechas_rev)):
#            recet[i]
                
                    
            
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
        
    def consulta_derivacion(self,nombre):
        lista_deriv=[]
        for i in self.pacientes:
            if nombre in self.pacientes[i].regresa_nombre():
                pac=self.pacientes[i].muestra_datos()
                revisiones=pac.revmed
                for a in revisiones:
                    diag=revisiones[a].diag
                    for j in diag:
                        if diag.derivado==True:
                            lista_deriv.append(diag.deriva)
        return lista_deriv# falta ordenarla por fehcas
    
    def arxivo_medicos(self):
        dic_med_orden={}
        for a in self.especialidades:
            for i in self.medicas:#recorro dic medicas
                if self.medicas[i].especialidad==self.especialidades[a].regresa_nombre():#recorro especialitats en ordre(alfabetis), si coincideixem amb la especialitat de un metge ho guardo al nou diccionari
                    dic_med_orden[self.medicas[i].id_num]=self.medicas[i]
        arx_med=open('Médicos.txt','w')
        for i in dic_med_orden:#recorro el dic i vaig 'escribint-lo' al fitxer
            arx_med.write(str(dic_med_orden[i].muestra_datos()))
        arx_med.close
        

            
    def arxivo_paciente(self,pac):#fem un consulta i triem el pacient
        nombre=pac.nombre
        nombre=nombre.replace(' ','')
        paciente=pac.muestra_datos()
        arx_pac=open(nombre+'.txt','w')
        for i in paciente:
            arx_pac.write(str(i ))
        arx_pac.close
        #estadisitcas
        rev=pac.revmed#llamo en el main el consulta_paciente i me elegira uno si hay mas de uno
        list_espe=[]#hago un lista con todas las especialidades de las revisiones de paciente mirando si ha sido derivado o no
        for i in rev:
            diags=i.diag
            for a in diags:#cada element de la llsita es un diagnostic dins d'una llista, llavors agafant el 1r element ja ho tenim
                if a.derivado==True:
                    derivacion=diags[a].deriva#accedo al objeto DerivaPaciente 
                    list_espe.append(derivacion.muestra_espe())#muestro la especialidad de la derivacion i la meto en la lista
                elif a.derivado==False:
                    list_espe.append(a.muestra_espe())
        lista_estadi=[]  #LISTA VAcia donde metere las estadisticas              
        list_una_espe=[]
        for i in list_espe:#creo una llista amb UNA vegada cada especialitat
            if i not in list_una_espe:
                list_una_espe.append(i)
                lista_estadi=[]
        for i in list_una_espe:
            n=list_espe.count(i)#me cuenta cuantas veces aparece en la lista
            lista_estadi.append([i,n])# me pone dentro de la lista el nombre de la especialidad i cuantas veces aparece esta        
        return lista_estadi
    
    def arxivo_enf(self):
        categorias=['P:practicante','J:enfermera junior','M:enfermera senior','JE:jefa de enfermeras']
        dic_enf_orden={}
        for a in categorias:
            for i in self.enfermeras:#recorro dic enf
                if self.enfermeras[i].categoria==a:#recorro especialitats en ordre(alfabetis), si coincideixem amb la especialitat de un metge ho guardo al nou diccionari
                    dic_enf_orden[self.enfermeras[i].id_num]=self.enfermeras[i]
        arx_enf=open('Enfermeras.txt','w')
        for i in dic_enf_orden:#recorro el dic i vaig 'escribint-lo' al fitxer
            arx_enf.write(str(dic_enf_orden[i].muestra_datos()))
        arx_enf.close
        cat=[]#lista con todas la categroias de todas las enfermenra
        for i in self.enfermeras:
           cat.append( self.enfermeras[i].categoria)
        estadist=[]
        for i in categorias:
            estadist.append([i,cat.count(i)])
        return estadist
    
    def arxivo_recep(self):
        turnos=['1:matutino','2:verspertino','3:nocturno','4:rotatorio'] 
        dic_recep_orden={}
        for a in turnos:
            for i in self.recepcionistas:#recorro dic recep
                if self.recepcionistas[i].turno==a:#recorro especialitats en ordre(alfabetis), si coincideixem amb la especialitat de un metge ho guardo al nou diccionari
                    dic_recep_orden[self.recepcionistas[i].id_num]=self.recepcionistas[i]
        arx_enf=open('Recepcionistas.txt','w')
        for i in dic_recep_orden:#recorro el dic i vaig 'escribint-lo' al fitxer
            arx_enf.write(str(dic_recep_orden[i].muestra_datos()))
        arx_enf.close
        turn=[]#lista con todas la categroias de todas las enfermenra
        for i in self.recepcionistas:
           turn.append( self.recepcionistas[i].turno)
        estadist=[]
        for i in turnos:
            estadist.append([i,turn.count(i)])
        return estadist
        
    
                    
                
            