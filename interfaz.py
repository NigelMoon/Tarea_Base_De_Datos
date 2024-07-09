import tkinter as tk
from tkinter import ttk
from datetime import date
import psycopg2 as network

PASSWORD = 'Contraseña'
DATABASE = 'Database'

CONFIG = {
            'user':'postgres',
            'password':PASSWORD, #Hay que cambiar en caso de ser otro el que ingresa
            'host':'localhost',
            'port':'5432',
            'database':DATABASE #Colocar el nombre de la base de datos original
    }
    
conexion = network.connect(**CONFIG)
cursor = conexion.cursor()

cursor.execute("select nombre from comuna;")
comunas = cursor.fetchall()

cursor.execute("select nombre_producto from producto;")
productos = cursor.fetchall()

#aqui ta raro el ingreso, ta medio huh? huh? huh?

def ingresa_venta(): #Funcion que maneja la venta de un producto
    def ingresa_detalle_venta(): #Funcion que maneja el detalle de venta de un producto
        
        def ingreso_datos():
            global texto_detalle
            texto_detalle = ''
            total = 0
            producto = combo_producto_detalle.get()
            cantidad = int(caja_cantidad.get())
            if productos_venta:
                existe = False
                for tupla in productos_venta:
                    if tupla[0] == producto:
                        tupla[1] += cantidad
                        existe = True
                if not existe:
                    productos_venta.append([producto, cantidad])
            else:
                productos_venta.append([producto, cantidad])

            for tupla in productos_venta:
                texto_detalle += str(tupla[1]) + 'x ' + str(tupla[0]) + '\n'
                total += tupla[1]*1000

            etiqueta_total.config(text=str(total))
            etiqueta_detalle_locura.config(text=texto_detalle)

            cierra_ventana_detalle_venta()


        def cierra_ventana_detalle_venta():
            ventana_detalle.destroy()
            ventana_venta.deiconify()

        ventana_venta.withdraw()
        ventana_detalle = tk.Tk()
        ventana_detalle.focus_force()
        ventana_detalle.title("Ingresar detalle de venta")

        wtotal = ventana.winfo_screenwidth()
        htotal = ventana.winfo_screenheight()

        ventana_detalle.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

        """TITULO"""
        etiqueta_titulo_detalle = ttk.Label(ventana_detalle, text="Ingresar datos del detalle de venta de un producto", font=("Arial", 15))
        etiqueta_titulo_detalle.place(x = 260, y = 20)

        """INGRESAR PRODUCTO"""
        etiqueta_producto_detalle = ttk.Label(ventana_detalle, text="Ingresar producto: ", font=("Arial", 15))
        etiqueta_producto_detalle.place(x = 20, y = 80)
        
        combo_producto_detalle = ttk.Combobox(ventana_detalle, values=productos, font=("Arial", 15), state='readonly')
        combo_producto_detalle.place(x = 320, y = 80, width= 350, height=30)

        """INGRESAR CANTIDAD"""
        etiqueta_cantidad = ttk.Label(ventana_detalle, text="Ingresar cantidad:", font=("Arial", 15))
        etiqueta_cantidad.place(x = 20, y = 160)
        
        caja_cantidad = ttk.Entry(ventana_detalle, font=("Arial", 15))
        caja_cantidad.place(x = 320, y = 160, width= 350, height=30)

        """INGRESAR VENTA"""
        boton_ingresar = tk.Button(ventana_detalle, text="Ingresar", font=("Arial", 15), command=ingreso_datos)
        boton_ingresar.place(x=350, y=240)


        """VOLVER"""
        boton_volver = tk.Button(ventana_detalle, text="Volver", font=("Arial", 15), command=cierra_ventana_detalle_venta)
        boton_volver.place(x=550, y=240)

        ventana_detalle.protocol("WM_DELETE_WINDOW", cierra_ventana_detalle_venta)
            

    def cierra_ventana_venta():
        ventana_venta.destroy()
        ventana.deiconify()


    ventana.withdraw()
    ventana_venta = tk.Tk()
    ventana_venta.focus_force()
    ventana_venta.title("Ingresar venta")

    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    ventana_venta.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

    """TITULO"""
    etiqueta_titulo = ttk.Label(ventana_venta, text="Ingresar datos de la venta de producto", font=("Arial", 15))
    etiqueta_titulo.place(x = 260, y = 20)

    """INGRESAR RUT CLIENTE"""
    etiqueta_rut_cl = ttk.Label(ventana_venta, text="Ingresar RUT comprador sin DV:", font=("Arial", 15))
    etiqueta_rut_cl.place(x = 20, y = 80)
    
    caja_rut_cl = ttk.Entry(ventana_venta, font=("Arial", 15))
    caja_rut_cl.place(x = 320, y = 80, width= 350, height=30)

    """DETALLE VENTA"""
    global etiqueta_detalle_locura
    etiqueta_detalle_locura = ttk.Label(ventana_venta, font=("Arial", 12))
    etiqueta_detalle_locura.place(x=320, y= 160)

    """TOTAL VENTA"""
    global etiqueta_total
    etiqueta_total_venta = ttk.Label(ventana_venta, text="Total:", font=("Arial", 12))
    etiqueta_total_venta.place(x=320, y= 280)

    etiqueta_total = ttk.Label(ventana_venta, text="0", font=("Arial", 12))
    etiqueta_total.place(x=600, y=280)

    """INGRESAR PRODUCTO"""
    etiqueta_detalle = ttk.Label(ventana_venta, text="Detalle:", font=("Arial", 15))
    etiqueta_detalle.place(x = 20, y = 160)
    
    boton_detalle = tk.Button(ventana_venta, text="Ingresar venta", font=("Arial", 15), command=ingresa_detalle_venta)
    boton_detalle.place(x = 320, y = 320, width= 350, height=30)

    """INGRESAR VENTA"""
    boton_ingresar = tk.Button(ventana_venta, text="Ingresar", font=("Arial", 15))
    boton_ingresar.place(x=350, y=370)

    """VOLVER"""
    boton_volver = tk.Button(ventana_venta, text="Volver", font=("Arial", 15), command=cierra_ventana_venta)
    boton_volver.place(x=550, y=370)

    ventana_venta.protocol("WM_DELETE_WINDOW", cierra_ventana_venta)

