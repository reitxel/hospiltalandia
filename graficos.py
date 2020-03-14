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
        self.mAltas.add_command(label="Alta de paciente", command= self.alta_paciente)#per cada submenu creeem les difrerentes opcions
        self.mAltas.add_command(label="Alta de médica", command= self.alta_medica)#el comand diu que cuan la cliclo pasara algo
        self.mAltas.add_command(label="Alta de enfermera", command= self.alta_enfermera)
        self.mAltas.add_command(label="Alta de recepcionista", command= self.alta_recepcionista)
        self.mAltas.add_command(label="Alta de especialidad", command= self.alta_especialidad)
        self.mAltas.add_command(label="Alta de medicamento", command= self.alta_medicamento)

        self.mConsultas.add_command(label="Consulta de paciente", command = self.consulta_paciente)
        self.mConsultas.add_command(label="Consulta de médica", command = self.consulta_medica)
        self.mConsultas.add_command(label="Consulta de enfermera", command = self.consulta_enfermera)
        self.mConsultas.add_command(label="Consulta de recepcionista", command = self.consulta_recepcionista)
        self.mConsultas.add_command(label="Consulta de especialidad", command = self.consulta_especialidad)
        self.mConsultas.add_command(label="Consulta de medicamento", command = self.consulta_medicamento)
        self.mConsultas.add_command(label="Consulta de recetas", command = self.consulta_recetas)
        self.mConsultas.add_command(label="Consulta de derivaciones", command = self.consulta_derivaciones)
        self.mConsultas.add_command(label="Consulta de médica por especialidad", command = self.consulta_med_espe)
                
        self.mRevisiones.add_command(label= "Alta de revisiones")
        self.mRevisiones.add_command(label= "Realizar revisión")

        self.mArchivos.add_command(label= "Informe de médicas")
        self.mArchivos.add_command(label= "Historial de una paciente")
        self.mArchivos.add_command(label= "Informe de enfermeras")
        self.mArchivos.add_command(label= "Informe de recepcionistas")
        
        self.mSalir.add_command(label= "Salida", command= self.v.destroy)# per eleminar uan finestra

        #Agregar menus a la barra
        self.barraMenu.add_cascade(label = "Altas", menu= self.mAltas)#eslicitament diem els menus son les etiquetes del menu que veiem
        self.barraMenu.add_cascade(label = "Consultas", menu= self.mConsultas)
        self.barraMenu.add_cascade(label = "Revisiones", menu= self.mRevisiones)
        self.barraMenu.add_cascade(label = "Archivos", menu= self.mArchivos)
        self.barraMenu.add_cascade(label = "Salida", menu= self.mSalir)
        
        #Indicar que la barra de menú está en la ventana
        self.v.config(menu = self.barraMenu)#modifiquem el confi( es necessari)
        self.v.mainloop()
    
    
    def comprobar_recep(self):
        
        v_comprobar = tk.Toplevel(self.v)#creo la finestra
        v_comprobar.geometry("350x350")
        v_comprobar.title("Login recepcionsita")    
        
        
        etiq_nom = tk.Label(v_comprobar, text= "Nombre:")
        etiq_nom.grid(column=0, row=1)#posicio
        v_nom = tk.StringVar()
        v_nom.set("")
        e_nom = tk.Entry(v_comprobar, textvariable=v_nom)#li pos la finestre i el lligo amb una variavbel 'v_nom'
        e_nom.grid(column=1, row=1)
        
        etiq_contra = tk.Label(v_comprobar, text= "Contraseña:")
        etiq_contra.grid(column=0, row=2)#posicio
        v_contra = tk.StringVar()
        v_contra.set("")
        e_contra = tk.Entry(v_comprobar, textvariable=v_contra)#li pos la finestre i el lligo amb una variavbel 'v_nom'
        e_contra.grid(column=1, row=2)
        
        login_recep_params=partial(self.comprobar_recep_aux, v_nom, v_contra,v_comprobar)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_comprobar,text="Asignar", command = login_recep_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_comprobar,text="Sortir", command = v_comprobar.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_comprobar.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_comprobar.grab_set()
        self.v.wait_window(v_comprobar)
        
