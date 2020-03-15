#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:17:18 2020

@author: raquel
"""
#programa principal que tendrá el menú inicial y la llamada a las clases utilidades y hospital.
from hospital import Hospital
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

def pedir_datos():#este metodo lo creamos para no pedir los mismos datos en cada una de las altas de personas
    nombre=input('-> Nombre: ').title()
    apellido=input('-> Primer apellido: ').title()
    direccion=input('-> Dirección: ')
    ciudad=input('-> Ciudad: ')
    cp=input('-> CP: ')
    telf=input('-> Telf: ')
    email=input('-> Email: ')
    return nombre,apellido,direccion,ciudad,cp,telf,email

def comprobar_fecha():            
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
    
#def comprobar(nombre,apellido,direccion,ciudad,cp,telf,email,espe_gruposang):
#    if len(nombre)!=0 and len(apellido)!=0 and len(direccion)!=0 and len(ciudad)!=0 and len(cp)!=0 and len(telf)!=0 and len(email)!=0 and len(espe_gruposang)!=0:
#        if len(nombre)>=2 and len(apellido)>=2 and len(telf)>=2: #asi puedo hacer la contraseña
#            if nombre.isalpha()==True and apellido.isalpha()==True:
#                nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
#            elif cp.isnumeric()==True:
#                #NO SE QUE PONER
#    else:
#        #algun campo esta vacio

def main():
    util=Utilidades() #creo objeto de la clase Utilidades
    dic_especialidades,dic_medicas,dic_pacientes,dic_enfermeras,dic_recepcionistas,dic_medicamentos,lista_hosp=util.lectura('especialidades.csv','informacion.csv','medicina.csv') #llamada al metodo de Utilidades para guardar lo que nos devuelve en variables 
    hosp=Hospital(lista_hosp[0],lista_hosp[1],lista_hosp[2],lista_hosp[3],lista_hosp[4],None,dic_pacientes,dic_medicas,dic_especialidades,dic_enfermeras,dic_recepcionistas,dic_medicamentos) #creo el objeto de hospital donde los primeros parámetros los toma de la lista de info hospital
    recep=dic_recepcionistas[1] #objeto de la clase Recepcionista
    enf=dic_enfermeras[1]
    opcion=0
    #lista_info=[]
    #MENU DE OPCIONES
    while opcion!=5: 
        try: 
            print('\nMenú de opciones\n 1) Altas\n 2) Consultas\n 3) Revisiones\n 4) Archivos\n 5) Salida\n')
            opcion=int(input('Seleccione una opción: '))
            if opcion==1:
                #MENU ALTAS
                opcion1=0
                print('Inicio sesión recepcionista')
                log=hosp.login('recep') #tendria que ser a cada opcion
                if log == 1:
                    print('\nNo se ha iniciado sesión')
                elif log == 2:
                    print('\nNo existe tal empleada')
                else:
                    while opcion1!=7:
                        try:
                            print('\nMenú de altas\n 1) Médica\n 2) Paciente\n 3) Enfermeras\n 4) Recepcionista\n 5) Especialidad\n 6) Medicamento\n 7) Regresar al menú de opciones')
                            opcion1=int(input('Seleccione una opción: ')) #input ha de ser un integer, sino salta a la expeción
                            if opcion1==1: #ALTA MEDICA
                                #comprobar_fechas(fecha)
                                
                                print('\nInformación de la médica a dar de alta: ')
                                #pido por pantalla todos los inputs necesarios para dar de alta una médica, en este caso no ponemos criterios de entrada por pantalla
                                nombre,apellido,direccion,ciudad,cp,telf,email=pedir_datos()
                                nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
                                especialidad=input('-> Especialidad: ') #ningún criterio de entrada de especialidad, no se especifica que tenga que estar dentro del dic_especialidades
                                
                                id_m=len(dic_medicas.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                                password=util.crea_password(nombre,apellido,telf) #creo la contraseña con el metodo de la clase utilidades
                                med=Medica(id_m,nom,direccion,ciudad,cp,telf,email,especialidad,password) #creo el objeto de la clase médica
                                hosp.metodo_alta(med,id_m,recep,'med') #llamada al método de hospital
                                print('Médica dada de alta con éxito')
                            
                            
                            elif opcion1==2: #ALTA PACIENTE
                                
                                print('\nInformación de la paciente a dar de alta: ')
                                nombre,apellido,direccion,ciudad,cp,telf,email=pedir_datos()
                                nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
                                
                                grupos_sanguineos=('AB+','AB-','A+','A-','B+','B-','0+','0-')
                                while True:
                                    grupo_sanguineo=input('-> Grupo Sanguíneo: ') #compruebo que el grupo sanguieno introducido por pantalla estea dentro de la tupla
                                    if grupo_sanguineo in grupos_sanguineos:
                                        id_p=len(dic_pacientes.keys())+1
                                        pac=Paciente(id_p,nom,direccion,ciudad,cp,telf,email,grupo_sanguineo)
                                        hosp.metodo_alta(pac,id_p,recep,'pac')
                                        print('Paciente dada de alta con éxito')
                                        break
                                    else: 
                                        print('No existe tal grupo sanguíneo')
                                        
                            elif opcion1==3: #ALTA ENFERMERA
                                
                                print('\nInformación de la enfermera a dar de alta: ')
                                nombre,apellido,direccion,ciudad,cp,telf,email=pedir_datos()
                                nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
                                
                                categorias=['P:practicante','J:enfermera junior','M:enfermera senior','JE:jefa de enfermeras']
                                print('Categorías disponibles: ',categorias, '\nSeleccione una categoría: ')
    
                                while True:
                                    categoria=input('-> Categoria: ')
                                    if categoria in categorias:
                                        id_e=len(dic_enfermeras.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                                        password=util.crea_password(nombre,apellido,telf)
                                        enf=Enfermera(id_e,nom,direccion,ciudad,cp,telf,email,categoria,password)
                                        hosp.metodo_alta(enf,id_e,recep,'enf')
                                        print('Enfermera dada de alta con éxito')
                                        break
                                    else:
                                        print('No existe tal categoría')
                                        
                            elif opcion1==4: # ALTA RECEPCIONISTA
                                
                                print('\nInformación de la recepcionista a dar de alta: ')
                                nombre,apellido,direccion,ciudad,cp,telf,email=pedir_datos()
                                nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
                                
                                turnos=['1:matutino','2:verspertino','3:nocturno','4:rotatorio']
                                print('Turnos disponibles: ',turnos, '\nSeleccione un turno: ')
    
                                while True:
                                    turno=input('-> Turno: ')
                                    if turno in turnos:
                                        id_r=len(dic_recepcionistas.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                                        password=util.crea_password(nombre,apellido,telf)
                                        recep=Recepcionista(id_r,nom,direccion,ciudad,cp,telf,email,turno,password)
                                        hosp.metodo_alta(recep,id_r,recep,'recep')
                                        print('Recepcionista dada de alta con éxito')
                                        break
                                    else:
                                        print('No existe tal turno')
                                
                            elif opcion1==5: #ALTA ESPECIALIDAD
                                
                                 print('Información de la especialidad a dar de alta: ')
                                 codigo=input('-> Código: ').upper()
                                 if codigo in dic_especialidades.keys():
                                     print('La especialidad ya existe')
                                 elif codigo not in dic_especialidades.keys():
                                    nombre=input('-> Nombre: ').capitalize()
                                    espe=Especialidad(codigo,nombre)
                                    hosp.metodo_alta(espe,codigo,recep,'espe')
                                    print('Especialidad dada de alta con éxito')
                                     
                            elif opcion1==6: #ALTA MEDICAMENTO
                                
                                print('Información sobre le medicamento a dar de alta: ')
                                try:
                                    codigo=int(input('Código: '))
                                    if codigo in dic_medicamentos.keys():
                                        print('El medicamento ya existe')
                                    elif codigo not in dic_medicamentos.keys():
                                        princ_activ=input('Principio Activo: ')
                                        marca=input('Marca: ')
                                        laboratorio=input('Laboratorio: ')
                                        medicamento=Medicamento(codigo,princ_activ,marca,laboratorio)
                                        hosp.metodo_alta(medicamento,codigo,recep,'medicamento')
                                        print('Medicamento dado de alta con éxito')
                                except ValueError:
                                    print('El código han de ser números y enteros')
                                
                            elif opcion1<1 or opcion1>6: #SALIDA MENU ALTAS
                                print('La opcion seleccionada no está disponible')
                                
                        except ValueError:
                            print('Opción seleccionada no válida')
                        
                print('\nHa salido del menú de altas')
                            
                                
            elif opcion==2: #MENU CONSULTAS
                  opcion2=0
                  while opcion2!=10:
                    try:
                        print('\nMenú de consulta\n 1) Médica\n 2) Paciente\n 3) Enfermera\n 4) Recepcionista\n 5) Especialidad\n 6) Medicamento\n 7) Recetas\n 8) Derivaciones\n 9) Medico por especialidad\n 10) Regresar al menú de opciones\n')
                        opcion2=int(input('Seleccione una opción: ')) #input ha de ser un integer, sino salta a la expeción
                        if opcion2==1: #BUSQUEDA MÉDICA
                            opcion3=0
                            while opcion3!=3: 
                                try: 
                                    print('\nOpciones de consulta de médicas\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: '))
                                    if opcion3==1: #busqueda medica por nombre
                                        nom=input('Introduzca el nombre y apellido de la médica: ').title()
                                        if nom.replace(' ','').isalpha()==True:
                                            lista_med=[]
                                            med=hosp.consulta_dics(nom,lista_med,'med')
                                            if med==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna médica con ese nombre
                                                print('\nNo figura una médica con ese nombre')
                                            else: #la lista no está vacía, hay una o más médicas con el nombre introducido
                                                for i in range(len(med)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print('\n -> ',med[i],'\n') #me imprime una flechita por cada médica que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                        
                                    elif opcion3==2: #busqueda medica por identificador 
                                        try:
                                            id_m=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            med=hosp.consulta_ident(id_m,'med') #me devulve el número identificador si existe
                                            if med==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una médica con ese número identificador')
                                            else: #lo ha encontrado
                                                print(med)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')
                                            
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                                                              
                        elif opcion2==2: #BUSQUEDA PACIENTE
                            opcion3=0
                            while opcion3!=3: 
                                try: 
                                    print('\nOpciones de consulta de pacientes\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: '))
                                    if opcion3==1: #busqueda paciente por nombre
                                        nom=input('Introduzca el nombre y apellido de la paciente: ').title()
                                        if nom.replace(' ','').isalpha()==True: #input han de ser letras
                                            pac=hosp.consulta_paciente(nom,recep)
                                            if pac==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna paciente con ese nombre
                                                print('\nNo figura una paciente con ese nombre')
                                            else: #la lista no está vacía, hay una o más pacientes con el nombre introducido
                                                for i in pac: #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print(' -> ',i.muestra_datos(),'\n') #me imprime una flechita por cada paciente que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                    elif opcion3==2: #busqueda paciente por identificador
                                        try:
                                            id_p=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            pac=hosp.consulta_ident(id_p,'pac') #me devulve el número identificador si existe
                                            if pac==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una paciente con ese número identificador')
                                            else: #lo ha encontrado
                                                print(pac)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')     
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')  
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                            
                        elif opcion2==3: #BUSQUEDA ENFERMERA
                            opcion3=0
                            while opcion3!=3: 
                                try: 
                                    print('\nOpciones de consulta de enfermeras\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: '))
                                    if opcion3==1: #busqueda medica por nombre
                                        nom=input('Introduzca el nombre y apellido de la enfermera: ').title()
                                        if nom.replace(' ','').isalpha()==True:
                                            lista_enf=[]
                                            enf=hosp.consulta_dics(nom,lista_enf,'enf')
                                            if enf==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna médica con ese nombre
                                                print('\nNo figura una enfermera con ese nombre')
                                            else: #la lista no está vacía, hay una o más médicas con el nombre introducido
                                                for i in range(len(enf)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print('\n -> ',enf[i],'\n') #me imprime una flechita por cada médica que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                        
                                    elif opcion3==2: #busqueda medica por identificador 
                                        try:
                                            id_e=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            enf=hosp.consulta_ident(id_e,'enf') #me devulve el número identificador si existe
                                            if enf==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una enfermera con ese número identificador')
                                            else: #lo ha encontrado
                                                print(enf)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')
                                            
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                            
                        elif opcion2==4: #BUSQUEDA RECEPCIONISTA  
                            opcion3=0
                            while opcion3!=3: 
                                try: 
                                    print('\nOpciones de consulta de recepcionistas\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: '))
                                    if opcion3==1: #busqueda medica por nombre
                                        nom=input('Introduzca el nombre y apellido de la recepcionista: ').title()
                                        if nom.replace(' ','').isalpha()==True:
                                            lista_recep=[]
                                            recep=hosp.consulta_dics(nom,lista_recep,'recep')
                                            if recep==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna médica con ese nombre
                                                print('\nNo figura una recepcionista con ese nombre')
                                            else: #la lista no está vacía, hay una o más médicas con el nombre introducido
                                                for i in range(len(recep)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print('\n -> ',recep[i],'\n') #me imprime una flechita por cada médica que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                        
                                    elif opcion3==2: #busqueda medica por identificador 
                                        try:
                                            id_r=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            recep=hosp.consulta_ident(id_r,'recep') #me devulve el número identificador si existe
                                            if recep==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una recepcionista con ese número identificador')
                                            else: #lo ha encontrado
                                                print(recep)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')
                                            
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                                    
                        elif opcion2==5: #BUSQUEDA ESPECIALIDAD
                            opcion3=0
                            while opcion3!=3:
                                try:
                                    print('\nOpciones de consulta de especialidades\n 1) Por nombre\n 2) Por código\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: ')) 
                                    if opcion3==1:
                                        nom=input('Introduzca el nombre de la especialidad: ').capitalize()
                                        lista_espe=[]
                                        espe=hosp.consulta_dics(nom,lista_espe,'espe')
                                        if espe==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna médica con ese nombre
                                            print('\nNo figura una especialidad con ese nombre')
                                        else: #la lista no está vacía, hay una o más médicas con el nombre introducido
                                            for i in range(len(espe)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                print('\n -> ',espe[i],'\n') 
                                        
                                    elif opcion3==2:
                                        codigo=input('Introduzca el código de la especialidad: ').upper()
                                        espe=hosp.consulta_cod_espe(codigo)
                                        if espe==None: #no ha encontrado ninguna coincidencia
                                            print('\nNo figura una especialidad con ese código')
                                        else: #lo ha encontrado
                                            print(espe)
                                        
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                                    
                        elif opcion2==6: #BUSQUEDA MEDICAMENTO
                            try:
                                print('\nOpciones de consulta de medicamentos\n')
                                codigo=int(input('Introduzca el código del medicamento: '))
                                medicamento=hosp.consulta_ident(codigo,'medicamento')
                                if medicamento==None: #no ha encontrado ninguna coincidencia
                                    print('\nNo figura una medicamento con ese código')
                                else: #lo ha encontrado
                                    print(medicamento)
                            except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                            
                        elif opcion2==7: #BUSQUEDA RECETAS  
                            nom=input('Nombre y apellido del paciente: ').title()
                            receta=hosp.consulta_recetas(nom)
                            print(receta)
                            #ordenar por diagnostico y especialidades
                            
                            #recetas esta dentro de diagnostico, y -> diagnostio tiene espe,obs,enfe,nommed
                            #for i in revmed: #recorro todas las revisiones que tengo
                                
                                
                            #- fichas tiene una lista con codigo,fecha y diag
                            
                            
                        elif opcion2==8: #BUSQUEDA DERIVACIONES
                            nombre=input('Nombre: ')
                            deriva=hosp.consulta_derivacion(nombre)
                            print(deriva)
                                    
                                    
                        elif opcion2==9: #BUSQUEDA MEDICO POR ESPECIALIDAD
                            especialidad=input('-> Introduzca la especialidad: ').capitalize() #hemos cambaido las claves del diccionario a codigos ya que es mas práctico 
                            meds=hosp.consulta_med_espe(especialidad)
                            if meds==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna médica con ese nombre
                                print('\nNo figura una especialidad con ese nombre')
                            else: #la lista no está vacía, hay una o más médicas con el nombre introducido
                                for i in range(len(meds)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                    print('\n -> ',meds[i],'\n')                        
                                
                                
                        elif opcion2<0 or opcion2>10: #SALIDA'Anarda Monroy'
                            print('la opcion seleccionada no está disponible')
                    except ValueError:
                        print('opcion seleccionada no es valida')
                        
            elif opcion==3: #Menu revisiones
                    opcion4=0
                    while opcion4!=3:
                        try:
                            print('\nMenú revisiones\n 1) Altas revisiones\n 2) Realiza revisión\n 3) Regresa menú de opciones')
                            opcion4=int(input('Selecciones una opción: '))
                            if opcion4==1: #ALTAS REVISIONES
                                print('Inicio sesión enfermera\n')
                                
                                enf=hosp.login('enf') #tendria que ser a cada opcion
                                if enf == 1:
                                    print('\nNo se ha iniciado sesión')
                                elif enf == 2:
                                    print('\nNo existe tal empleada')
                                else:    
                                    nom=input("Introduzca el nombre y apellido de la paciente: ").title()
                                    if nom.replace(' ','').isalpha()==True:
                                        while True:
                                            try:
                                                a=0
                                                fecha=comprobar_fecha()
                                                for i in dic_pacientes:
                                                    if nom in dic_pacientes[i].regresa_nombre():
                                                        pac=dic_pacientes[i]      
                                                        a+=1
                               
                                                if a==0:
                                                    print('No existe tal paciente')
                                                elif a==1:
                                                    enf.asigna_revision(pac,fecha,dic_medicas)
                                                    print('Revisión a',pac.regresa_nombre(),'asignada')
                                                elif a!=1: #más de unx paciente con el nombre introducido
                                                    print('Hay',a,'pacientes con el nombre introducido:')
                                                    for i in dic_pacientes:
                                                        if nom in dic_pacientes[i].regresa_nombre():
                                                            print(dic_pacientes[i].muestra_datos())
                                                    id_p=int(input('Introduzca el número identificador de la paciente a asignar la revisión: '))
                                                    pac=dic_pacientes[id_p]
                                                    enf.asigna_revision(pac,fecha,dic_medicas)
                                                    print('Revisión a',pac.regresa_nombre(),'asignada')
    
                                                break
                                            
                                            except ValueError:
                                                print("\nNo ha introducido una fecha correcta")
                                            
                                            
                            elif opcion4==2: #REALIZAR REVISION
                                print('Inicio sesión médica\n')
                                
                                med=hosp.login('med') #tendria que ser a cada opcion
                                if med == 1:
                                    print('\nNo se ha iniciado sesión')
                                elif med == 2:
                                    print('\nNo existe tal empleada')
                                else:
                                    #mirar si hay pacientes que tenga una fecha actual para realizar la revision
                                    hoy = datetime.now().date()
                                    lista_pacrev=med.pacrev #atendidos
                                    lista_pacnorev=med.pacnorev #lista no atendidos
                                    lista_atender_hoy=[]
                                    for i in lista_pacnorev:
                                        revision=i.revmed
                                        for j in revision:
                                            if j.fecha == hoy: #pasar fecha del formato str a datetime
                                                lista_atender_hoy.append(i)                                        
                                    #IMPRIMIR TODA LA INFO DEL PACIENTE                                  
                                    #mostrar toda la información del paciente, que pasa si tengo varias?
                                    if len(lista_atender_hoy)==0:
                                        print('La médica no tiene ninguna paciente con visita programada para hoy')
                                        break
                                    elif len(lista_atender_hoy)==1:
                                        pac=lista_atender_hoy[0]    
                                    elif len(lista_atender_hoy)!=1:
                                        print('Hay',len(lista_atender_hoy),'pacientes con el nombre introducido: ')
                                        for i in lista_atender_hoy:
                                            print(i.muestra_datos()) #imprimo el id y los datos?
                                        id_p=int(input('Introduzca el número identificador de la paciente a realizar la revisión: '))
                                        for i in lista_atender_hoy:
                                            if id_p==i.id_num:
                                                pac=i #me crea el objeto paciente con el que haya seleccionado
                        #FALTARI PONER LA EXEPCION DE QUE NO EXISTE EL ID
                                                print(pac.muestra_datos())
                                                print('\nPaciente escogido')
                                            #escojo un paciente y ahora prodedo a hacerle la revisión
                                            
                                            
                                    for i in pac.revmed:#recorro todas la revisiones del paciente y cojo solo de con fecha de hoy
                                        if i.fecha==hoy:
                                            rev=i
                                    #revision anterior? pero tener en cuanta entre listas co cosas y una lista de objetos
                                    diag=rev.diag[-1]# cojo el ultimo diagnostico
                                    if diag.derivado==True: #el paciente ya  esta derivado
                                                #MOSTRAR INFO DIAG ANTERIOR
                                        print('\nUltimo diágnostico: ', diag)
                                            #pedimos a la maedica que rellene ls datos de diagnostico
                                    elif diag.derivado==False:#si no esta derivado aun
                                        print('\nDatos a introducir diag: ')
                                        enf=input('Enfermedad: ')
                                        obs=input('Observaciones: ')
                                        diag.observaciones=obs
                                        diag.enfermedad=enf#completo el diagnostico que tenia
                                        print (pac.muestra_datos())   
                                            #preguntamos si quiere expedir receta
                                        expedir=input('Desea expedir receta? Responda si/no: ').lower()
                                        while expedir=='si':
                                            print('Introduza los datos para expedir receta: ')
                                            codigo=int(input('Codigo del medicamento: '))#ponemos el codigo porque es mas facil de buscar al haber varios con el mismo nombre
                                            medicamento=hosp.consulta_ident(codigo,'medicamento')
                                            print (medicamento)
                                            if medicamento==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una medicamento con ese código')
                                            else: #lo ha encontrado
                                                dosis=input('Dosis del medicamento: ')
                                                receta=diag.gen_recet(medicamento,dosis)
                                                expedir=input('Desea expedir otra receta? Responda si/no: ').lower()
                                
                                            #preguntamos si quiere derivar al paciente
                                        derivar=input('Desea derivar a la paciente? Responda si/no: ').lower()
                                        if derivar=='si':
                                            print('Intoduzca los datos necesarios para la derivación: ')
                                                #fecha será la actual, nommed es uno nuevo no?
                                            nommed=input('Nombre y apellido de la médica a la cual derivamos: ').title()
                                            while True:
                                                especialidad=input('Nombre de la especialidad: ')
                                                if especialidad in dic_especialidades:
                                                    diag.derivap(nommed,hoy,especialidad)#guardo la derivacio en el diagnotico
                                                    break
                                                else:
                                                    print('No existe tal especialidad')
                                                    no_derivacion=input('Desea continuar con la derivación? Responda si/no').lower()
                                                    if no_derivacion=='no':
                                                        break
                                                    else:
                                                        pass
                                        
                                        lista_pacnorev.remove(pac)
                                        lista_pacrev.append(pac)
                                            
                                        #NO SE SI FALTARÍA HACERLO CUANDO SOLO TENEMOS UN PACIENTE PARA ATENDER HOY
                                    
                                
#                                else: #si simplemente hay una paciente
#                                    if hosp.consulta_revmed(nom)==[]:
#                                        print('\nEsta paciente no tiene revisiones médicas')
#                                    else:
#                                        print('\nLas revisiones médicas de la paciente',nom,'son:\n',hosp.consulta_revmed(nom))
                                            
                            elif opcion4<1 or opcion4>3:#SALIDA
                               print('la opcion seleccionada no está disponible')
                                
                            
                        except ValueError:
                            print('La opción seleccionada no es válida, por favor, seleccione otra opción')

            elif opcion==4:# menu de archivos
                opcion5=0
                while opcion5!=4:
                    try:
                        print('\nMenú revisiones\n 1) Medicos\n 2) Historial de un paciente\n 3) Enfermeras\n 4) Recepcionistas\n 5) Regresa menú de opciones')
                        opcion5=int(input('Selecciones una opción: '))
                        if opcion5==1: #ARCHIVO MEDICAS
                            hosp.archivo_medicas()
                            print('\nSe ha generado el archivo')
                        elif opcion5==2: #ARCHIVO PACIENTES
                            nom=input("Introduzca el nombre y apellido de la paciente: ").title()
                            pac=hosp.consulta_paciente(nom,recep)
                            if pac==[]:
                                print('No existe tal paciente')
                            elif len(pac)==1:
                                pac=pac[0]#saco el objeto paciente de su lista
                                #ESTAMOS RENOMBRANDO LA MISMA VARIABLE, NO SE SI TIENE SENTIDO
                            elif len(pac)!=1: #más de unx paciente con el nombre introducido
                                print('\nHay',len(pac),'pacientes con el nombre introducido:')
                                for i in pac:
                                    print(i.muestra_datos())
                                id_p=int(input('Introduzca el número identificador de la paciente a la que quieras el historial: '))
                                pac=dic_pacientes[id_p]
                            espe=hosp.archivo_pacientes(pac)
                            print(espe)
                        elif opcion5==3: #ARCHIVO ENFERMERAS
                            estad=hosp.archivo_enf()
                            print('\nSe ha generado el archivo')
                            print(estad)
                        elif opcion5==4: #ARCHIVO RECEPCIONISTAS
                            estad=hosp.archivo_recep()
                            print('\nSe ha generado el archivo')
                            print(estad)
                        elif opcion5<1 or opcion5>5: #SALIDA
                            print('la opcion seleccionada no está disponible')
                    except ValueError:
                        print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                            
                        
            elif opcion<1 or opcion>4:
                print('\nLa opción seleccionada no está disponible')
                
        except ValueError: #en el caso de que haya introducido algo erroneo como opcion
            print('La opción seleccionada no es válida, por favor, seleccione otra opción')
    print('\nHa salido del menú')
    
if __name__=='__main__':
    main()