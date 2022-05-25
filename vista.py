from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Frame
from tkinter import Text
from tkinter import Button
from tkinter import Scrollbar
from tkinter import Menu
from tkinter import NS
from tkinter import ttk
from modelo import Funcion
from menu_cascada import MenuCascada


class Ventana():

    def __init__(self, root):
        
        self.root = root
        self.funcion = Funcion()
        #-----------------Menú------------------
        self.menu_c()

        
        #-----------------Configuración de ventana----------#
        
        #root.geometry('900x850')
        a = self.root.config(bg='#c8c6ae')
        self.root.title('HisC 1.2.1')

        #--------------Configuración de Frame1-------------#
        caja_1 = Frame(self.root, bg='#c8c6ae', width=900, height=300)
        caja_1.grid(row=0, column=0)

        #----------------TITULOS------------------------------

        apellido = Label(caja_1, 
                        text='Apellido:',
                        bg='#c8c6ae', 
                        font='Arial 12')
        apellido.grid(row=0, column=0, sticky='e')


        nombre = Label(caja_1, text='Nombre:',bg='#c8c6ae', font='Arial 12')
        nombre.grid(row=1, column=0, sticky= 'e')

        obra_social = Label(caja_1, 
                            text='Obra Social:',
                            bg='#c8c6ae', 
                            font='Arial 12'
                            )
        obra_social.grid(row=2, column=0, sticky='e')
        obra_social.config(pady=4)

        dni = Label(caja_1, text='DNI:',bg='#c8c6ae', font='Arial 12')
        dni.grid(row=3, column=0, sticky='e')

        historia_clinica = Label(caja_1, 
                                text='    Historia Clínica:', 
                                bg='#c8c6ae', 
                                font='Arial 13' )
        historia_clinica.grid(row=0, column=2, rowspan=4, sticky='e')

        #-------------------ENTRADAS DE TEXTO-----------------------

        self.var_ape = StringVar()
        self.var_nom = StringVar()
        self.var_obra_s = StringVar()
        self.var_dni = IntVar()
        
        self.var_dni.set('')

        self.en_apellido = Entry(caja_1, font='arial 12',
                                    textvariable=self.var_ape)
        self.en_apellido.config(state='disabled')
        self.en_apellido.focus()
        self.en_apellido.grid(row=0, column=1)

        self.en_nombre = Entry(caja_1, font='arial 12', 
                                textvariable=self.var_nom)
        self.en_nombre.config(state='disabled')
        self.en_nombre.grid(row=1, column=1)

        self.en_obra = Entry(caja_1, font='arial 12', 
                            textvariable=self.var_obra_s)
        self.en_obra.config(state='disabled')
        self.en_obra.grid(row=2, column=1)

        self.en_dni = Entry(caja_1, font='arial 12', 
                            textvariable=self.var_dni)
        self.en_dni.config(state='disabled')
        self.en_dni.grid(row=3, column=1)

        #----------------- ENTRADA DE TEXTO 1000 CARACTERES --------------

        self.en_resumen = Text(caja_1, font='arial 10', width=50, height=10)
        self.en_resumen.config(state='disabled')
        self.en_resumen.grid(row=0, column=4, rowspan=4, columnspan=4)
        
        #----------------- BOTONES  -------------------
        caja_2 = Frame(self.root, bg='#c8c6ae', width=900, height=300)
        caja_2.grid(row=4, column=0)

        self.b_nuevo = Button(caja_2, 
                        text='Nuevo', 
                        font='arial 12', 
                        width=9
                        
                        )
        self.b_nuevo.grid(row=4, column=0, padx=30, pady=3)

        self.b_guardar = Button(caja_2, 
                        text='Guardar', 
                        font='arial 12', 
                        width=9, 
                        
                        )
        self.b_guardar.config(state='disabled')
        self.b_guardar.grid(row=4, column=1, padx=30, pady=3)

        self.b_consulta = Button(caja_2, 
                        text='Consulta', 
                        font='arial 12', 
                        width=9, 
                        
                        )
        self.b_consulta.grid(row=4, column=2, padx=30)

        self.b_modificar = Button(caja_2, 
                        text='Modificar', 
                        font='arial 12', 
                        width=9, 
                        
                        )
        self.b_modificar.grid(row=4, column=3, padx=30, pady=3)

        self.b_borrar = Button(caja_2, 
                        text='Borrar', 
                        font='arial 12', 
                        width=9, 
                        
                        )
        self.b_borrar.grid(row=4, column=4, padx=30)

        #----------------- TreeView ---- Importamos ttk-------------

        caja_3 = Frame(self.root, bg='#c8c6ae', width=900, height=300)
        caja_3.grid(row=5, column=0)

        #----------------- TABLA ---------------------

        self.tabla = ttk.Treeview(caja_3, 
                            columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.tabla.grid(row=5, column=0)
        self.tabla.column('#0', width=50)
        self.tabla.column('col1', width=100)
        self.tabla.column('col2', width=150)
        self.tabla.column('col3', width=150)
        self.tabla.column('col4', width=150)
        self.tabla.column('col5', width=100)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('col1', text='FECHA')
        self.tabla.heading('col2', text='APELLIDO')
        self.tabla.heading('col3', text='NOMBRE')
        self.tabla.heading('col4', text='OBRA SOCIAL')
        self.tabla.heading('col5', text='DNI')

        

        #### BARRA VERTICAL

        self.barra = Scrollbar(caja_3, orient='vertical', 
                                command=self.tabla.yview)
        self.barra.grid(row=5, column=5, sticky=NS)

        self.tabla.config(yscrollcommand=self.barra.set)
        
        ######################## BUSCAR ####################

        caja_4 = Frame(
                        self.root, 
                        bg='#c8c6ae', 
                        width=900, 
                        height=300, 
                        pady=10
                        )
        caja_4.grid(row=6, column=0)

        tit_buscar = Label(caja_4,
                        bg='#c8c6ae',
                        text='Ingrese DNI: ',
                        font='arial 10')
        tit_buscar.grid(row=0, column=0, padx=5)


        self.v_buscar=StringVar()

        self.en_buscar = Entry(caja_4, textvariable=self.v_buscar)
        self.en_buscar.grid(row=0, column=1, padx=10)

        self.b_buscar = Button(caja_4,
                        text='Buscar',
                        font='arial 12', 
                        width=9
                        )
        self.b_buscar.grid(row=0, column=2, padx=10)

        self.b_refresh = Button(caja_4, 
                        text='Refresh',
                        font='arial 12', 
                        width=9
                        )
        self.b_refresh.grid(row=0, column=3, padx=10)

        #Ejecucion de las funciones a través de los botones

        self.funcion.conectar(self.tabla)

        

        self.b_nuevo.config(command=lambda:self.funcion.nuevo
                                    (self.en_apellido.config,                                                             
                                     self.en_nombre.config,
                                     self.en_obra.config,
                                     self.en_dni.config,
                                     self.en_resumen.config,
                                     self.b_guardar.config
                                                            )
                                                            )


        self.b_guardar.config(
            command=lambda:self.funcion.guardar(self.var_ape,
                                                  self.var_nom,
                                                  self.var_obra_s,
                                                  self.var_dni,
                                                  self.en_resumen,
                                                  self.tabla,
                                                  self.en_apellido.config,                                                             
                                                  self.en_nombre.config,
                                                  self.en_obra.config,
                                                  self.en_dni.config,
                                                  self.en_resumen.config,
                                                                  ))

        self.b_consulta.config(
                            command=lambda:
                            self.funcion.consulta(
                                                self.en_apellido.config,                                                             
                                                self.en_nombre.config,
                                                self.en_obra.config,
                                                self.en_dni.config,
                                                self.en_resumen.config,
                                                self.var_ape,
                                                self.var_nom,
                                                self.var_obra_s,
                                                self.var_dni,
                                                self.en_resumen,
                                                self.tabla,                               
                                                                    ))

        self.b_modificar.config(
            command=lambda:self.funcion.modificar(self.var_ape,
                                                      self.var_nom,
                                                      self.var_obra_s,
                                                      self.var_dni,
                                                      self.en_resumen,
                                                      self.tabla,
                                                      self.en_apellido.config,                                                             
                                                      self.en_nombre.config,
                                                      self.en_obra.config,
                                                      self.en_dni.config,
                                                      self.en_resumen.config,
                                                      )
                                                    )

        self.b_borrar.config(
            command=lambda:self.funcion.borrar(self.tabla,
                                                self.var_ape,
                                                self.var_nom,
                                                self.var_obra_s,
                                                self.var_dni,
                                                self.en_resumen,
                                                self.en_apellido.config,                                                             
                                                self.en_nombre.config,
                                                self.en_obra.config,
                                                self.en_dni.config,
                                                self.en_resumen.config,))


        self.b_buscar.config(command=lambda:self.funcion.buscar(
                                                                self.tabla,
                                                                self.v_buscar
                                                                )
                                                            )


        self.b_refresh.config(command=lambda:self.funcion.refrescar(
                                                            self.tabla,
                                                            self.v_buscar
                                                            )
                                                        )
    
    def menu_c(self):
        
        barra_menu = Menu(self.root)
        
        archivo = Menu(barra_menu, tearoff=0)

        temas = Menu(barra_menu, tearoff=0)

        self.apuntes = MenuCascada()
        
        archivo.add_command(label="Exportar a .txt",
                             command=lambda:self.apuntes.print_tabla())
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.root.destroy)
        barra_menu.add_cascade(label='Archivo', menu=archivo)

        barra_menu.add_cascade(label='Ir', menu=temas)

        temas.add_command(label="Versión", 
                            command=lambda:self.apuntes.version())
        temas.add_command(label="Manual", 
                            command=lambda:self.apuntes.manual())
        temas.add_command(label="Obras sociales y prepagas", 
                            command=lambda:self.apuntes.link_obras())
        
        self.root.config(menu=barra_menu)



        


