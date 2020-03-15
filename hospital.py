#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:49:33 2020

@author: raquel
"""
from datos import Datos #hereda de la clase Datos

from utilidades import Utilidades

from medica import Medica
from paciente import Paciente
from especialidad import Especialidad
from enfermera import Enfermera
from recepcionista import Recepcionista
from medicamento import Medicamento
from diagnostico import Diagnostico
from derivapaciente import DerivaPaciente

from datetime import datetime


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
    
    #MÉTODO DE INICIAR SESIÓN: tanto medicas, enfermeras como recepcionitas
    def login_med(self,nom,contra):#la entrada es el nombre de
        while True:
                lista_med=[]
                for i in self.medicas:
                    if nom == self.medicas[i].regresa_nombre():
                        lista_med.append(self.medicas[i].regresa_nombre())
                if lista_med==[]:
                    return False    
                for i in lista_med:
                    for j in self.medicas:
                        if lista_med!=[]:
                            if contra==self.medicas[j].password:
                                med=self.medicas[j]
                                return med#si es troba un recep
                return False#si no es troba la contrasenya
            
    def login_enf(self,nom,contra):
                lista_enf=[]
                for i in self.enfermeras:
                    if nom == self.enfermeras[i].regresa_nombre():
                        lista_enf.append(self.enfermeras[i].regresa_nombre())
                if lista_enf==[]:
                    return False
                    for j in self.enfermeras:
                        if lista_enf!=[]:
                            if contra==self.enfermeras[j].password:
                                print('Constraseña acertada')
                                enf=self.enfermeras[j]
                                return enf
                    return False
    def log_recep(self,nom,contra):             
        lista_recep=[]
        for i in self.recepcionistas:
            if nom.title() == self.recepcionistas[i].regresa_nombre():
                lista_recep.append(self.recepcionistas[i].regresa_nombre())
                if lista_recep==[]:
                    return False#si no existeix el nom
            for i in lista_recep:
                for j in self.recepcionistas:
                    if lista_recep!=[]:
                        if contra==self.recepcionistas[j].password.lower():
                            recep=self.recepcionistas[j]
                            return recep 
            return False#si no hi ha contra  ben posada
     
    #COMPROBAR FECHA
    def comprobar_fecha(fecha_str):            
        while True:
            try:
                fecha_str=input('\nIntroduzca la fecha de revisión en formato "dd-mm-aaaa": ')#criterio para que la fecha que me introduzca por pantalla mantenga este formato
                fecha = datetime.strptime(fecha_str,'%d-%m-%Y').date()
                hoy = datetime.now().date()
                if str(fecha)>=str(hoy):
                    return fecha
                elif str(fecha) < str(hoy):
                    print('\nLa fecha es anterior a la actual')
            except ValueError:
                print("\nNo ha introducido una fecha correcta")  
    #para el despliegue de todas las especialidades en tkinter
    def comprobar_especialidad(self):
        lista_espes=[]
        for i in self.especialidades:
            lista_espes.append(self.especialidades[i].regresa_nombre())
        return lista_espes
    
  
    #METODOS DE ALTA: medica, paciente, enfermera, recepcionista, especialidad, medicamento
    def alta_pac(self,nom,dire,ciudad,cp,telf,email,sang,recep):
        id_p=len(self.pacientes.keys())+1
        pac=Paciente(id_p,nom.title(),dire,ciudad,cp,telf,email,sang)
        recep.altas(self.pacientes,pac,id_p)
        
    def alta_med(self,nom,apell,dire,ciudad,cp,telf,email,espe,recep,password):
        nom=(nom+' '+apell).title()
        id_m=len(self.medicas.keys())+1
        med=Medica(id_m,nom,dire,ciudad,cp,telf,email,password,espe)
        recep.altas(self.medicas,med,id_m)
        
    def alta_enf(self,nom,apell,dire,ciudad,cp,telf,email,cat,recep,password):
        nom=(nom+' '+apell).title()
        id_e=len(self.enfermeras.keys())+1
        enf=Enfermera(id_e,nom,dire,ciudad,cp,telf,email,password,cat)
        recep.altas(self.enfermeras,enf,id_e)
        
    def alta_recep(self,nom,apell,dire,ciudad,cp,telf,email,turno,recep,password):
        nom=(nom+' '+apell).title()
        id_r=len(self.recepcionistas.keys())+1
        rec=Recepcionista(id_r,nom,dire,ciudad,cp,telf,email,password,turno)
        recep.altas(self.recepcionistas,rec,id_r)
        
    def alta_espe(self,nom,cod,recep):
        espe=Especialidad(cod,nom)
        recep.altas(self.especialidades,espe,cod)
        
    def alta_medi(self,codigo,princ_activ,marca,lab,recep):
        medi=Medicamento(codigo,princ_activ,marca,lab)
        recep.altas(self.medicamentos,medi,codigo)
        
#    def alta_rev(self,nom): #nombre y apellido de la paciente
#        while True:
#            try:
#                a=0
#                fecha=comprobar_fecha()
#                for i in dic_pacientes:
#                    if nom in dic_pacientes[i].regresa_nombre():
#                        pac=dic_pacientes[i]      
#                        a+=1
#   
#                if a==0:
#                    print('No existe tal paciente')
#                elif a==1:
#                    enf.asigna_revision(pac,fecha,dic_medicas)
#                    print('Revisión a',pac.regresa_nombre(),'asignada')
#                elif a!=1: #más de unx paciente con el nombre introducido
#                    print('Hay',a,'pacientes con el nombre introducido:')
#                    for i in dic_pacientes:
#                        if nom in dic_pacientes[i].regresa_nombre():
#                            print(dic_pacientes[i].muestra_datos())
#                    id_p=int(input('Introduzca el número identificador de la paciente a asignar la revisión: '))
#                    pac=dic_pacientes[id_p]
#                    enf.asigna_revision(pac,fecha,dic_medicas)
#                    print('Revisión a',pac.regresa_nombre(),'asignada')
#
#                break
#            
#            except ValueError:
#                print("\nNo ha introducido una fecha correcta")
    
            
    #METODOS DE CONSULTA:
    #metodo que abarca abarca las consultas por NOMBRE de medicas, recepcionistas, enfermeras y especialidades dependiendo del parametro de entrada
    def consulta_med(self,nom,apell):
        nom=nom+' '+apell
        lista_consulta=[]
        for i in self.medicas: #localizar un dato que no sea el campo clave del diccionario
            if nom.title() in self.medicas[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.medicas[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    #método de consulta de pacientes por NOMBRE
    def consulta_pac(self,nom,apell,recep): #alusion a informa de recepcionista
        nom=nom+' '+apell
        lista=[]
        for pac in recep.informa(nom,self.pacientes):
            lista.append(pac) #llamada al método informa de la clase recepccionista a través de un objeto de esta clase que toma como parámetro
        return lista
    
    def consulta_enf(self,nom,apell):
        nom=nom+' '+apell
        lista_consulta=[]
        for i in self.enfermeras: #localizar un dato que no sea el campo clave del diccionario
            if nom.title()  in self.enfermeras[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.enfermeras[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    
    def consulta_recep(self,nom,apell):
        lista_consulta=[]
        nom=nom+' '+apell
        for i in self.recepcionistas: #localizar un dato que no sea el campo clave del diccionario
            if nom.title()  in self.recepcionistas[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.recepcionistas[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    
    def consulta_espe(self,nom):
        lista_consulta=[]
        for i in self.especialidades: #localizar un dato que no sea el campo clave del diccionario
            if nom in self.especialidades[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.especialidades[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    
    def consulta_medi(self,cod):
        lista_meds=[]
        for i in self.medicamentos:
            if cod in self.medicamentos.keys():
                lista_meds.append(self.medicamento[i].muestra_datos)

    #método de búsqueda de especialidade por CODIGO
    def consulta_cod_espe(self,cod):
        for i in self.especialidades:
            if cod in self.especialidades[i].muestra_datos():
                return self.especialidades[i].muestra_datos() 

    #métodode consulta de recetas que ordena por fecha y especialidad
    def consulta_recet(self,nom): #nombre del paciente como parametro, pero tengo las recetas dentro de diagnostico
        lista_recetas=[]
        for i in self.pacientes:
            if nom in i.regresa_nombre():
                pac=i.muestra_datos()
                revisiones=pac.revmed
                for a in revisiones:
                    diag=a.diag
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
    
    #método de consulta derivaciones
    def consulta_deriv(self,nombre):
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
    
    #método de consulta medicas por especialidad       
    def consulta_med_espe(self,especialidad):
        lista_medesp=[]
        for i in self.medicas:#recorro el dic de medicos y miro que medicos tienen la especialidad puesta como input
            if especialidad in self.medicas[i].muestra_datos():
                lista_medesp.append([self.medicas[i].regresa_nombre(),self.medicas[i].regresa_numpac()])#si la espeicalida coincide meto el nombre y el numero de pacientes del medico en una lista
        return lista_medesp
   
    #METODOS DE CREACION DE ARCHIVOS: medicas, pacientes, enfermeras y recepcionistas
    def archivo_medicas(self):
        dic_med_orden={}
        for a in self.especialidades:
            for i in self.medicas:#recorro dic medicas
                if self.medicas[i].especialidad==self.especialidades[a].regresa_nombre():#recorro especialitats en ordre(alfabetis), si coincideixem amb la especialitat de un metge ho guardo al nou diccionari
                    dic_med_orden[self.medicas[i].id_num]=self.medicas[i]
        arx_med=open('Médicos.txt','w')
        for i in dic_med_orden:#recorro el dic i vaig 'escribint-lo' al fitxer
            arx_med.write(str(dic_med_orden[i].muestra_datos()))
        arx_med.close
      
    def archivo_pacientes(self,pac):#fem un consulta i triem el pacient
        nombre=pac.nombre
        nombre=nombre.replace(' ','')
        paciente=pac.muestra_datos()
        arx_pac=open(nombre+'.txt','w')
        for i in paciente:
            arx_pac.write(str(i))
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
        lista_estadisticas=[]  #LISTA VAcia donde metere las estadisticas              
        list_una_espe=[]
        for i in list_espe:#creo una llista amb UNA vegada cada especialitat
            if i not in list_una_espe:
                list_una_espe.append(i)
                lista_estadisticas=[]
        for i in list_una_espe:
            n=list_espe.count(i)#me cuenta cuantas veces aparece en la lista
            lista_estadisticas.append([i,n])# me pone dentro de la lista el nombre de la especialidad i cuantas veces aparece esta        
        return lista_estadisticas
 
    def archivo_enf(self):
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

    def archivo_recep(self):
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
            