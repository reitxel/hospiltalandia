#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:49:33 2020

@author: raquel
"""
from datos import Datos #hereda de la clase Datos

from medica import Medica
from paciente import Paciente
from especialidad import Especialidad
from enfermera import Enfermera
from recepcionista import Recepcionista
from medicamento import Medicamento

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
        lista_med=[]
        for i in self.medicas:
            if nom == self.medicas[i].regresa_nombre():
                lista_med.append(self.medicas[i].regresa_nombre())
        if lista_med==[]:
            return False 
        else:
            for i in lista_med:
                for j in self.medicas:
                    if contra==self.medicas[j].password.lower():
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
        else:
            for i in lista_enf:
                for j in self.enfermeras:
                      if contra==self.enfermeras[j].password.lower():
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
        elif lista_recep!=[]:
            for i in lista_recep:
                for j in self.recepcionistas:
                    if contra==self.recepcionistas[j].password.lower():
                        recep=self.recepcionistas[j]
                        return recep 
            return False#si no hi ha contra  ben posada
     
    #COMPROBAR FECHA
    def comprobar_fecha(self,fecha_str):            
        fecha = datetime.strptime(fecha_str,'%d-%m-%Y').date()
        hoy = datetime.now().date()
        if str(fecha)>=str(hoy):
            return fecha
        elif str(fecha) < str(hoy):
            return False           

    #para el despliegue de todas las especialidades en tkinter
    def comprobar_especialidad(self):
        lista_espes=[]
        for i in self.especialidades:
            lista_espes.append(self.especialidades[i].regresa_nombre())
        lista_espes.sort(key=str)
        return lista_espes
    
    def comprobar_medi(self):
        lista_medis=[]
        for i in self.medicamentos:
            lista_medis.append(self.medicamentos[i].regresa_cod())
        return lista_medis
    
    def mcomprobar(self):
        lista_m=[]
        for i in self.medicas:
            lista_m.append(self.medicas[i].regresa_nombre())
        lista_m.sort(key=str)
        return lista_m
    
  
#METODOS DE ALTA: medica, paciente, enfermera, recepcionista, especialidad, medicamento
    def alta_pac(self,nom,apell,dire,ciudad,cp,telf,email,sang,recep):
        nom=(nom+' '+apell).title()
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
                                          
            
#METODOS DE CONSULTA:
    #metodo que abarca abarca las consultas por NOMBRE de medicas, recepcionistas, enfermeras y especialidades dependiendo del parametro de entrada
    def consulta_med(self,nom,apell):
        nom=nom+' '+apell
        lista_consulta=[]
        for i in self.medicas: #localizar un dato que no sea el campo clave del diccionario
            if nom.title() == self.medicas[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.medicas[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    #método de consulta de pacientes por NOMBRE
    def consulta_pac(self,nom,apell,recep): #alusion a informa de recepcionista
        nom=nom+' '+apell
        lista=[]
        for pac in recep.informa(nom,self.pacientes):
            lista.append(pac) #llamada al método informa de la clase recepccionista a través de un objeto de esta clase que toma como parámetro
        return lista
    def consulta_id_pac(self,ids):
        for i in self.pacientes.keys():
            if str(i)==str(ids):
                pac=self.pacientes[i]

                return pac
    
    def consulta_enf(self,nom,apell):
        nom=nom+' '+apell
        lista_consulta=[]
        for i in self.enfermeras: #localizar un dato que no sea el campo clave del diccionario
            if nom.title()  == self.enfermeras[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.enfermeras[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    
    def consulta_recep(self,nom,apell):
        lista_consulta=[]
        nom=nom+' '+apell
        for i in self.recepcionistas: #localizar un dato que no sea el campo clave del diccionario
            if nom.title()  == self.recepcionistas[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.recepcionistas[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    
    def consulta_espe(self,nom):
        lista_consulta=[]
        for i in self.especialidades: #localizar un dato que no sea el campo clave del diccionario
            if nom.capitalize() == self.especialidades[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(self.especialidades[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta
    
    def consulta_medi(self,cod):
        for i in self.medicamentos:
            if str(cod)==str(i):
                return (self.medicamentos[i].muestra_datos())

    #método de búsqueda de especialidade por CODIGO
    def consulta_cod_espe(self,cod):
        for i in self.especialidades:
            if cod in self.especialidades[i].muestra_datos():
                return self.especialidades[i].muestra_datos() 
    
    #método de consulta medicas por especialidad       
    def consulta_med_espe(self,especialidad):
        lista_medesp=[]
        for i in self.medicas:#recorro el dic de medicos y miro que medicos tienen la especialidad puesta como input
            if especialidad in self.medicas[i].muestra_datos():
                lista_medesp.append([self.medicas[i].regresa_nombre(),self.medicas[i].regresa_numpac()])#si la espeicalida coincide meto el nombre y el numero de pacientes del medico en una lista
        return lista_medesp
    
    #método de consulta de recetas que ordena por fecha y especialidad
    def consulta_recet(self,pac): #nombre del paciente como parametro, pero tengo las recetas dentro de diagnostico
        lista_recetas=[]#creo una lista con las recetas de cada diagnostico
        lista_diags=[]#creo una lista con los diagnosticos que tengan recetas
        lista_fechas=[]
        lista_revs=[]
        revisiones=pac.revmed
        for a in revisiones:
            diag=a.diag
            lista_fechas.append(a.fecha)
            for j in diag:
                if j.receta!=[]:
                    lista_recetas.append(j.receta)#encara que cada diag tingui mes dunar recepta, com que tindran les mateixes fechas i espes no 'desmonto' la llista
                    lista_diags.append(j)
                    lista_revs.append(a)
        lista_fechas.sort()
        espe_orden=[]#creo una lista con todas las especilaidades i las ordeno alfabeticamente
        for i in self.especialidades:            
           espe_orden.append(self.especialidades[i].nombre)
        espe_orden.sort(key=str)
        
        lista_final=[]
        for i in lista_fechas:#recooro llista fechas por orden
            for a in espe_orden:#recooro la lista de espeicalidades en orden
                for j in lista_revs:
                    if i==j.fecha:#en cas que la data coinsitexi amb una diag del de la llista 
                        for b in range(len(lista_diags)):
                            if a==lista_diags[b].especialidad:#tenint en compre que recorrerem les especialitats i dates en ordre
                                for g in range(len(lista_recetas[b])):
                                    lista_final.append(lista_recetas[b][g].muestra_datos())#com que la llista diag i rece
        return lista_final# estan ordenades per diagnostics, en ordre de dia i per especialitat del diagnostic en cas d'havar-hi dos en el mateix dia
    
    #método de consulta derivaciones
    def consulta_deriv(self,pac):
        lista_deriv=[]#llista amb els objetes derivacio
        lista_fecha=[]#llista de dates amb els de les derivacions
        revisiones=pac.revmed
        for a in revisiones:
            diag=a.diag
            for j in diag:
                if j.derivado==True:
                    derivacion=j.deriva
                    for b in derivacion:
                        lista_deriv.append(b)
                        lista_fecha.append(b.fecha)                   
        lista_fecha.sort()
        fechas_orden=lista_fecha[::-1]#invierto la lista de fechas para tener la mas temprana antes
        lista_ordre=[]
        for i in fechas_orden:
            for j in lista_deriv:
                if i==j.fecha:#si la data de la derivacio concideix amb la data es guardara tenint en compte que les dates van en ordre
                    lista_ordre.append(j.muestra_datos())
        return lista_ordre

#METODOS MENU REVISIÓN   
    #ALTA REVISIONES                                    
    def alta_revisiones(self,fecha,nom,apell,recep):
                fecha=self.comprobar_fecha(fecha)#comprueba la fecha
                pac=self.consulta_paciente(nom,apell,recep)#comprueva el faciente i genera el objeto  
                return pac

    def assignar(self,pac,fecha,enf):#creamos este metodo ara no aplicar un metodo que depende de un dic en graficos
          enf.asigna_revision(pac,fecha,self.medicas)  
    
    #REALIZA REVISION   
    def revision_hoy(self,med):
        lista_pacnorev=med.pacnorev #lista no atendidos
        lista_atender_hoy=[]
        for i in lista_pacnorev:
            revision=i.revmed
            for j in revision:
                if j.fecha == datetime.now().date(): #pasar fecha del formato str a datetime
                    lista_atender_hoy.append(i)  
        return lista_atender_hoy
    
    #de aqui lo llevo a comprueba paceinte, que le pongo el id si hay mas de uno
    def atender_hoy(self,pac):       
        for i in pac.revmed:#recorro todas la revisiones del paciente y cojo solo de con fecha de hoy
            if i.fecha==datetime.now().date():
                rev=i
        return rev.diag[-1]#aqui si no existe supongo que devuelve none, si devuelve el diagnostico seria comporbar si el True lo muestro si es False lo creo y me voy a realizo diag
            
    def realizar_diag(self,diag,enfe,obs):
        diag.observaciones=obs
        diag.enfermedad=enfe#completo el diagnostico que tenia
        return diag
    
    def expedir_receta(self,diag,codigo,dosis): #preguntamos si quiere expedir receta
        diag.gen_recet(codigo,dosis) #funcion de diagnotico que me genera la receta

    def derivar(self,diag,nommed,especialidad,med,pac):    #aqui llega si quiere derivar
        diag.derivap(nommed,datetime.now().date(),especialidad)#guardo la derivacio en el diagnotico
        #en algun momento hay que dar la opcion de que pare la derivacion, osea boton de salida
        
    def actualizar_listas_med(self,med,pac): #cuando se cumple la derivaicon
        lista_pacnorev=med.pacnorev
        lista_pacrev=med.pacrev
        lista_pacnorev.remove(pac)
        lista_pacrev.append(pac) 
    
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
        espe_totes=[]
        for i in self.medicas:
            espe_totes.append(self.medicas[i].muestra_espe())
        estadistiques=[]
        for i in self.especialidades:
            estadistiques.append([i,espe_totes.count(i)])
        estadistiques.append(['Numero total de medicas es: ',len(self.medicas)])
        return estadistiques           
      
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
                    derivacion=a.deriva#accedo al objeto DerivaPaciente 
                    list_espe.append(derivacion[0].muestra_espe())#muestro la especialidad de la derivacion i la meto en la lista
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
            
