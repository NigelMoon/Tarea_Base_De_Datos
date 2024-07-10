import schedule
import time
import psycopg2 as network

"""
comuna y peluqueria primero

"""
TABLA_HECHOS_1={
    'cita':'id_cita, fecha, rut_empleado, id_peluqueria, id_servicio, rut_cliente, id_comuna_cliente, id_comuna_empleado, id_bloque_inicio, costo_servicio, id_comuna_peluqueria, sexo, id_bloque_fin'
    ,'peluqueria':'id_peluqueria'
    ,'bloque':'id_bloque'
    ,'comuna':'id_comuna, nombre'
    ,'cliente':'rut_cliente, nombre'
    ,'empleado':'rut_empleado,nombre_empleado,apellido_empleado'
    ,'servicios':'id_servicio, nombre_servicio'
}

TABLA_HECHOS_2 ={
    'detalle_venta':'id_detalle_venta, id_venta, id_producto, precio_venta, total, fecha, sexo, id_comuna, rut_cliente, id_peluqueria, id_comuna_peluqueria, subtotal, cantidad'
    ,'peluqueria_v':'id_peluqueria'
    ,'clienteventa':'rut_cliente, nombre'
    ,'venta':'id_venta'
    ,'producto':'id_producto'
    ,'comuna_c':'id_comuna,nombre'
}

TABLA_HECHOS_3 = {
    'empleado_h':'rut_empleado,id_peluqueria ,nombre_empleado,apellido_empleado,id_comuna,fecha,monto,id_sueldo,id_comuna_peluqueria'
    ,'comuna_h':'id_comuna,nombre'
    ,'peluqueria_h':'id_peluqueria'
    ,'sueldo':'id_sueldo'
}

TABLA_HECHOS_4 = {
    'ofrece':'id_ofrece, id_peluqueria, id_comuna, costo_servicio, id_servicio'
    ,'servicios_o':'id_servicio, nombre_servicio'
    ,'comuna_p':'id_comuna,nombre'
    ,'peluqueria_s':'id_peluqueria'
}


TABLA = {
    'bloque': 'id_bloque',
    'comuna': 'id_comuna, nombre',
    'producto': 'id_producto, precio_compra, nombre_producto, precio_venta, stock_actual',
    'servicios': 'id_servicio, nombre_servicio',
    'transaccion_stock': 'id_transaccion_stock, cant_transaccion, fecha, tipo_transaccion',
    'cliente': 'rut_cliente, sexo, nombre, id_comuna',
    'peluqueria': 'id_peluqueria, id_comuna, direccion',
    'compra': 'id_compra, fecha, total, id_peluqueria',
    'detalle_compra': 'id_detalle_compra, cantidad, subtotal, id_compra, id_producto',
    'venta': 'id_venta, fecha, total, rut_cliente',
    'detalle_venta': 'id_detalle_venta, subtotal, cantidad, id_venta, id_producto',
    'usa_producto': 'id_usa_producto, id_producto, id_servicio, fecha',
    'empleado': 'rut_empleado, sueldo, nombre_empleado, apellido_empleado, id_peluqueria, id_comuna',
    'ofrece': 'id_ofrece, id_peluqueria, id_servicio, costo_servicio',
    'cita': 'id_cita, fecha, rut_empleado, id_servicio, id_peluqueria, rut_cliente',
    'ocurre': 'id_ocurre, id_cita, id_bloque',
    'sueldo': 'id_sueldo, fecha, monto, rut_empleado'
}

def main():
    Bruno = True
    while Bruno:
        try:
            Contraseña = input("Contraseña de postgress: ")
            BaseTrans = input("Nombre de la base de datos Transaccional: ")
            BaseAnalisis = input("Nombre de la base de datos para Analisis: ")
            Config1 = {
                'user':'postgres',
                'password':Contraseña, #Hay que cambiar en caso de ser otro el que ingresa
                'host':'localhost',
                'port':'5432',
                'database':BaseTrans #Colocar el nombre de la base de datos original
            }
            Config2 = {
                'user':'postgres',
                'password':Contraseña, #Hay que cambiar en caso de ser otro el que ingresa
                'host':'localhost',
                'port':'5432',
                'database':BaseAnalisis #Colocar el nombre de la base de datos para el analisis
            }
            conexion = network.connect(**Config1)
            conexion.close()
            conexion = network.connect(**Config2)
            conexion.close()
        except network.OperationalError:
            print("Error al conectar!!!")
        finally:
            Bruno = False

    print("inicializando schedule")
    tarea(Config1,Config2)
    schedule.every(1).week.do(tarea,Config1,Config2)
    while True:
        schedule.run_pending()
        time.sleep(1)

