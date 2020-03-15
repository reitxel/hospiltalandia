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
    

    #MÉTODO DE INICIAR SESIÓN: tanto medicas, enfermeras como recepcionitas
    def login(self,entrada):
        nom=input('-> Nombre y apellido: ').title()
        while True:
            if entrada=='med':
                lista_med=[]
                for i in self.medicas:
                    if nom == self.medicas[i].regresa_nombre():
                        lista_med.append(self.medicas[i].regresa_nombre())
                if lista_med==[]:
                    return 2    
                password=input('-> Contraseña (puede introducir ''salir'' para volver al menú principal): ')
                for i in lista_med:
                    for j in self.medicas:
                        if lista_med!=[]:
                            if password==self.medicas[j].password:
                                print('Constraseña acertada')
                                med=self.medicas[j]
                                return med
                            elif password=='salir':
                                return 1

                
            elif entrada=='enf':
                lista_enf=[]
                for i in self.enfermeras:
                    if nom == self.enfermeras[i].regresa_nombre():
                        lista_enf.append(self.enfermeras[i].regresa_nombre())
                if lista_enf==[]:
                    return 2
                password=input('-> Contraseña (puede introducir ''salir'' para volver al menú principal): ')
                for i in lista_enf:
                    for j in self.enfermeras:
                        if lista_enf!=[]:
                            if password==self.enfermeras[j].password:
                                print('Constraseña acertada')
                                enf=self.enfermeras[j]
                                return enf
                            elif password=='salir':
                                return 1

            elif entrada=='recep':
                lista_recep=[]
                for i in self.recepcionistas:
                    if nom == self.recepcionistas[i].regresa_nombre():
                        lista_recep.append(self.recepcionistas[i].regresa_nombre())
                if lista_recep==[]:
                    return 2
                password=input('-> Contraseña (puede introducir ''salir'' para volver al menú principal): ')
                for i in lista_recep:
                    for j in self.recepcionistas:
                        if lista_recep!=[]:
                            if password==self.recepcionsitas[j].password:
                                print('Constraseña acertada')
                                recep=self.recepcionistas[j]
                                return recep
                            elif password=='salir':
                                return 1               

                    
    #METODOS DE ALTA: medica, paciente, enfermera, recepcionista, especialidad, medicamento
    def metodo_alta(self,obj,ident,recep,entrada): #metodo unico que abarca todas las altas dependiendo del parametro de entrada
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
            
    #METODOS DE CONSULTA:
    #metodo que abarca abarca las consultas por NOMBRE de medicas, recepcionistas, enfermeras y especialidades dependiendo del parametro de entrada
    def consulta_dics(self,nom,lista_consulta,entrada): #
        if entrada=='med':
            dic=self.medicas
        elif entrada=='recep':
            dic=self.recepcionistas
        elif entrada=='enf':
            dic=self.enfermeras
        elif entrada=='espe':
            dic=self.especialidades
        lista_consulta=[]
        for i in dic: #localizar un dato que no sea el campo clave del diccionario
            if nom in dic[i].regresa_nombre(): #comparo lo que el usuario ha introducido con el método que me devuelve el nombre de la médica
                lista_consulta.append(dic[i].muestra_datos()) #estoy metiendo en la lista todos los datos de las médicas con ese nombre
        return lista_consulta #me devuelve una lista con todos los datos de las medicas cuyo nombre coincida con algo de lo que se haya introducido por pantalla
    
    #método de consulta de pacientes por NOMBRE
    def consulta_paciente(self,nom,recep): #alusion a informa de recepcionista
        lista=[]
        for pac in recep.informa(nom,self.pacientes):
            lista.append(pac) #llamada al método informa de la clase recepccionista a través de un objeto de esta clase que toma como parámetro
        return lista
    
    #método qua abarca las consultas por identificador/código de pacientes, médicas, recepcionistas, enfermeras y medicamentos 
    def consulta_ident(self,identificador,entrada): #nos da la opción de consultas por número identificador
        if entrada=='pac':
            dic=self.pacientes
        elif entrada=='med':
            dic=self.medicas
        elif entrada=='recep':
            dic=self.recepcionistas
        elif entrada=='enf':
            dic=self.enfermeras
        elif entrada=='medicamento': #en el caso del medicamento nos cogería el código, que es la clave del diccionario
            dic=self.medicamentos
        
        if identificador in dic.keys(): #condición de que el parametro introducido coincida con alguna clave del diccionario de médicas, que son los numeros identificadores
            return dic[identificador].muestra_datos() #me devuelve toda la información que corresponda al número en cuestión si existe

    #método de búsqueda de especialidade por CODIGO
    def consulta_cod_espe(self,cod):
        for i in self.especialidades:
            if cod in self.especialidades[i].muestra_datos():
                return self.especialidades[i].muestra_datos() 

    #métodode consulta de recetas que ordena por fecha y especialidad
    def consulta_recetas(self,nom): #nombre del paciente como parametro, pero tengo las recetas dentro de diagnostico
        lista_recetas=[]#creo una lista con las recetas de cada diagnostico
        lista_diags=[]#creo una lista con los diagnosticos que tengan recetas
        lista_fechas=[]
        lista_revs=[]
        for i in self.pacientes:
            if nom in self.pacientes[i].regresa_nombre():
                pac=self.pacientes[i]
                revisiones=pac.revmed
                for a in revisiones:
                    diag=a.diag
                    lista_fechas.append(a.fecha)
                    for j in diag:
                        if j.receta!=[]:
                            lista_recetas.append(j.receta)#encara que cada diag tingui mes dunar recepta, com que tindran les mateixes fechas i espes no 'desmonto' la llista
                            lista_diags.append(j)
                            lista_revs.append(a)
        lista_fechas=lista_fechas.sort()
        espe_orden=[]#creo una lista con todas las especilaidades i las ordeno alfabeticamente
        for i in self.especialidades:            
           espe_orden.append(self.especialidades[i].nombre)
        espe_orden=espe_orden.sort(key=str)
        
        lista_final=[]
        for i in lista_fechas:#recooro llista fechas por orden
            for a in espe_orden:#recooro la lista de espeicalidades en orden
                for j in lista_revs:
                    if i==j.fecha:#en cas que la data coinsitexi amb una diag del de la llista 
                        for b in range(len(lista_diags)):
                            if a==lista_diags[b].especialidad:#tenint en compre que recorrerem les especialitats i dates en ordre
                                lista_final.append(lista_recetas[b][0].muestra_datos())#com que la llista diag i rece
        return lista_final
                    
    #método de consulta derivaciones
    def consulta_derivacion(self,nombre):
        lista_deriv=[]#llista amb els objetes derivacio
        lista_fecha=[]#llista de dates amb els de les derivacions
        for i in self.pacientes:
            if nombre.title() in self.pacientes[i].regresa_nombre():
                pac=self.pacientes[i]
                revisiones=pac.revmed
                for a in revisiones:
                    diag=a.diag
                    for j in diag:
                        if j.derivado==True:
                            derivacion=j.deriva
                            for b in derivacion:
                                print (derivacion)
                                lista_deriv.append(b)
                                lista_fecha.append(b.fecha)
        print (lista_fecha)                   
        lista_fecha.sort()
        
        lista_ordre=[]
        for i in lista_fecha:
            for j in lista_deriv:
                if i==j.fecha:#si la data de la derivacio concideix amb la data es guardara tenint en compte que les dates van en ordre
                    lista_ordre.append(j.muestra_datos())
                            
        return lista_ordre# falta ordenarla por fehcas
    
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
            