# -*- coding: utf-8 -*-
from graficos import Interface
from hospital import Hospital
from utilidades import Utilidades

def main():
    util=Utilidades() #creo objeto de la clase Utilidades
    dic_especialidades,dic_medicas,dic_pacientes,dic_enfermeras,dic_recepcionistas,dic_medicamentos,lista_hosp=util.lectura('especialidades.csv','informacion.csv','medicina.csv') #llamada al metodo de Utilidades para guardar lo que nos devuelve en variables 
    hospi=Hospital(lista_hosp[0],lista_hosp[1],lista_hosp[2],lista_hosp[3],lista_hosp[4],None,dic_pacientes,dic_medicas,dic_especialidades,dic_enfermeras,dic_recepcionistas,dic_medicamentos) #creo el objeto de hospital donde los primeros parámetros los toma de la lista de info hospital
#    recep=dic_recepcionistas[1] #objeto de la clase Recepcionista
#    enf=dic_enfermeras[1]
    # Crear hospita
    # U=Utilidades()
    # nom,dire,ciudad,cp,tel,dicmed,dicpac,dicesp,dicrecp,dicenf=U.lectura("informacion.csv","especialidades.csv")
    # hospi=Hospital(nom,dire,ciudad,cp,tel,None,dicmed,dicpac,dicesp,dicrecp,dicenf)

    # Crear interface
    MainWindow = Interface(hospi)
    MainWindow.create_main_window()
    
    
    
if __name__=="__main__":
    main()