def ingresa_compra(): #Funcion que maneja las compras de un producto
    def ingresa_detalle_compra(): #Funcion que maneja el detalle de venta de un producto
        def cierra_ventana_detalle_compra():
            ventana_detalle.destroy()
            ventana_compra.deiconify()


        def ingreso_datos():
            global texto_detalle
            texto_detalle = ''
            total = 0
            #cursor.execute("Select id_venta")
            producto = combo_producto_detalle.get()
            cantidad = int(caja_cantidad.get())
            if productos_venta:
                existe = False
                for tupla in productos_venta:
                    if tupla[0] == producto:
                        tupla[1] += cantidad
                        existe = True
                if not existe:
                    productos_venta.append([producto, cantidad])
            else:
                productos_venta.append([producto, cantidad])

            for tupla in productos_venta:
                texto_detalle += str(tupla[1]) + 'x ' + str(tupla[0]) + '\n'
                total += tupla[1]*1000

            etiqueta_total.config(text=str(total))
            etiqueta_detalle_locura.config(text=texto_detalle)

            cierra_ventana_detalle_compra()


        ventana_compra.withdraw()
        ventana_detalle = tk.Tk()
        ventana_detalle.focus_force()
        ventana_detalle.title("Ingresar detalle de venta")

        peluqueria = combo_peluqueria.get()

        wtotal = ventana.winfo_screenwidth()
        htotal = ventana.winfo_screenheight()

        ventana_detalle.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

        """TITULO"""
        etiqueta_titulo_detalle = ttk.Label(ventana_detalle, text="Ingresar datos del detalle de compra de un producto", font=("Arial", 15))
        etiqueta_titulo_detalle.place(x = 260, y = 20)

        """INGRESAR PRODUCTO"""
        etiqueta_producto_detalle = ttk.Label(ventana_detalle, text="Ingresar producto: ", font=("Arial", 15))
        etiqueta_producto_detalle.place(x = 20, y = 80)
        
        
        combo_producto_detalle = ttk.Combobox(ventana_detalle, values=productos, font=("Arial", 15), state='readonly')
        combo_producto_detalle.place(x = 320, y = 80, width= 350, height=30)

        """INGRESAR CANTIDAD"""
        etiqueta_cantidad = ttk.Label(ventana_detalle, text="Ingresar cantidad:", font=("Arial", 15))
        etiqueta_cantidad.place(x = 20, y = 160)
        
        caja_cantidad = ttk.Entry(ventana_detalle, font=("Arial", 15))
        caja_cantidad.place(x = 320, y = 160, width= 350, height=30)

        """INGRESAR VENTA"""
        boton_ingresar = tk.Button(ventana_detalle, text="Ingresar", font=("Arial", 15), command=ingreso_datos)
        boton_ingresar.place(x=350, y=240)


        """VOLVER"""
        boton_volver = tk.Button(ventana_detalle, text="Volver", font=("Arial", 15), command=cierra_ventana_detalle_compra)
        boton_volver.place(x=550, y=240)

        ventana_detalle.protocol("WM_DELETE_WINDOW", cierra_ventana_detalle_compra)
            

    def cierra_ventana_compra():
        ventana_compra.destroy()
        ventana.deiconify()


    ventana.withdraw()
    ventana_compra = tk.Tk()
    ventana_compra.focus_force()
    ventana_compra.title("Ingresar compra")

    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    ventana_compra.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

    """TITULO"""
    etiqueta_titulo = ttk.Label(ventana_compra, text="Ingresar datos de la compra de stock", font=("Arial", 15))
    etiqueta_titulo.place(x = 260, y = 20)

    """DETALLE VENTA"""
    global etiqueta_detalle_locura
    etiqueta_detalle_locura = ttk.Label(ventana_compra, font=("Arial", 12))
    etiqueta_detalle_locura.place(x=320, y= 80)

    """INGRESAR PRODUCTO"""
    etiqueta_detalle = ttk.Label(ventana_compra, text="Detalle:", font=("Arial", 15))
    etiqueta_detalle.place(x = 20, y = 80)

    """TOTAL VENTA"""
    global etiqueta_total
    etiqueta_total_venta = ttk.Label(ventana_compra, text="Total:", font=("Arial", 12))
    etiqueta_total_venta.place(x=320, y= 280)

    etiqueta_total = ttk.Label(ventana_compra, text="0", font=("Arial", 12))
    etiqueta_total.place(x=600, y=280)

    boton_detalle = tk.Button(ventana_compra, text="Ingresar venta", font=("Arial", 15), command=ingresa_detalle_compra)
    boton_detalle.place(x = 320, y = 320, width= 350, height=30)

    """INGRESAR VENTA"""
    boton_ingresar = tk.Button(ventana_compra, text="Ingresar", font=("Arial", 15))
    boton_ingresar.place(x=350, y=370)

    """VOLVER"""
    boton_volver = tk.Button(ventana_compra, text="Volver", font=("Arial", 15), command=cierra_ventana_compra)
    boton_volver.place(x=550, y=370)

    ventana_compra.protocol("WM_DELETE_WINDOW", cierra_ventana_compra)

