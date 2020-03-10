# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:57:24 2020

@author: berta
"""



#
##
#date_str=input('\nIntroduzca la fecha de revisión en formato "dd-mm-aaaa": ')
#date_object = datetime.strptime(date_str,'%m-%d-%Y').date()
#print(date_object) 
from datetime import datetime
from datetime import date


while True:
    try:
        fecha_str=input('\nIntroduzca la fecha de revisión en formato "dd-mm-aaaa": ')#criterio para que la fecha que me introduzca por pantalla mantenga este formato
        fecha = datetime.strptime(fecha_str,'%d-%m-%Y').date()
        hoy = datetime.now().date()
        print(hoy,fecha)
        if str(fecha)>=str(hoy):
            print(fecha)
            break
        elif str(fecha) < str(hoy):
            print('La fecha es anterior a la actual')
    except ValueError:
        print("\nNo ha introducido una fecha correcta")

    