#        nom=self.nom.get()
#        contra=self.contra.get()
#        recep=self.Hospital.login_recep(nom,contra)
#        if recep==log:
#            return recep

    def comprobar_recep_aux(self,nom,contra,v_comprobar):
        if not all([nom.get(), contra.get()]):# NOMES SEXECUTA AL CLICAL AL BOTO
            messagebox.showinfo(title='Error', message='Alguno de los campos está vacío')#COMPROBACIO QUE CAP DELS CAMPS ESTIGUU SOL
        else:
            log=self.Hospital.log_recep(nom.get(),contra.get())
            if log==False:
                 messagebox.showinfo(title='Error', message='No existe esta recepcionista, o la contraseña es incorrecta')
            else:
                messagebox.showinfo(title='Correcto', message='Bienvenido!') 
            v_comprobar.destroy()
            
    
    def alta_paciente(self):
        """
        Función que implementa una ventana para hacer el alta de una paciente. 
        """
        #Prepara la finestra
        v_ingreso = tk.Toplevel(self.v)#creo la finestra
        v_ingreso.geometry("350x350")
        v_ingreso.title("Alta de paciente")    
    
        etiq_0= tk.Label(v_ingreso, text= "Insertar datos de la paciente nueva")#etiqueta 0 es letiqueta de dalt de tot
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
        etiq_ciudad = tk.Label(v_ingreso, text= "Ciutad:")
        etiq_ciudad.grid(column=0, row=3)
        v_ciudad = tk.StringVar()
        v_ciudad.set("")
        e_ciudad = tk.Entry(v_ingreso, textvariable=v_ciudad)
        e_ciudad.grid(column=1, row=3)

        # Codi postal
        etiq_cp = tk.Label(v_ingreso, text= "Código Postal:")
        etiq_cp.grid(column=0, row=4)
        v_cp = tk.StringVar()
        v_cp.set("")
        e_cp = tk.Entry(v_ingreso, textvariable=v_cp)
        e_cp.grid(column=1, row=4)

        # Telefon
        etiq_tlf = tk.Label(v_ingreso, text= "Teléfono:")
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
        etiq_sang = tk.Label(v_ingreso, text= "Grupo sanguíneo:")
        etiq_sang.grid(column=0, row=7)
        grupos_sanguineos = ['O+','A+','B+','O-','A-','AB+','B-','AB-']
        spin_sang = ttk.Combobox(v_ingreso, values=grupos_sanguineos)#un desplegable a comobox no cal assignarli variable
        spin_sang.grid(column=1, row=7)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.alta_pac_aux, v_nom, v_dir, v_ciudad, v_cp, v_tlf, v_email, spin_sang, v_ingreso)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_ingreso,text="Asignar", command = alta_pac_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_ingreso,text="Salida", command = v_ingreso.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingreso.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingreso.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingreso)# QUE LA VENTANA ORIGINAL ESPERA HASTA QUE LA ACTUAL PETE

    def alta_pac_aux(self, nom, dire, ciudad, cp, tlf, email, sang, v_ingreso):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si algun esta empty
        if not all([nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), sang.get()]):# NOMES SEXECUTA AL CLICAL AL BOTO
            messagebox.showinfo(title='Error', message='Alguno de los campos está vacío')#COMPROBACIO QUE CAP DELS CAMPS ESTIGUU SOL
        else:
            # Cridar a alta d'hospital
            self.Hospital.alta_pac(nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), sang.get())
            messagebox.showinfo(title='Añadida', message='La paciente ha sido añadida!')
            v_ingreso.destroy()
            

    def alta_medica(self):
        v_ingreso = tk.Toplevel(self.v)#creo la finestra
        v_ingreso.geometry("350x350")
        v_ingreso.title("Alta de médica")    
    
        etiq_0= tk.Label(v_ingreso, text= "Insertar datos de la nueva médica:")#etiqueta 0 es letiqueta de dalt de tot
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
        etiq_ciudad = tk.Label(v_ingreso, text= "Ciutad:")
        etiq_ciudad.grid(column=0, row=3)
        v_ciudad = tk.StringVar()
        v_ciudad.set("")
        e_ciudad = tk.Entry(v_ingreso, textvariable=v_ciudad)
        e_ciudad.grid(column=1, row=3)

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
        etiq_espe = tk.Label(v_ingreso, text= "Especialidad:")
        etiq_espe.grid(column=0, row=7)
        especialidades = self.Hospital.comprobar_especialidad()
        spin_espe = ttk.Combobox(v_ingreso, values=especialidades)#un desplegable a comobox no cal assignarli variable
        spin_espe.grid(column=1, row=7)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_med_params=partial(self.alta_med_aux, v_nom, v_dir, v_ciudad, v_cp, v_tlf, v_email, spin_espe, v_ingreso)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_ingreso,text="Asignar", command = alta_med_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_ingreso,text="Salida", command = v_ingreso.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingreso.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingreso.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingreso)# QUE LA VENTANA ORIGINAL ESPERA HASTA QUE LA ACTUAL PETE
        
    def alta_med_aux(self, nom, dire, ciudad, cp, tlf, email, espe, v_ingreso):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si algun esta empty
        if not all([nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), espe.get()]):# NOMES SEXECUTA AL CLICAL AL BOTO
            messagebox.showinfo(title='Error', message='Alguno de los campos está vacío')#COMPROBACIO QUE CAP DELS CAMPS ESTIGUU SOL
        else:
            # Cridar a alta d'hospital
            self.Hospital.alta_med(nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), espe.get())
            messagebox.showinfo(title='Añadida', message='La médica ha sido añadida!')
            v_ingreso.destroy()
        
    def alta_enfermera(self):
        v_ingreso = tk.Toplevel(self.v)#creo la finestra
        v_ingreso.geometry("350x350")
        v_ingreso.title("Alta de enfermera")    
    
        etiq_0= tk.Label(v_ingreso, text= "Insertar datos de la nueva enfermera:")#etiqueta 0 es letiqueta de dalt de tot
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
        etiq_ciudad = tk.Label(v_ingreso, text= "Ciutad:")
        etiq_ciudad.grid(column=0, row=3)
        v_ciudad = tk.StringVar()
        v_ciudad.set("")
        e_ciudad = tk.Entry(v_ingreso, textvariable=v_ciudad)
        e_ciudad.grid(column=1, row=3)

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
        etiq_cat = tk.Label(v_ingreso, text= "Categoría:")
        etiq_cat.grid(column=0, row=7)
        categorias = ['P:practicante','J:enfermera junior','M:enfermera senior','JE:jefa de enfermeras'] 
        spin_cat = ttk.Combobox(v_ingreso, values=categorias)#un desplegable a comobox no cal assignarli variable
        spin_cat.grid(column=1, row=7)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_enf_params=partial(self.alta_enf_aux, v_nom, v_dir, v_ciudad, v_cp, v_tlf, v_email, spin_cat, v_ingreso)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_ingreso,text="Asignar", command = alta_enf_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_ingreso,text="Salida", command = v_ingreso.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingreso.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingreso.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingreso)# QUE LA VENTANA ORIGINAL ESPERA HASTA QUE LA ACTUAL PETE
        
    def alta_enf_aux(self, nom, dire, ciudad, cp, tlf, email, cat, v_ingreso):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si algun esta empty
        if not all([nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), cat.get()]):# NOMES SEXECUTA AL CLICAL AL BOTO
            messagebox.showinfo(title='Error', message='Alguno de los campos está vacío')#COMPROBACIO QUE CAP DELS CAMPS ESTIGUU SOL
        else:
            # Cridar a alta d'hospital
            self.Hospital.alta_enf(nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), cat.get())
            messagebox.showinfo(title='Añadida', message='La recepcionista ha sido añadida!')
            v_ingreso.destroy()
            
            
    def alta_recepcionista(self):
        v_ingreso = tk.Toplevel(self.v)#creo la finestra
        v_ingreso.geometry("350x350")
        v_ingreso.title("Alta de recepcionista")    
    
        etiq_0= tk.Label(v_ingreso, text= "Insertar datos de la nueva recepcionista:")#etiqueta 0 es letiqueta de dalt de tot
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
        etiq_ciudad = tk.Label(v_ingreso, text= "Ciutad:")
        etiq_ciudad.grid(column=0, row=3)
        v_ciudad = tk.StringVar()
        v_ciudad.set("")
        e_ciudad = tk.Entry(v_ingreso, textvariable=v_ciudad)
        e_ciudad.grid(column=1, row=3)

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
        etiq_turn = tk.Label(v_ingreso, text= "Turno:")
        etiq_turn.grid(column=0, row=7)
        turnos = ['1:matutino','2:verspertino','3:nocturno','4:rotatorio']
        spin_turn = ttk.Combobox(v_ingreso, values=turnos)#un desplegable a comobox no cal assignarli variable
        spin_turn.grid(column=1, row=7)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_recep_params=partial(self.alta_enf_aux, v_nom, v_dir, v_ciudad, v_cp, v_tlf, v_email, spin_turn, v_ingreso)# PASO LA FUNCIO I TOTS ELS PARAMETRES QUE VULL QUE TINGUI LA FUNCIO, AIXO SI QUE HO PUC POSAR AL COMMAND

        # Programar botó
        btnAsignar=tk.Button(v_ingreso,text="Asignar", command = alta_recep_params).grid(column=0,row=8)#creo dos botons, no li puc passa parametres, solcuio posa un self dabant de toss el v_ o importar la funcio PARTIAL
        btnSortir=tk.Button(v_ingreso,text="Salida", command = v_ingreso.destroy).grid(column=1,row=8)#destrueixo la finestra per tant surto

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingreso.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingreso.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingreso)# QUE LA VENTANA ORIGINAL ESPERA HASTA QUE LA ACTUAL PETE
        
    def alta_med_aux(self, nom, dire, ciudad, cp, tlf, email, turn, v_ingreso):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si algun esta empty
        if not all([nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), turn.get()]):# NOMES SEXECUTA AL CLICAL AL BOTO
            messagebox.showinfo(title='Error', message='Alguno de los campos está vacío')#COMPROBACIO QUE CAP DELS CAMPS ESTIGUU SOL
        else:
            # Cridar a alta d'hospital
            self.Hospital.alta_enf(nom.get(), dire.get(), ciudad.get(), cp.get(), tlf.get(), email.get(), turn.get())
            messagebox.showinfo(title='Añadida', message='La recepcionista ha sido añadida!')
            v_ingreso.destroy() 
    
    def consulta_paciente(self):
        """
        Funció que implementa una finestra amb la consulta de pacient.
        """
        #Prepara la finestra
        v_consulta = tk.Toplevel(self.v)
        v_consulta.geometry("350x350")
        v_consulta.title("Consulta paciente")    
    
        etiq_0= tk.Label(v_consulta, text= "Insertar el nombre a buscar:")
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