#de aqui pa abajo ya tan listos los insert, capaz algo que diga error al igreso, ahi no c tu

def ingresa_empleado(): #Funcion que maneja el ingreso de un cliente
    def cierra_ventana_empleado():
        ventana_empleado.destroy()
        ventana.deiconify()


    def ingreso_datos():
        rut = caja_rut.get() #Creo que falta un casteo a int
        nombre = caja_nombre.get()
        apellido = caja_apellido.get()
        sexo = caja_sexo.get() #no hace falta
        comuna = "pico"
        cursor.execute(f"select id_comuna from comuna where nombre={comuna};")
        id_comuna = cursor.fetchone()
        peluqueria = int(combo_peluqueria.get())
        
        try:
            cursor.execute("insert into empleado (rut_empleado,nombre_empleado,apellido_empleado,id_peluqueria,id_comuna) values (%s,%s,%s,%s,%s)",(rut,nombre,apellido,peluqueria,id_comuna))
            conexion.commit()
        except network.IntegrityError:
            conexion.rollback()


    ventana.withdraw()
    ventana_empleado = tk.Tk()
    ventana_empleado.focus_force()
    ventana_empleado.title("Ingresar empleado")

    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    ventana_empleado.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

    """TITULO"""
    etiqueta_titulo = ttk.Label(ventana_empleado, text="Ingresar datos del empleado", font=("Arial", 15))
    etiqueta_titulo.place(x = 260, y = 20)

    """INGRESAR RUT"""
    etiqueta_rut = ttk.Label(ventana_empleado, text="Ingresar RUT: ", font=("Arial", 15))
    etiqueta_rut.place(x = 20, y = 80)
    
    caja_rut = ttk.Entry(ventana_empleado, font=("Arial", 15))
    caja_rut.place(x = 320, y = 80, width= 350, height=30)

    """INGRESAR NOMBRE"""
    etiqueta_nombre = ttk.Label(ventana_empleado, text="Ingresar nombre: ", font=("Arial", 15))
    etiqueta_nombre.place(x = 20, y = 160)
    
    caja_nombre = ttk.Entry(ventana_empleado, font=("Arial", 15))
    caja_nombre.place(x = 320, y = 160, width= 350, height=30)

    """INGRESAR APELLIDO"""
    etiqueta_apellido = ttk.Label(ventana_empleado, text="Ingresar apellido: ", font=("Arial", 15))
    etiqueta_apellido.place(x = 20, y = 240)
    
    caja_apellido = ttk.Entry(ventana_empleado, font=("Arial", 15))
    caja_apellido.place(x = 320, y = 240, width= 350, height=30)


    """INGRESAR EMPLEADO"""
    boton_ingresar = tk.Button(ventana_empleado, text="Ingresar", font=("Arial", 15), command=ingreso_datos)
    boton_ingresar.place(x=350, y=370)

    """VOLVER"""
    boton_volver = tk.Button(ventana_empleado, text="Volver", font=("Arial", 15), command=cierra_ventana_empleado)
    boton_volver.place(x=550, y=370)

    ventana_empleado.protocol("WM_DELETE_WINDOW", cierra_ventana_empleado)

