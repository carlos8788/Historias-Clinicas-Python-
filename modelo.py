import sqlite3
from datetime import datetime
import re
from tkinter import messagebox

class Funcion:

    def __init__(self) -> None:
        
        self.fecha = datetime.now()
        self.fecha_actual = datetime.strftime(self.fecha, '%d - %m - %Y')
    

    def conectar(self, tabla):
        try:
            self.reinicio_tree(tabla)
            
    
            nombre_db = 'hist.db'
            conexion = sqlite3.connect(nombre_db)
            cursor = conexion.cursor()
            sql = """CREATE TABLE historia (id INTEGER,
                                            fecha TEXT, 
                                            apellido TEXT(20),
                                            nombre TEXT(20),
                                            obra_social TEXT(20),
                                            dni INTEGER(10),
                                            resumen TEXT,
                                            PRIMARY KEY(ID AUTOINCREMENT)
                                            )"""
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
            
        except:
            datos = []
            nombre_db = 'hist.db'
            conexion = sqlite3.connect(nombre_db)
            cursor = conexion.cursor()
                    
            most = "SELECT id, fecha, apellido, nombre, obra_social, dni \
                    FROM historia"
            cursor.execute(most)
            datos = cursor.fetchall()
                    
            for p in datos:
                
                tabla.insert('', 'end',
                            text=p[0],
                            values=(p[1], p[2], p[3], p[4], p[5])
                            )
                        

            conexion.commit()
            conexion.close()


    def nuevo(self, c_ape, c_nom, c_ob, c_dni, c_res, activa):
        
        self.habilitar(c_ape, c_nom, c_ob, c_dni, c_res)
        activa(state='normal')
        pass


    def guardar(self, ape, nom, ob, dni, res, tabla,
                c_ape, c_nom, c_ob, c_dni, c_res):
        
        try:
            if re.findall('[0-9]', str(dni.get())) and \
                re.findall('[\D]', nom.get()) and \
                re.findall('[\D]', ape.get()):
                    
            
                self.reinicio_tree(tabla)
                
                nombre_db = 'hist.db'
                conexion = sqlite3.connect(nombre_db)
                cursor = conexion.cursor()
                insertar_datos = f"""INSERT INTO historia ('fecha',
                                                        'apellido',
                                                        'nombre',
                                                        'obra_social',
                                                        'dni',
                                                        'resumen') 
                                    VALUES ('{self.fecha_actual}',
                                            '{ape.get()}',
                                            '{nom.get()}',
                                            '{ob.get()}',
                                            '{dni.get()}',
                                            '{res.get('1.0', 'end')}'
                                            )"""
                cursor.execute(insertar_datos)
                conexion.commit()
                conexion.close()
                
                
                datos = []

                nombre_db = 'hist.db'
                conexion = sqlite3.connect(nombre_db)
                cursor = conexion.cursor()
                    
                most = "SELECT id, fecha, apellido, nombre, obra_social, dni \
                        FROM historia"
                cursor.execute(most)
                datos = cursor.fetchall()
                
                for p in datos:
                    
                    tabla.insert('', 'end', 
                                text=p[0], 
                                values=(p[1], p[2], p[3], p[4], p[5])
                                )
                conexion.commit()
                conexion.close()

                self.borrar_entradas(ape, nom, ob, dni, res)

                messagebox.showinfo("Guardar", "Registro guardado")
            else:
                messagebox.showinfo("Guardar", "Datos no válidos\n\
                                    Revise por favor\n \
                                    DNI: Solo números\n \
                                    Nombre y Apellido: Solo letras")
        except:
            messagebox.showinfo("Guardar", "Datos no válidos\n\
                                    Revise por favor\n \
                                    DNI: Solo números\n \
                                    Nombre y Apellido: Solo letras")
        self.borrar_entradas(ape, nom, ob, dni, res)
        self.deshabilitar(c_ape, c_nom, c_ob, c_dni, c_res)
        
    def consulta(self, c_ape, c_nom, c_ob, c_dni, c_res,
                 var_ape, var_nom, var_dni, var_ob, res_ide, tabla):
        
        
        item = tabla.item(tabla.selection())
        
        lista = list(item['values'])
        print(lista)
        ide = item['text']
        print(ide)
        if ide !='':
            try:
                self.habilitar(c_ape, c_nom, c_ob, c_dni, c_res)
                var_ape.set(lista[1])
                var_nom.set(lista[2])
                var_dni.set(lista[3])
                var_ob.set(lista[4])
            
                ide = item['text']

                def mostrar(ide):
                    nombre_db = 'hist.db'
                    conexion = sqlite3.connect(nombre_db)
                    cursor = conexion.cursor()
                    data = (ide,)
                    most = "SELECT resumen FROM historia WHERE id=?"
                    cursor.execute(most, data)
                    datos = cursor.fetchall()
                    datos = str(datos)
                    
                    resumen = res_ide.insert('1.0', f"{datos[3:-6]}")
                    
                    conexion.commit()
                    conexion.close()

                    
                mostrar(ide)
            
            except:
                pass
            
        else:
            messagebox.showinfo('Consulta', 'Seleccione un registro')


    def modificar(self, ape, nom, ob, dni, res, tabla,
                    c_ape, c_nom, c_ob, c_dni, c_res):
        try:
            if re.findall('[0-9]', str(dni.get())) and \
                re.findall('[\D]', nom.get()) and \
                re.findall('[\D]', ape.get()):

                item = tabla.item(tabla.selection())
                
                lis2 = (item['text'])
                lista = [
                    lis2, ape.get(),
                    nom.get(), 
                    ob.get(), 
                    dni.get(), 
                    res.get('1.0', 'end')
                    ]


                #b_modificar.config(state='disabled')
                
                

                def actualizar(ape, nom, obs, dn, resu, id):

                    borrar = tabla.get_children()
                    for elemento in borrar:
                        tabla.delete(elemento)

                    nombre_db = 'hist.db'
                    conexion = sqlite3.connect(nombre_db)
                    cursor = conexion.cursor()
                    data = (ape, nom, obs, dn, resu, id)
                    modificar_datos = "UPDATE historia \
                                    SET apellido=?, \
                                    nombre=?, obra_social=?, \
                                    dni=?, resumen=? \
                                    WHERE id=?"
                    cursor.execute(modificar_datos,data)
                    conexion.commit()
                    conexion.close()
                actualizar(lista[1], 
                            lista[2],
                            lista[3], 
                            lista[4], 
                            lista[5], 
                            lis2
                            )

                datos = []

                nombre_db = 'hist.db'
                conexion = sqlite3.connect(nombre_db)
                cursor = conexion.cursor()
                    
                most = "SELECT id, fecha, apellido, nombre, obra_social, dni \
                        FROM historia"
                cursor.execute(most)
                datos = cursor.fetchall()
                    
                for p in datos:
                    tabla.insert('', 'end', 
                                text=p[0], 
                                values=(p[1], p[2], p[3], p[4], p[5])
                                )
                        

                conexion.commit()
                conexion.close()
                
                self.borrar_entradas(ape, nom, ob, dni, res)
                self.deshabilitar(c_ape, c_nom, c_ob, c_dni, c_res)
                messagebox.showinfo('Modificar', 'Se modificó un registro')
            else:
                messagebox.showinfo("Modificar", "Datos no válidos\n\
                                    Revise por favor\n \
                                    DNI: Solo números\n \
                                    Nombre y Apellido: Solo letras")
        except:
            messagebox.showerror("Modificar", \
                                 "Primero debe realizar una consulta")


    def borrar(self, tabla,ape, nom, ob, dni, res,
                    c_ape, c_nom, c_ob, c_dni, c_res):

        a_borrar = tabla.selection()
        item = tabla.item(tabla.selection())
        ide = item['text']
        if ide !='':
            preg_borrar = messagebox.askquestion(
                                                "Borrar",
                                                "Desea borrar este registro?"
                                                )
            if preg_borrar == "yes":
                try:
                    
                    nombre_db = 'hist.db'
                    conexion = sqlite3.connect(nombre_db)
                    cursor = conexion.cursor()
                    data = (ide,)
                    most = "DELETE FROM historia WHERE id=?;"
                    cursor.execute(most, data)
                    conexion.commit()
                    conexion.close()
                    tabla.delete(a_borrar)
                    
                    self.borrar_entradas(ape, nom, ob, dni, res)
                    self.deshabilitar(c_ape, c_nom, c_ob, c_dni, c_res)

                    messagebox.showinfo("Borrar", "Registro borrado")
                except:
                    pass

            else:
                messagebox.showinfo("Borrar", "No se borró el registro")
        else:
            messagebox.showinfo('Borrar', 'Seleccione un registro')


    def buscar(self, tabla, v_buscar):
        borrar = tabla.get_children()
        for elemento in borrar:
            tabla.delete(elemento)

        datos = []

        nombre_db = 'hist.db'
        conexion = sqlite3.connect(nombre_db)
        cursor = conexion.cursor()
                    
        most = "SELECT * FROM historia"
        cursor.execute(most)
        datos = cursor.fetchall()

        busca = v_buscar.get()
        print(v_buscar.get())
        
        if re.findall('[0-9]', v_buscar.get()):
            contador = 0
            for p in datos:
                
                if p[5] == int(v_buscar.get()):
                    
                    contador += 1
                    tabla.insert('', 'end', 
                                text=p[0], 
                                values=(p[1], p[2], p[3], p[4], p[5])
                                )
                
                
            v_buscar.set("")
            
            if contador == 0:
                v_buscar.set("")
                self.conectar(tabla)
                messagebox.showinfo("Buscar","DNI no encontrado")    
        else:
            self.conectar(tabla)
            messagebox.showinfo("Buscar","Datos invalidos")
     
        conexion.commit()
        conexion.close()


    def refrescar(self, tabla, v_buscar):
        v_buscar.set("")
        self.reinicio_tree(tabla)
        self.conectar(tabla)
        

    def habilitar(self, c_ape, c_nom, c_ob, c_dni, c_res):
        c_ape(state='normal')
        c_nom(state='normal')
        c_ob(state='normal')
        c_dni(state='normal')
        c_res(state='normal')


    def deshabilitar(self, c_ape, c_nom, c_ob, c_dni, c_res):
        c_ape(state='disabled')
        c_nom(state='disabled')
        c_ob(state='disabled')
        c_dni(state='disabled')
        c_res(state='disabled')


    def reinicio_tree(self, tabla):
        borrar = tabla.get_children()
        
        for elemento in borrar:
            tabla.delete(elemento)
    

    def borrar_entradas(self, c_ape, c_nom, c_ob, c_dni, c_res):
        c_ape.set('')
        c_nom.set('')
        c_ob.set('')
        c_dni.set('')
        c_res.delete("1.0", 'end')
