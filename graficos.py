"""
Class implementing a graphical interface for the Hospital.
"""

import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import messagebox

class Interface():

    def __init__(self, Hospital):
        self.v = tk.Tk()
        self.v.geometry("600x480")
        self.v.title("Gestió de l'hospital")
        self.Hospital=Hospital

    def create_main_window(self):
        """
        Crear menú principal.

        Tindrà menus per cada opció del menú.
        """

        #Barra de menu
        self.barraMenu=tk.Menu(self.v)#finestra on estem crean el menu

        # Diferents opcions
        self.mAltas = tk.Menu(self.barraMenu, tearoff=0)# submenus (els que apareixen a dalt)
        self.mConsultas = tk.Menu(self.barraMenu, tearoff=0)
        self.mRevisiones = tk.Menu(self.barraMenu, tearoff=0)
        self.mArchivos = tk.Menu(self.barraMenu, tearoff=0)
        self.mSalir = tk.Menu(self.barraMenu, tearoff=0)

        #Comandos
        self.mAltas.add_command(label="Alta de pacient", command= self.alta_paciente)#per cada submenu creeem les difrerentes opcions
        self.mAltas.add_command(label="Alta de metge")#el comand diu que cuan la cliclo pasara algo
        self.mAltas.add_command(label="Alta de enfermera")
        self.mAltas.add_command(label="Alta de recepcionista")
        self.mAltas.add_command(label="Alta de especialitat")
        self.mAltas.add_command(label="Alta de medicament")

        self.mConsultas.add_command(label="Consulta de pacient", command = self.consulta_paciente)
        self.mConsultas.add_command(label="Consulta de metge")
        self.mConsultas.add_command(label="Consulta de infermera")
        self.mConsultas.add_command(label="Consulta de recepcionista")
        self.mConsultas.add_command(label="Consulta de especialitat")
        self.mConsultas.add_command(label="Consulta de medicament")
        self.mConsultas.add_command(label="Consulta de receptes")
        self.mConsultas.add_command(label="Consulta de derivacions")
        self.mConsultas.add_command(label="Consulta de metge per especialitat")
                
        self.mRevisiones.add_command(label= "Alta de revisions")
        self.mRevisiones.add_command(label= "Realitzar revisió")

        self.mArchivos.add_command(label= "Informe de metges")
        self.mArchivos.add_command(label= "Historial d'un pacient")
        self.mArchivos.add_command(label= "Informe d'infermeres")
        self.mArchivos.add_command(label= "Informe de recepcionistes")
        
        self.mSalir.add_command(label= "Sortir", command= self.v.destroy)# per eleminar uan finestra

        #Agregar menus a la barra
        self.barraMenu.add_cascade(label = "Altes", menu= self.mAltas)#eslicitament diem els menus son les etiquetes del menu que veiem
        self.barraMenu.add_cascade(label = "Consultes", menu= self.mConsultas)
        self.barraMenu.add_cascade(label = "Revisions", menu= self.mRevisiones)
        self.barraMenu.add_cascade(label = "Arxius", menu= self.mArchivos)
        self.barraMenu.add_cascade(label = "Sortir", menu= self.mSalir)
        
        #Indicar que la barra de menú está en la ventana
        self.v.config(menu = self.barraMenu)#modifiquem el confi( es necessari)
        self.v.mainloop()
        
    
    def alta_paciente(self):
        """
        Funció que implementa una finestra per fer l'alta de pacient. 
        """
        #Prepara la finestra
        v_ingreso = tk.Toplevel(self.v)#creo la finestra
        v_ingreso.geometry("350x350")
        v_ingreso.title("Alta de pacient")    
    
        etiq_0= tk.Label(v_ingreso, text= "Inserir dades del pacient nou:")#etiqueta 0 es letiqueta de dalt de tot
        etiq_0.grid(column=0, row=0)#posicio

        # Nom
        etiq_nom = tk.Label(v_ingreso, text= "Nom:")
        etiq_nom.grid(column=0, row=1)#posicio
        v_nom = tk.StringVar()
        v_nom.set("")
        e_nom = tk.Entry(v_ingreso, textvariable=v_nom)#li pos la finestre i el lligo amb una variavbel 'v_nom'
        e_nom.grid(column=1, row=1)
        
        # Dirección
        etiq_dir = tk.Label(v_ingreso, text= "Direcció:")
        etiq_dir.grid(column=0, row=2)
        v_dir = tk.StringVar()
        v_dir.set("")
        e_dir = tk.Entry(v_ingreso, textvariable=v_dir)
        e_dir.grid(column=1, row=2)

        # Ciutat
        etiq_ciutat = tk.Label(v_ingreso, text= "Ciutat:")
        etiq_ciutat.grid(column=0, row=3)
        v_ciutat = tk.StringVar()
        v_ciutat.set("")
        e_ciutat = tk.Entry(v_ingreso, textvariable=v_ciutat)
        e_ciutat.grid(column=1, row=3)

        # Codi postal
        etiq_cp = tk.Label(v_ingreso, text= "Codi Postal:")
        etiq_cp.grid(column=0, row=4)
        v_cp = tk.StringVar()
        v_cp.set("")
        e_cp = tk.Entry(v_ingreso, textvariable=v_cp)
        e_cp.grid(column=1, row=4)

        # Telefon
        etiq_tlf = tk.Label(v_ingreso, text= "Telèfon:")
        etiq_tlf.grid(column=0, row=5)
        v_tlf = tk.StringVar()
        v_tlf.set("")
        e_tlf = tk.Entry(v_ingreso, textvariable=v_tlf)
        e_tlf.grid(column=1, row=5)
               
        # email
        etiq_email = tk.Label(v_ingreso, text= "Email:")
        etiq_email.grid(column=0, row=6)
        v_email = tk.StringVar()
        v_email.set("")
        e_email = tk.Entry(v_ingreso, textvariable=v_email)
        e_email.grid(column=1, row=6)
        
        # Grup sanguini (desplegable)
        etiq_sang = tk.Label(v_ingreso, text= "Grup sanguini:")
        etiq_sang.grid(column=0, row=7)
        grup_sanguini = ['O+','A+','B+','O-','A-','AB+','B-','AB-']
        spin_sang = ttk.Combobox(v_ingreso, values=grup_sanguini)#un desplegable a comobox no cal assignarli variable
        spin_sang.grid(column=1, row=7)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.alta_pac_aux, v_nom, v_dir, v_ciutat, v_cp, v_tlf, v_email, spin_sang, v_ingreso)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_ingreso,text="Asignar", command = alta_pac_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_ingreso,text="Sortir", command = v_ingreso.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingreso.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingreso.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingreso)# QUE LA VENTANA ORIGINAL ESPERA HASTA QUE LA ACTUAL PETE

    def alta_pac_aux(self, nom, dire, ciutat, cp, tlf, email, sang, v_ingreso):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si algun esta empty
        if not all([nom.get(), dire.get(), ciutat.get(), cp.get(), tlf.get(), email.get(), sang.get()]):# NOMES SEXECUTA AL CLICAL AL BOTO
            messagebox.showinfo(title='Error', message='Alguno de los campos está vacío')#COMPROBACIO QUE CAP DELS CAMPS ESTIGUU SOL
        else:
            # Cridar a alta d'hospital
            self.Hospital.alta_pac(nom.get(), dire.get(), ciutat.get(), cp.get(), tlf.get(), email.get(), sang.get())
            messagebox.showinfo(title='Afegit', message='Afegit el pacient!')
            v_ingreso.destroy()

    def alta_medico(self):
        v_ingreso = tk.Toplevel(self.v)#creo la finestra
        v_ingreso.geometry("350x350")
        v_ingreso.title("Alta de médico")    
    
        etiq_0= tk.Label(v_ingreso, text= "Inserir datos del nuevo médico:")#etiqueta 0 es letiqueta de dalt de tot
        etiq_0.grid(column=0, row=0)#posicio

        # Nom
        etiq_nom = tk.Label(v_ingreso, text= "Nombre:")
        etiq_nom.grid(column=0, row=1)#posicio
        v_nom = tk.StringVar()
        v_nom.set("")
        e_nom = tk.Entry(v_ingreso, textvariable=v_nom)#li pos la finestre i el lligo amb una variavbel 'v_nom'
        e_nom.grid(column=1, row=1)
        
        # Dirección
        etiq_dir = tk.Label(v_ingreso, text= "Dirección:")
        etiq_dir.grid(column=0, row=2)
        v_dir = tk.StringVar()
        v_dir.set("")
        e_dir = tk.Entry(v_ingreso, textvariable=v_dir)
        e_dir.grid(column=1, row=2)

        # Ciutat
        etiq_ciutat = tk.Label(v_ingreso, text= "Ciutad:")
        etiq_ciutat.grid(column=0, row=3)
        v_ciutat = tk.StringVar()
        v_ciutat.set("")
        e_ciutat = tk.Entry(v_ingreso, textvariable=v_ciutat)
        e_ciutat.grid(column=1, row=3)

        # Codi postal
        etiq_cp = tk.Label(v_ingreso, text= "Codigo Postal:")
        etiq_cp.grid(column=0, row=4)
        v_cp = tk.StringVar()
        v_cp.set("")
        e_cp = tk.Entry(v_ingreso, textvariable=v_cp)
        e_cp.grid(column=1, row=4)

        # Telefon
        etiq_tlf = tk.Label(v_ingreso, text= "Telefono:")
        etiq_tlf.grid(column=0, row=5)
        v_tlf = tk.StringVar()
        v_tlf.set("")
        e_tlf = tk.Entry(v_ingreso, textvariable=v_tlf)
        e_tlf.grid(column=1, row=5)
               
        # email
        etiq_email = tk.Label(v_ingreso, text= "Email:")
        etiq_email.grid(column=0, row=6)
        v_email = tk.StringVar()
        v_email.set("")
        e_email = tk.Entry(v_ingreso, textvariable=v_email)
        e_email.grid(column=1, row=6)
        
        # Grup sanguini (desplegable)
        etiq_sang = tk.Label(v_ingreso, text= "Especialidad:")
        etiq_sang.grid(column=0, row=7)
        grup_sanguini = ['O+','A+','B+','O-','A-','AB+','B-','AB-']
        spin_sang = ttk.Combobox(v_ingreso, values=grup_sanguini)#un desplegable a comobox no cal assignarli variable
        spin_sang.grid(column=1, row=7)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.alta_pac_aux, v_nom, v_dir, v_ciutat, v_cp, v_tlf, v_email, spin_sang, v_ingreso)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_ingreso,text="Asignar", command = alta_pac_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_ingreso,text="Sortir", command = v_ingreso.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingreso.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingreso.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingreso)# QUE LA VENTANA ORIGINAL ESPERA HASTA QUE LA ACTUAL PETE
            
    def consulta_paciente(self):
        """
        Funció que implementa una finestra amb la consulta de pacient.
        """
        #Prepara la finestra
        v_consulta = tk.Toplevel(self.v)
        v_consulta.geometry("350x350")
        v_consulta.title("Consulta pacient")    
    
        etiq_0= tk.Label(v_consulta, text= "Inserir nom del pacient a buscar:")
        etiq_0.grid(column=0, row=0)

        # Nom
        etiq_nom = tk.Label(v_consulta, text= "Nom:")
        etiq_nom.grid(column=0, row=1)
        v_nom = tk.StringVar()
        v_nom.set("")
        e_nom = tk.Entry(v_consulta, textvariable=v_nom)
        e_nom.grid(column=1, row=1)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.consulta_pac_aux, v_nom, v_consulta)

        # Programar botó
        btnAsignar=tk.Button(v_consulta,text="Consultar", command = alta_pac_params).grid(column=0,row=8)
        btnSortir=tk.Button(v_consulta,text="Sortir", command = v_consulta.destroy).grid(column=1,row=8)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_consulta.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_consulta.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_consulta)

    def consulta_pac_aux(self, nom, v_consulta):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si esta empty
        if not nom.get():
            messagebox.showinfo(title='Error', message='No ha introduit cap nom!')
        else:
            # Cridar a alta d'hospital
            result = self.Hospital.mpaciente(nom.get())
            if not result:
                messagebox.showinfo(title='Error', message='Pacient no trobat!')
            else:
                messagebox.showinfo(title='Pacient', message=result.muestra_datos())