def ingresa_cita(): #Funcion que maneja el ingreso de citas
    def cierra_ventana_cita():
        ventana_cita.destroy()
        ventana.deiconify()
        ...
    
    def ingreso_datos():
        rut_cl = caja_rut_cl.get()
        rut_pel = caja_rut_pel.get()
        fecha = caja_fecha.get() 
        bloque = caja_bloque.get() #Son varios bloques :p
        peluqueria = int(combo_peluqueria.get())
        servicio = "Aqui iria lo que alvaro coloco de nuevo uwu"
        
        cursor.execute("select max(id_cita) from cita limit 1;")
        id_cita = cursor.fetchone()[0]+1
        try:
            cursor.execute("insert into cita (id_cita,fecha,rut_empleado,id_servicio,id_peluqueria,rut_cliente) values (%s,%s,%s,%s,%s,%s)",(id_cita,fecha,rut_pel,servicio,id_peluqueria,rut_cl))
            conexion.commit()
        except network.IntegrityError:
            conexion.rollback()
        finally:
            cursor.execute("select max(id_ocurre) from ocurre limit 1;")
            id_ocurre = cursor.fetchone()[0]+1
            for i in bloque:
                cursor.execute("insert into ocurre (id_ocurre, id_cita, id_bloque) values (%s,%s,%s)",(id_ocurre,id_cita,i))
                conexion.commit()
                id_ocurre+=1
        ...

    
    ventana.withdraw()
    ventana_cita = tk.Tk()
    ventana_cita.focus_force()
    ventana_cita.title("Ingresar cita")

    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    ventana_cita.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

    """TITULO"""
    etiqueta_titulo = ttk.Label(ventana_cita, text="Ingresar datos de la cita", font=("Arial", 15))
    etiqueta_titulo.place(x = 260, y = 20)

    """INGRESAR RUT"""
    etiqueta_rut_cl = ttk.Label(ventana_cita, text="Ingresar RUT del cliente: ", font=("Arial", 15))
    etiqueta_rut_cl.place(x = 20, y = 80)
    
    caja_rut_cl = ttk.Entry(ventana_cita, font=("Arial", 15))
    caja_rut_cl.place(x = 320, y = 80, width= 350, height=30)

    """INGRESAR RUT PELUQUERO"""
    etiqueta_rut_pel = ttk.Label(ventana_cita, text="Ingresar RUT del peluquero/a: ", font=("Arial", 15))
    etiqueta_rut_pel.place(x = 20, y = 128)
    
    caja_rut_pel = ttk.Entry(ventana_cita, font=("Arial", 15))
    caja_rut_pel.place(x = 320, y = 128, width= 350, height=30)

    """INGRESAR FECHA"""
    etiqueta_fecha = ttk.Label(ventana_cita, text="Ingresar fecha (yyyy-mm-dd): ", font=("Arial", 15))
    etiqueta_fecha.place(x = 20, y = 176)
    
    caja_fecha = ttk.Entry(ventana_cita, font=("Arial", 15))
    caja_fecha.place(x = 320, y = 176, width= 350, height=30)

    """INGRESAR BLOQUE"""
    etiqueta_bloque = tk.Label(ventana_cita, text="Ingresar bloque/hora: ", font=("Arial", 15))
    etiqueta_bloque.place(x = 20, y = 224)
    
    caja_bloque = tk.Entry(ventana_cita, font=("Arial", 15))
    caja_bloque.place(x = 320, y = 224, width= 350, height=30)


    """INGRESAR CITA"""
    boton_ingresar = tk.Button(ventana_cita, text="Ingresar", font=("Arial", 15), command=ingreso_datos)
    boton_ingresar.place(x=350, y=370)

    """VOLVER"""
    boton_volver = tk.Button(ventana_cita, text="Volver", font=("Arial", 15), command=cierra_ventana_cita)
    boton_volver.place(x=550, y=370)

    ventana_cita.protocol("WM_DELETE_WINDOW", cierra_ventana_cita)

