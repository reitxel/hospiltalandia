# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:57:24 2020

@author: berta
"""


a=datetime.date(2004,18,1)
b=datetime.date(2004,2,3)
c=datetime.date(2005,2,1),
d=datetime.date(2004,5,1)
lista=[a,b,c,d]
lista.sorted()
print (lista)
#
##
#date_str=input('\nIntroduzca la fecha de revisión en formato "dd-mm-aaaa": ')
#date_object = datetime.strptime(date_str,'%m-%d-%Y').date()
#print(date_object) 
#from datetime import datetime
#from datetime import date
#
#
#while True:
#    try:
#        fecha_str=input('\nIntroduzca la fecha de revisión en formato "dd-mm-aaaa": ')#criterio para que la fecha que me introduzca por pantalla mantenga este formato
#        fecha = datetime.strptime(fecha_str,'%d-%m-%Y').date()
#        hoy = datetime.now().date()
#        print(hoy,fecha)
#        if str(fecha)>=str(hoy):
#            print(fecha)
#            break
#        elif str(fecha) < str(hoy):
#            print('La fecha es anterior a la actual')
#    except ValueError:
#        print("\nNo ha introducido una fecha correcta")
list_espe=['a','d','g','e','y','s','h','u','r','t','t','s','s']       
list_una_espe=[]
for i in list_espe:#creo una llista amb UNA vegada cada especialitat
    if i not in list_una_espe:
        list_una_espe.append(i)
    lista_estadi=[]
    for i in list_una_espe:
        n=list_espe.count(i)#me cuenta cuantas veces aparece en la lista
        lista_estadi.append([i,n])
print(lista_estadi)

    