def tarea(Config1,Config2):
    print("Ejecutando tarea....")
    
    sentencia = """
    select t.id_cita, t.fecha, o.rut_empleado, p.id_peluqueria, s.id_servicio, e.rut_cliente, 
    e.id_comuna, o.id_comuna, ofertas.id_bloque_inicio, s.costo_servicio, 
    p.id_comuna, e.sexo, ofertas.id_bloque_fin 
    from cita t 
    inner join peluqueria p on p.id_peluqueria = t.id_peluqueria
    inner join cliente e on e.rut_cliente = t.rut_cliente
    inner join empleado o on o.rut_empleado = t.rut_empleado
    inner join servicios s on s.id_servicio = t.id_servicio
    inner join
    (select o.id_cita,min(o.id_bloque) as id_bloque_inicio, max(o.id_bloque) as id_bloque_fin
    from ocurre o
    group by o.id_cita
    ) as ofertas on ofertas.id_cita = t.id_cita;
    """
    
    conexion1 = network.connect(**Config1)
    cursor1 = conexion1.cursor()
    
    conexion2 = network.connect(**Config2)
    cursor2 = conexion2.cursor()


    cursor1.execute("select * from comuna;")
    comunas = cursor1.fetchall()
    
    cursor1.execute("select id_peluqueria from peluqueria;")
    peluquerias = cursor1.fetchall()
    
    #Tabla 1 cita
    
    cursor1.execute("select * from bloque;")
    bloques = cursor1.fetchall()
    
    cursor1.execute("select rut_cliente, nombre from cliente;")
    clientes = cursor1.fetchall()
    
    cursor1.execute("select id_servicio,nombre_servicio from servicios;")
    servicios = cursor1.fetchall()

    cursor1.execute("select rut_empleado,nombre_empleado,apellido_empleado from empleado;")
    empleados = cursor1.fetchall()

    
    cursor1.execute(sentencia)
    citas = cursor1.fetchall()
    
    
    bloque = verificar_dato(bloques,"bloque",cursor2)
    if len(bloque) != 0:
        cursor2.executemany("insert into bloque (id_bloque) VALUES (%s)",bloque)
        conexion2.commit()

    peluqueria = verificar_dato(peluquerias,"peluqueria",cursor2)
    if len(peluqueria) != 0:
        cursor2.executemany("insert into peluqueria (id_peluqueria) values (%s)",peluqueria)
        conexion2.commit()
    
    comuna = verificar_dato(comunas,"comuna",cursor2)
    if len(comuna)!=0:
        cursor2.executemany("insert into comuna (id_comuna,nombre) values (%s,%s)",comuna)
        conexion2.commit()
    
    cliente = verificar_dato(clientes,"cliente",cursor2)
    if len(cliente)!=0:
        cursor2.executemany("insert into cliente (rut_cliente,nombre) values (%s,%s)",cliente)
        conexion2.commit()
    
    empleado = verificar_dato(empleados,"empleado",cursor2)
    if len(empleado) !=0:
        cursor2.execute("insert into empleado (rut_empleado,nombre_empleado,apellido_empleado) values (%s,%s,%s)",empleado)
        conexion2.commit()

    servicio = verificar_dato(servicios,"servicios",cursor2)
    if(len(servicio) != 0):
        cursor2.execute("insert into servicios (id_servicio, nombre_servicio) values (%s,%s)",servicio)
        conexion2.commit()
    
    cita = verificar_dato(citas,"cita",cursor2)
    if len(cita)!=0:
        cursor2.execute("insert into cita (id_cita, fecha, rut_empleado, id_peluqueria, id_servicio, rut_cliente, id_comuna_cliente, id_comuna_empleado, id_bloque_inicio, costo_servicio, id_comuna_peluqueria, sexo, id_bloque_fin) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",cita)
        conexion2.commit()

    print("Elementos de la tabla 1 ingresados con exito!!")
    
    #Tabla 2 detalle_venta
    
    sentencia2 = """
    select d.id_detalle_venta, d.id_venta, d.id_producto, p.precio_venta, v.total, v.fecha, c.sexo, c.id_comuna, v.rut_cliente, v.id_peluqueria, pe.id_comuna, d.subtotal, d.cantidad
    from detalle_venta d
    inner join venta v on v.id_venta = d.id_venta
    inner join producto p on p.id_producto = d.id_producto
    inner join cliente c on c.rut_cliente = v.rut_cliente
    inner join peluqueria pe on pe.id_peluqueria = v.id_peluqueria;
    """
    
    cursor1.execute("select id_venta from venta;")
    ventas = cursor1.fetchall()
    
    cursor1.execute("select id_producto from producto;")
    productos = cursor1.fetchall()
    
    cursor1.execute(sentencia2)
    detalles = cursor1.fetchall()
    
    peluqueria = verificar_dato(peluquerias,"peluqueria_v",cursor2)
    if len(peluqueria) != 0:
        cursor2.execute("insert into peluqueria_v (id_peluqueria) values (%s)",peluqueria)
        conexion2.commit()
    
    comuna = verificar_dato(comunas,"comuna_c",cursor2)
    if len(comuna)!=0:
        cursor2.execute("insert into comuna_c (id_comuna,nombre) values (%s,%s)",comuna)
        conexion2.commit()
    
    cliente = verificar_dato(clientes,"clienteventa",cursor2)
    if len(cliente) != 0:
        cursor2.execute("insert into clienteventa (rut_cliente,nombre) values (%s,%s)",cliente)
        conexion2.commit()
        
    venta = verificar_dato(ventas,"venta",cursor2)
    if len(venta) != 0:
        cursor2.execute("insert into venta (id_venta) values (%s)",venta)
        conexion2.commit()
    
    producto = verificar_dato(productos,"producto",cursor2)
    if len(producto)!=0:
        cursor2.execute("insert into producto (id_producto) values (%s)",producto)
        conexion2.commit()
            
    detalle_venta = verificar_dato(detalles,"detalle_venta",cursor2)
    if len(detalle_venta)!=0:
        cursor2.execute("insert into detalle_venta (id_detalle_venta, id_venta, id_producto, precio_venta, total, fecha, sexo, id_comuna, rut_cliente, id_peluqueria, id_comuna_peluqueria, subtotal, cantidad) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",detalle_venta)
        conexion2.commit()
    
    print("Elementos de la tabla 2 ingresados con exito!!!")
    
    #Tabla 3 empleado_h
    sentencia3 = """
    select e.rut_empleado, e.id_peluqueria, e.nombre_empleado, e.apellido_empleado, e.id_comuna, s.fecha, s.monto, s.id_sueldo, p.id_comuna
    from empleado e
    inner join peluqueria p on p.id_peluqueria = e.id_peluqueria
    inner join sueldo s on s.rut_empleado = e.rut_empleado;
    """
    cursor1.execute("select id_sueldo from sueldo;")
    sueldos = cursor1.fetchall()
    
    cursor1.execute(sentencia3)
    empleados_h = cursor1.fetchall()
    
    comuna = verificar_dato(comunas,"comuna_h",cursor2)
    if len(comuna) != 0:
        cursor2.execute("insert into comuna_h (id_comuna,nombre) values (%s,%s)",comuna)
        conexion2.commit()
    
    peluqueria = verificar_dato(peluquerias,"peluqueria_h",cursor2)
    if len(peluqeuria) != 0:
        cursor2.execute("insert into peluqueria_h (id_peluqueria) values (%s)",peluqueria)
        conexion2.commit()
    
    sueldo = verificar_dato(sueldos,"sueldo",cursor2)
    if len(sueldo)!=0:
        cursor2.execute("insert into sueldo (id_sueldo) values (%s)",sueldo)
        conexion2.commit()
    
    empleado = verificar_dato(empleados_h,"empleado_h",cursor2)
    if len(empleado) != 0:
        cursor2.execute("insert into empleado_h (rut_empleado,id_peluqueria ,nombre_empleado,apellido_empleado,id_comuna,fecha,monto,id_sueldo,id_comuna_peluqueria) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",empleado)
        conexion2.commit()
    
    print("Elementos de la tabla 3 ingresados con exito!!")
    
    #Tabla 4 ofrece
    sentencia4 = """
    select o.id_ofrece, o.id_peluqueria, p.id_comuna, s.costo_servicio , o.id_servicio
    from ofrece o
    inner join peluqueria p on p.id_peluqueria = o.id_peluqueria
    inner join servicios s on s.id_servicio = o.id_servicio;
    """
    
    cursor1.execute(sentencia4)
    ofreces = cursor1.fetchall()
    
    servicio = verificar_dato(servicios,"servicios_o",cursor2)
    if len(servicio)!=0:
        cursor2.execute("insert into servicios_o (id_servicio, nombre_servicio) values (%s,%s)",servicio)
        conexion2.commit()
    
    comuna = verificar_dato(comunas,"comuna_p",cursor2)
    if len(comuna) != 0:
        cursor2.execute("insert into comuna_p (id_comuna, nombre) values (%s,%s)",comuna)
        conexion2.commit()
            
    
    peluqueria = verificar_dato(peluquerias,"peluqueria_s",cursor2)
    if len(peluqueria) != 0:
        cursor2.execute("insert into peluqueria_s (id_peluqueria) values (%s)",peluqueria)
        conexion2.commit()
            
    ofrece = verificar_dato(ofreces,"ofrece",cursor2)
    if len(ofrece)!=0:
        cursor2.execute("insert into ofrece (id_ofrece, id_peluqueria, id_comuna, costo_servicio, id_servicio) values (%s,%s,%s,%s,%s)",ofrece)
        conexion2.commit()
    
    print("Elementos de la tabla 4 ingresados con exito!!!")
    
    print("Ejecucion finalizada!!")
    cursor1.close()
    conexion1.close()
    cursor2.close()
    conexion2.close()

def verificar_dato(dato,tipo,cursor2):
    query = f"""
        SELECT * From {tipo};
    """
    cursor2.execute(query)
    count = cursor2.fetchall()
    if len(count)==0:
        return dato
    return [elementos for elementos in dato if elementos not in count]

if __name__ == "__main__":
    main()