def ingresa_cliente(): #Funcion que maneja el ingreso de un cliente
    def cierra_ventana_cliente():
        ventana_cliente.destroy()
        ventana.deiconify()
    

    def ingreso_datos():
        rut = caja_rut.get() #esto deberia ser entero
        nombre = caja_nombre.get()
        apellido = caja_apellido.get() #no es taaan necesario btw
        sexo = combo_sexo.get()
        comuna = combo_comuna_cl.get()
        cursor.execute(f"select id_comuna from comuna where nombre={comuna};")
        id_comuna = cursor.fetchone()[0]
        
        try:
            cursor.execute("insert into cliente (rut_cliente,sexo,nombre,id_comuna) values (%s,%s,%s,%s)",(rut,sexo,nombre,id_comuna))
            conexion.commit()
        except network.IntegrityError:
            conexion.rollback()
        ...


    ventana.withdraw()
    ventana_cliente = tk.Tk()
    ventana_cliente.focus_force()
    ventana_cliente.title("Ingresar cliente")

    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    ventana_cliente.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")

    """TITULO"""
    etiqueta_titulo = ttk.Label(ventana_cliente, text="Ingresar datos del cliente", font=("Arial", 15))
    etiqueta_titulo.place(x = 260, y = 20)

    """INGRESAR RUT"""
    etiqueta_rut = ttk.Label(ventana_cliente, text="Ingresar RUT sin DV: ", font=("Arial", 15))
    etiqueta_rut.place(x = 20, y = 80)
    
    caja_rut = ttk.Entry(ventana_cliente, font=("Arial", 15))
    caja_rut.place(x = 320, y = 80, width= 350, height=30)

    """INGRESAR NOMBRE"""
    etiqueta_nombre = ttk.Label(ventana_cliente, text="Ingresar nombre: ", font=("Arial", 15))
    etiqueta_nombre.place(x = 20, y = 128)
    
    caja_nombre = ttk.Entry(ventana_cliente, font=("Arial", 15))
    caja_nombre.place(x = 320, y = 128, width= 350, height=30)

    """INGRESAR APELLIDO"""
    etiqueta_apellido = ttk.Label(ventana_cliente, text="Ingresar apellido: ", font=("Arial", 15))
    etiqueta_apellido.place(x = 20, y = 176)
    
    caja_apellido = ttk.Entry(ventana_cliente, font=("Arial", 15))
    caja_apellido.place(x = 320, y = 176, width= 350, height=30)


    """INGRESAR SEXO"""
    etiqueta_sexo = tk.Label(ventana_cliente, text="Ingresar sexo: ", font=("Arial", 15))
    etiqueta_sexo.place(x = 20, y = 224)

    combo_sexo = ttk.Combobox(ventana_cliente, values=["M", "F"], state='readonly', font=("Arial", 15))
    combo_sexo.place(x = 320, y = 224, width= 350, height=30)

    """INGRESAR COMUNA"""
    etiqueta_comuna_cl = tk.Label(ventana_cliente, text="Ingresar comuna: ", font=("Arial", 15))
    etiqueta_comuna_cl.place(x = 20, y = 272)

    
    combo_comuna_cl = ttk.Combobox(ventana_cliente, values=comunas, state='readonly', font=("Arial", 15))
    combo_comuna_cl.place(x = 320, y = 272, width= 350, height=30)

    """INGRESAR CLIENTE"""
    boton_ingresar = tk.Button(ventana_cliente, text="Ingresar", font=("Arial", 15), command=ingreso_datos)
    boton_ingresar.place(x=350, y=370)

    """VOLVER"""
    boton_volver = tk.Button(ventana_cliente, text="Volver", font=("Arial", 15), command=cierra_ventana_cliente)
    boton_volver.place(x= 550, y=370)

    ventana_cliente.protocol("WM_DELETE_WINDOW", cierra_ventana_cliente)

def inicializa_ventana(): #Funcion que inicializa la ventana principal
    global ventana, productos_venta, productos_compra

    productos_venta = []
    productos_compra = []

    ventana = tk.Tk()
    ventana.title("Interfaz peluqueria")

    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    ventana.geometry(f"750x450+{int(wtotal/4)}+{int(htotal/5)}")


def main():
    global combo_peluqueria
    inicializa_ventana()

    etiqueta_ingresar = tk.Label(text="Bienvenido! ¿Qué deseas hacer?", font=("Arial", 19))
    etiqueta_ingresar.place(x=ventana.winfo_screenheight()/5 + 20, y= 20)

    """INGRESAR CITA"""
    boton_cita = tk.Button(text= "Ingresar cita", font=("Arial", 19), command=ingresa_cita)
    boton_cita.place(x=60, y=180)

    """INGRESAR CLIENTE"""
    boton_cliente = tk.Button(text= "Ingresar cliente", font=("Arial", 19), command=ingresa_cliente)
    boton_cliente.place(x=250, y=180)

    """INGRESAR EMPLEADO"""
    boton_empleado = tk.Button(text= "Ingresar empleado", font=("Arial", 19), command=ingresa_empleado)
    boton_empleado.place(x=480, y=180)

    """INGRESAR COMPRA"""
    boton_compra = tk.Button(text= "Ingresar compra", font=("Arial", 19), command=ingresa_compra)
    boton_compra.place(x=60, y=270)

    """INGRESAR VENTA"""
    boton_venta = tk.Button(text= "Ingresar venta", font=("Arial", 19), command=ingresa_venta)
    boton_venta.place(x=300, y=270)

    """INGRESAR PELUQUERIA"""
    etiqueta_peluqueria = ttk.Label(text="Ingresa sede: ", font=("Arial", 19))
    etiqueta_peluqueria.place(x=80, y=90)

    cursor.execute("select id_peluqueria from peluqueria;")
    peluquerias = cursor.fetchall()

    combo_peluqueria = ttk.Combobox(values=peluquerias, width=30, font=("Arial", 19), state='readonly')
    combo_peluqueria.place(x=250, y=90)

    ventana.mainloop()


if __name__ == "__main__":
    main()