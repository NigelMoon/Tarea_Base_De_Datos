import psycopg2 as network
import random

random.seed(911)
N_PELUQUERIAS = 100
#Servicios es constante, a no ser que quieran agregar mas
N_CLIENTE = 1000
N_COMPRA = 1000
N_EMPLEADO = 1000
N_VENTA = 1000
N_USA_PRODUCTO = 100
N_PRODUCTO = 100
N_DETALLE_VENTA = random.randint(N_VENTA*5*N_PELUQUERIAS,N_VENTA*10*N_PELUQUERIAS)
N_CITA = 1000
N_TRANSACCION = 1000

"""
comuna, bloque, servicio, producto,
    peluqueria, cliente, usa_producto, transaccion_stock,
    empleado, compra, venta, ofrece,
    cita, detalle_compra, detalle_venta,
    ocurre sueldo
"""

TABLA = [
    "comuna",
    "bloque",
    "servicios",
    "producto",
    "peluqueria",
    "cliente",
    "usa_producto",
    "transaccion_stock",
    "empleado",
    "compra",
    "venta",
    "ofrece",
    "cita",
    "detalle_compra",
    "detalle_venta",
    "ocurre",
    "sueldo"
]

DATOS = {
    'bloque': 'id_bloque',
    'comuna': 'id_comuna, nombre',
    'producto': 'id_producto, precio_compra, nombre_producto, precio_venta',
    'servicios': 'id_servicio, nombre_servicio, costo_servicio',
    'transaccion_stock': 'id_transaccion_stock, cant_transaccion, fecha, tipo_transaccion,id_producto',
    'cliente': 'rut_cliente, sexo, nombre, id_comuna',
    'peluqueria': 'id_peluqueria, id_comuna, direccion',
    'compra': 'id_compra, fecha, total, id_peluqueria',
    'detalle_compra': 'id_detalle_compra, cantidad, subtotal, id_compra, id_producto',
    'venta': 'id_venta, fecha, total, rut_cliente, id_peluqueria',
    'detalle_venta': 'id_detalle_venta, subtotal, cantidad, id_venta, id_producto',
    'usa_producto': 'id_usa_producto, id_producto, id_servicio, fecha',
    'empleado': 'rut_empleado, nombre_empleado, apellido_empleado, id_peluqueria, id_comuna',
    'ofrece': 'id_ofrece, id_peluqueria, id_servicio',
    'cita': 'id_cita, fecha, rut_empleado, id_servicio, id_peluqueria, rut_cliente',
    'ocurre': 'id_ocurre, id_cita, id_bloque',
    'sueldo': 'id_sueldo, fecha, monto, rut_empleado'
}

lista_servicios = [
    "Corte de cabello para hombres",
    "Corte de cabello para mujeres",
    "Corte de cabello unisex",
    "Peinados para ocasiones especiales",
    "Tintes y coloracion de cabello",
    "Mechas y reflejos",
    "Tratamientos capilares",
    "Lavado y secado de cabello",
    "Alisado y ondulado permanente",
    "Tratamientos de keratina",
    "Manicura y pedicura",
    "Depilacion facial",
    "Depilacion corporal",
    "Maquillaje profesional",
    "Tratamientos de spa capilar",
    "Masajes capilares",
    "Extensiones de cabello",
    "Servicios de barberia",
    "Tratamientos para el cuero cabelludo",
    "Asesoria de imagen personalizada",
    "corte de pelo y barba"]

N_SERVICIOS = len(lista_servicios)

def main():
    Bruno = True
    while Bruno:
        try:
            password = input("ingrese la contraseña: ")
            database = input("Ingrese el nombre de la base de datos: ")
            
            CONFIG = {
            'user':'postgres',
            'password':password, #Hay que cambiar en caso de ser otro el que ingresa
            'host':'localhost',
            'port':'5432',
            'database':database #Colocar el nombre de la base de datos original
            }
            conexion = network.connect(**CONFIG)
            cursor = conexion.cursor()
            conexion.rollback()
        except network.OperationalError :
            print("Error de conexion!!!")
        finally:
            Bruno = False
    #comuna
    r = open("comuna.txt","r",encoding="utf-8")
    consulta = r.read()
    r.close()
    cursor.execute(consulta)
    conexion.commit()
    #bloque
    cursor.execute(pato(TABLA[1],DATOS.get(TABLA[1])))
    conexion.commit()
    #servicio
    cursor.execute(pato(TABLA[2],DATOS.get(TABLA[2])))
    conexion.commit()
    #producto
    producto(cursor,conexion)
    #peluqueria
    peluqueria(cursor,conexion)
    #cliente
    cursor.execute(pato(TABLA[5],DATOS.get(TABLA[5])))
    conexion.commit()
    #usa_producto
    usa_producto(cursor,conexion)
    #transaccion
    cursor.execute(pato(TABLA[7],DATOS.get(TABLA[7])))
    conexion.commit()
    #empleado
    cursor.execute(pato(TABLA[8],DATOS.get(TABLA[8])))
    conexion.commit()
    #compra
    compra(cursor,conexion)
    #venta
    cursor.execute(pato(TABLA[10],DATOS.get(TABLA[10])))
    conexion.commit()
    #ofrece
    ofrece(cursor,conexion)
    #cita
    cita(cursor,conexion)
    #detalle_compra
    detalle_compra(cursor,conexion)
    #detalle_venta
    cursor.execute(pato(TABLA[14],DATOS.get(TABLA[14])))
    conexion.commit()
    #ocurre
    cursor.execute(pato(TABLA[15],DATOS.get(TABLA[15])))
    conexion.commit()
    #sueldo
    sueldo(cursor,conexion)
    
    cursor.execute("insert into servicio values (%s,'%s',%s);"%(911,"2001 acaba de llamar... golpearon la segunda torre",37295740000000))
    conexion.commit()
    
    cursor.close()
    conexion.close()
    print("Ejecucion terminada!!!!")
    return 0


nombres=[
			"Adela","Adelaida","Alba","Albina","Alejandra","Almudena","Amelia","Ana",
			"Anastasia","Andrea","Angela","Ananias","Antonia","Araceli","Ariadna",
			"Ascension","Asuncion","Aurea","Aurelia","Aurora","Barbara","Beatriz",
			"Belen","Bernarda","Blanca","Borja","Candida","Carina","Carmen","Carolina",
			"Catalina","Cecilia","Celia","Celina","Clara","Claudia","Clotilde",
			"Concepcion","Consuelo","Cristina","Dorotea","Elena","Elisa","Elvira",
			"Emilia","Epifania","Esperanza","Ester","Esther","Eugenia","Eulalia",
			"Eva","Fabiola","Fatima","Francisca","Gema","Genoveva","Gertrudis",
			"Gisela","Gloria","Guadalupe","Hildegarda","Ines","Inmaculada","Irene",
			"Isabel","Josefa","Josefina","Juana","Laura","Leocadia","Lidia","Liduvina",
			"Lorena","Lucia","Lucrecia","Luisa","Magdalena","Manuela","Margarita",
			"Marina","Marta","Matilde","Mercedes","Milagros","Miriam","Monica",
			"Montserrat","Natalia","Natividad","Nieves","Noelia","Nuria","Olga",
			"Otilia","Patricia","Paula","Petronila","Pilar","Priscila","Purificacion",
			"Raquel","Rebeca","Remedios","Rita","Rosa","Rosalia","Rosario","Salome",
			"Sandra","Sara","Silvia","Sofia","Soledad","Sonia","Susana","Tania","Teofila",
			"Teresa","Trinidad","Ursula","Vanesa","Veronica","Vicenta","Victoria",
			"Vidal","Virginia","Yolanda",
			"Aaron","Abdon","Abel","Abelardo","Abrahan","Absalon","Acacio","Adalberto",
			"Adan","Adolfo","Adon","Adrian","Agustin","Aitor","Albert","Alberto","Alejandro",
			"Alejo","Alfonso","Alfredo","Alicia","Alipio","Alonso","Alvaro","Amadeo","Amaro",
			"Ambrosio","Amparo","Anatolio","Andres","Angel","Angeles","Aniano","Anna","Anselmo",
			"Antero","Antonio","Aquiles","Aranzazu","Arcadio","Aresio","Aristides","Arnaldo",
			"Artemio","Arturo","Atanasio","Augusto","Aureliano","Aurelio","Baldomero","Balduino",
			"Baltasar","Bartolome","Basileo","Beltran","Benedicto","Benigno","Benito","Benjamin",
			"Bernabe","Bernardo","Blas","Bonifacio","Bruno","Calixto","Camilo","Carlos","Carmelo",
			"Casiano","Casimiro","Casio","Cayetano","Cayo","Ceferino","Celso","Cesar","Cesareo",
			"Cipriano","Cirilo","Cirino","Ciro","Claudio","Cleofas","Colombo","Columba","Columbano",
			"Conrado","Constancio","Constantino","Cosme","Cristian","Cristobal","Daciano","Dacio",
			"Damaso","Damian","Daniel","Dario","David","Democrito","Diego","Dimas","Dolores","Domingo",
			"Donato","Edgar","Edmundo","Eduardo","Eduvigis","Efren","Elias","Eliseo","Emiliano",
			"Emilio","Encarnacion","Enrique","Erico","Ernesto","Esdras","Esiquio","Esteban","Eugenio",
			"Eusebio","Evaristo","Ezequiel","Fabian","Fabio","Facundo","Faustino","Fausto","Federico",
			"Feliciano","Felipe","Felix","Fermin","Fernando","Fidel","Fortunato","Francesc","Francisco",
			"Fulgencio","Gabriel","Gerardo","German","Godofredo","Gonzalo","Gregorio","Guido","Guillermo",
			"Gustavo","Guzman","Hector","Heliodoro","Heraclio","Heriberto","Hilarion","Homero","Honorato",
			"Honorio","Hugo","Humberto","Ifigenia","Ignacio","Ildefonso","Inocencio","Ireneo","Isaac",
			"Isaias","Isidro","Ismael","Ivan","Jacinto","Jacob","Jacobo","Jaime","Jaume","Javier","Jeremias",
			"Jeronimo","Jesus","Joan","Joaquim","Joaquin","Joel","Jonas","Jonathan","Jordi",
			"Jorge","Josafat","Jose","Josep","Josue","Juan","Julia","Julian","Julio","Justino",
			"Juvenal","Ladislao","Laureano","Lazaro","Leandro","Leon","Leonardo","Leoncio","Leonor",
			"Leopoldo","Lino","Lorenzo","Lourdes","Lucano","Lucas","Luciano","Luis","Luz",
			"Macario","Manuel","Mar","Marc","Marcelino","Marcelo","Marcial","Marciano","Marcos",
			"Maria","Mariano","Mario","Martin","Mateo","Matias","Mauricio","Maximiliano","Melchor",
			"Miguel","Miqueas","Mohamed","Moises","Narciso","Nazario","Nemesio","Nicanor",
			"Nicodemo","Nicolas","Nicomedes","Noe","Norberto","Octavio","Odon","Onesimo","Orestes",
			"Oriol","Oscar","oscar","Oseas","Oswaldo","Oto","Pablo","Pancracio","Pascual","Patricio",
			"Pedro","Pio","Poncio","Porfirio","Primo","Probo","Rafael","Raimundo","Ramiro","Ramon",
			"Raul","Reinaldo","Renato","Ricardo","Rigoberto","Roberto","Rocio","Rodrigo","Rogelio",
			"Roman","Romualdo","Roque","Rosendo","Ruben","Rufo","Ruperto","Salomon","Salvador",
			"Salvio","Samuel","Sanson","Santiago","Sebastian","Segismundo","Sergio","Severino",
			"Simeon","Simon","Siro","Sixto","Tadeo","Tarsicio","Teodora","Teodosia","Teofanes",
			"Timoteo","Tito","Tobias","Tomas","Tomas","Toribio","Ubaldo","Urbano","Valentin","Valeriano",
			"Velerio","Venancio","Vicente","Victor","Victorino","Victorio","Virgilio","Vladimiro","Wilfredo",
			"Xavier","Zacarias","Zaqueo"
	]

mujer=[
			"Adela","Adelaida","Alba","Albina","Alejandra","Almudena","Amelia","Ana",
			"Anastasia","Andrea","Angela","Ananias","Antonia","Araceli","Ariadna",
			"Ascension","Asuncion","Aurea","Aurelia","Aurora","Barbara","Beatriz",
			"Belen","Bernarda","Blanca","Borja","Candida","Carina","Carmen","Carolina",
			"Catalina","Cecilia","Celia","Celina","Clara","Claudia","Clotilde",
			"Concepcion","Consuelo","Cristina","Dorotea","Elena","Elisa","Elvira",
			"Emilia","Epifania","Esperanza","Ester","Esther","Eugenia","Eulalia",
			"Eva","Fabiola","Fatima","Francisca","Gema","Genoveva","Gertrudis",
			"Gisela","Gloria","Guadalupe","Hildegarda","Ines","Inmaculada","Irene",
			"Isabel","Josefa","Josefina","Juana","Laura","Leocadia","Lidia","Liduvina",
			"Lorena","Lucia","Lucrecia","Luisa","Magdalena","Manuela","Margarita",
			"Marina","Marta","Matilde","Mercedes","Milagros","Miriam","Monica",
			"Montserrat","Natalia","Natividad","Nieves","Noelia","Nuria","Olga",
			"Otilia","Patricia","Paula","Petronila","Pilar","Priscila","Purificacion",
			"Raquel","Rebeca","Remedios","Rita","Rosa","Rosalia","Rosario","Salome",
			"Sandra","Sara","Silvia","Sofia","Soledad","Sonia","Susana","Tania","Teofila",
			"Teresa","Trinidad","Ursula","Vanesa","Veronica","Vicenta","Victoria",
			"Vidal","Virginia","Yolanda"]

hombre=[
			"Aaron","Abdon","Abel","Abelardo","Abrahan","Absalon","Acacio","Adalberto",
			"Adan","Adolfo","Adon","Adrian","Agustin","Aitor","Albert","Alberto","Alejandro",
			"Alejo","Alfonso","Alfredo","Alicia","Alipio","Alonso","Alvaro","Amadeo","Amaro",
			"Ambrosio","Amparo","Anatolio","Andres","Angel","Angeles","Aniano","Anna","Anselmo",
			"Antero","Antonio","Aquiles","Aranzazu","Arcadio","Aresio","Aristides","Arnaldo",
			"Artemio","Arturo","Atanasio","Augusto","Aureliano","Aurelio","Baldomero","Balduino",
			"Baltasar","Bartolome","Basileo","Beltran","Benedicto","Benigno","Benito","Benjamin",
			"Bernabe","Bernardo","Blas","Bonifacio","Bruno","Calixto","Camilo","Carlos","Carmelo",
			"Casiano","Casimiro","Casio","Cayetano","Cayo","Ceferino","Celso","Cesar","Cesareo",
			"Cipriano","Cirilo","Cirino","Ciro","Claudio","Cleofas","Colombo","Columba","Columbano",
			"Conrado","Constancio","Constantino","Cosme","Cristian","Cristobal","Daciano","Dacio",
			"Damaso","Damian","Daniel","Dario","David","Democrito","Diego","Dimas","Dolores","Domingo",
			"Donato","Edgar","Edmundo","Eduardo","Eduvigis","Efren","Elias","Eliseo","Emiliano",
			"Emilio","Encarnacion","Enrique","Erico","Ernesto","Esdras","Esiquio","Esteban","Eugenio",
			"Eusebio","Evaristo","Ezequiel","Fabian","Fabio","Facundo","Faustino","Fausto","Federico",
			"Feliciano","Felipe","Felix","Fermin","Fernando","Fidel","Fortunato","Francesc","Francisco",
			"Fulgencio","Gabriel","Gerardo","German","Godofredo","Gonzalo","Gregorio","Guido","Guillermo",
			"Gustavo","Guzman","Hector","Heliodoro","Heraclio","Heriberto","Hilarion","Homero","Honorato",
			"Honorio","Hugo","Humberto","Ifigenia","Ignacio","Ildefonso","Inocencio","Ireneo","Isaac",
			"Isaias","Isidro","Ismael","Ivan","Jacinto","Jacob","Jacobo","Jaime","Jaume","Javier","Jeremias",
			"Jeronimo","Jesus","Joan","Joaquim","Joaquin","Joel","Jonas","Jonathan","Jordi",
			"Jorge","Josafat","Jose","Josep","Josue","Juan","Julia","Julian","Julio","Justino",
			"Juvenal","Ladislao","Laureano","Lazaro","Leandro","Leon","Leonardo","Leoncio","Leonor",
			"Leopoldo","Lino","Lorenzo","Lourdes","Lucano","Lucas","Luciano","Luis","Luz",
			"Macario","Manuel","Mar","Marc","Marcelino","Marcelo","Marcial","Marciano","Marcos",
			"Maria","Mariano","Mario","Martin","Mateo","Matias","Mauricio","Maximiliano","Melchor",
			"Miguel","Miqueas","Mohamed","Moises","Narciso","Nazario","Nemesio","Nicanor",
			"Nicodemo","Nicolas","Nicomedes","Noe","Norberto","Octavio","Odon","Onesimo","Orestes",
			"Oriol","Oscar","oscar","Oseas","Oswaldo","Oto","Pablo","Pancracio","Pascual","Patricio",
			"Pedro","Pio","Poncio","Porfirio","Primo","Probo","Rafael","Raimundo","Ramiro","Ramon",
			"Raul","Reinaldo","Renato","Ricardo","Rigoberto","Roberto","Rocio","Rodrigo","Rogelio",
			"Roman","Romualdo","Roque","Rosendo","Ruben","Rufo","Ruperto","Salomon","Salvador",
			"Salvio","Samuel","Sanson","Santiago","Sebastian","Segismundo","Sergio","Severino",
			"Simeon","Simon","Siro","Sixto","Tadeo","Tarsicio","Teodora","Teodosia","Teofanes",
			"Timoteo","Tito","Tobias","Tomas","Tomas","Toribio","Ubaldo","Urbano","Valentin","Valeriano",
			"Velerio","Venancio","Vicente","Victor","Victorino","Victorio","Virgilio","Vladimiro","Wilfredo",
			"Xavier","Zacarias","Zaqueo"
	]

apellidos =[ 
            "Aguilar","Alonso","Alvarez","Arias","Benitez","Blanco","Blesa","Bravo",
			"Caballero","Cabrera","Calvo","Cambil","Campos","Cano","Carmona","Carrasco",
			"Castillo","Castro","Cortes","Crespo","Cruz","Delgado","Diaz","Diez","Dominguez",
			"Duran","Esteban","Fernandez","Ferrer","Flores","Fuentes","Gallardo","Gallego",
			"Garcia","Garrido","Gil","Gimenez","Gomez","Gonzalez","Guerrero","Gutierrez",
			"Hernandez","Herrera","Herrero","Hidalgo","Iglesias","Jimenez","Leon","Lopez",
			"Lorenzo","Lozano","Marin","Marquez","Martin","Martinez","Medina","Mendez",
			"Molina","Montero","Montoro","Mora","Morales","Moreno","Moya","Navarro","Nieto",
			"Ortega","Ortiz","Parra","Pascual","Pastor","Perez","Prieto","Ramirez","Ramos",
			"Rey","Reyes","Rodriguez","Roman","Romero","Rubio","Ruiz","Saez","Sanchez",
			"Santana","Santiago","Santos","Sanz","Serrano","Soler","Soto","Suarez",
			"Torres","Vargas","Vazquez","Vega","Velasco","Vicente","Vidal"]

def bloque():
    datos=""
    for i in range(0,8):
        datos+="(%s),\n"%str(i+1)
    datos+="(10);\n"
    return datos

def servicio():
    datos=""
    precio = 0
    n=len(lista_servicios)
    for i in range(n-1):
        if i == 1:
            precio = 500000
        else:
            precio = random.randint(5000,300000)
        datos+="(%s,'%s',%s),\n"%(str(i+1),lista_servicios[i],precio)
    precio = random.randint(5000,300000)
    datos+="(%s,'%s',%s);\n"%(str(n),lista_servicios[n-1],precio)
    return datos
    
def cliente():
    datos=""
    for i in range(0,N_CLIENTE):
        sexo = random.choice(("M","F"))
        match sexo:
            case "M":
                nombre = random.choice(hombre)
            case "F":
                nombre = random.choice(mujer)
            case _:
                return ""
        comuna = random.choice(range(1,201))
        datos+="(%s,'%s','%s',%s),\n"%(str(10000000+i),sexo,nombre,str(comuna))
        
    sexo = random.choice(("M","F"))
    match sexo:
            case "M":
                nombre = random.choice(hombre)
            case "F":
                nombre = random.choice(mujer)
            case _:
                return ""
    comuna = random.choice(range(1,201))
    datos+="(%s,'%s','%s',%s);\n"%(str(10000000+N_CLIENTE),sexo,nombre,str(comuna))
    return datos

def empleado():
    datos = ""
    for i in range(N_EMPLEADO):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        comuna = random.choice(range(1,201))
        datos+="(%s,'%s','%s',%s,%s),\n"%(str(10000000+N_CLIENTE*2+i),nombre,apellido,str(i//10+1),str(comuna))
    
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    comuna = random.choice(range(1,201))
    datos+="(%s,'%s','%s',%s,%s);\n"%(str(10000000+N_CLIENTE*2+N_EMPLEADO),nombre,apellido,str(1000//10),str(comuna))
    
    return datos

#aqui falta un cambio

def venta():
    #id_venta, fecha, total, rut_cliente
    datos = ""
    for i in range(N_VENTA*N_PELUQUERIAS*5):
        fecha = f"'{2019+i//(N_VENTA*N_PELUQUERIAS)%5}-{random.randint(1,12)}-{random.randint(1,28)}'"
        datos+=f"({i+1},{fecha},{random.randint(1,200)},{random.randint(10000000,10000000+N_CLIENTE)},{i//(N_VENTA*5)%N_PELUQUERIAS+1}),\n"
    fecha = f"'{2023}-{random.randint(1,12)}-{random.randint(1,28)}'"
    datos+=f"({N_VENTA*5*N_PELUQUERIAS+1},{fecha},{random.randint(1,200)},{random.randint(10000000,10000000+N_CLIENTE)},{N_PELUQUERIAS});\n"
    return datos

def ocurre():
    #id_ocurre, id_cita, id_bloque
    datos = ""
    const = 1
    for i in range(N_CITA-1):
        bloque = random.randint(1,10)
        datos+=f"({const},{i},{bloque}),\n"
        while random.randint(0,1)!=0 and bloque<12:
            const+=1
            bloque+=1
            datos+=f"({const},{i+1},{bloque}),\n"
    const+=1
    bloque = random.randint(1,10)
    while True:
        if random.randint(0,1) == 1 and bloque<12:
            datos+=f"({const},{N_CITA},{bloque}),\n"
            const+=1
            bloque+=1
        else:
            datos+=f"({const},{N_CITA},{bloque});\n"
            return datos

def detalle_venta():
    #id_detalle_venta, subtotal, cantidad, id_venta, id_producto
	datos = ""
	for i in range(N_DETALLE_VENTA):
		cantidad = random.randint(1,1000)
		subtotal = random.randint(1,30)*cantidad
		datos+=f"({i+1},{subtotal},{cantidad},{random.randint(1,N_VENTA*5*N_PELUQUERIAS+1)},{random.randint(1,N_PRODUCTO)}),\n"
	cantidad = random.randint(1,1000)
	subtotal = random.randint(1,30)*cantidad
	datos+=f"({N_DETALLE_VENTA+1},{subtotal},{cantidad},{random.randint(1,N_VENTA*5*N_PELUQUERIAS+1)},{random.randint(1,N_PRODUCTO)});\n"
	return datos

def transaccion_stack():
    #id_transaccion_stack, cant_transaccion, fecha, tipo_transaccion, id_producto
    datos = ""
    tipo = ["servicio","compra","venta"]
    for i in range(N_TRANSACCION*5):
        t = random.choice(tipo)
        match t:
            case "servicio":
                total = random.randint(0,2)
                locura = random.randint(1,N_PRODUCTO)
            case "compra":
                total = random.randint(1,20)
                locura = random.randint(1,N_PRODUCTO)
            case "venta":
                total = random.randint(100,1000)
                locura = random.randint(1,N_PRODUCTO)
            case _:
                return None
        
        fecha = f"{2019+i//N_TRANSACCION}-{random.randint(1,12)}-{random.randint(1,28)}"
        datos+=f"({i+1},{total},'{fecha}','{t}',{locura}),\n"
    t = random.choice(tipo)
    match t:
        case "servicio":
            total = random.randint(0,2)
            locura = random.randint(1,N_PRODUCTO)
        case "compra":
            total = random.randint(1,20)
            locura = random.randint(1,N_PRODUCTO)
        case "venta":
            total = random.randint(100,1000)
            locura = random.randint(1,N_PRODUCTO)
        case _:
            return None
        
    fecha = f"{2023}-{random.randint(1,12)}-{random.randint(1,28)}"
    datos+=f"({N_TRANSACCION*5+1},{total},'{fecha}','{t}',{locura});\n"
    return datos

def pato(a,b):
    insert = "INSERT INTO %s (%s) VALUES\n"%(a,b)
    match a:
        case "bloque":
            insert+=bloque()
        case "servicios":
            insert+=servicio()
        case "cliente":
            insert+=cliente()
        case "empleado":
            insert+=empleado()
        case "venta":
            insert+=venta()
        case "detalle_venta":
            insert+=detalle_venta()
        case "transaccion_stock":
            insert+=transaccion_stack()
        case "ocurre":
            insert+=ocurre()
        case _:
            print("-<>-")
            return 0
    return insert

def producto(cursor,conexion):
    tipo_producto = [
        "Champús",
        "Acondicionador",
        "Mascarillas Capilar",
        "Tratamientos Capilar",
        "Gel",
        "Cera",
        "Espuma",
        "Mousse",
        "Spray",
        "Laca",
        "Crema de Peinado",
        "Aceite Capilar",
        "Serum Capilar",
        "Protector Térmico",
        "Ampollas" ]
    propiedades= [
        "Hidratante",
        "Otorga brillo",
        "Revitalizante",
        "Reparador",
        "Voluminizador",
        "Anticaspa",
        "Antifrizz",
        "Protector térmico",
        "Suavizante",
        "Fortalecedor",
        "Nutritivo",
        "Anticaída",
        "Definidor de rizos",
        "Acondicionador profundo",
        "Desenredante",
        "Purificante",
        "Refrescante",
        "Antioxidante",
        "Reestructurante",
        "Anti-edad",
        "Calmante",
        "Desintoxicante",
        "Termoactivador",
        "Iluminador",
        "Equilibrante",
        "Sebo-regulador",
        "Protector de color",
        "Alisador",
        "Protector UV",
        "Estimulante del crecimiento"
    ]


    # Genera los datos de inserción
    data_to_insert = []
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1,N_PRODUCTO+1):
        producto = random.choice(tipo_producto)
        propiedad = random.choice(propiedades)
        precio_venta = random.randint(50000, 200000)
        precio_compra = random.randint(30000, 150000)
        nombre = producto + " " + propiedad
        data_to_insert.append((i, precio_compra, nombre, precio_venta))

    # Consulta de inserción
    insert_query = "INSERT INTO producto (id_producto, precio_compra, nombre_producto, precio_venta) VALUES (%s, %s,%s,%s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit()

def peluqueria(cursor,conexion):
    data_to_insert = []
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, N_PELUQUERIAS+1):
        comuna = random.randint(1, 200)
        data_to_insert.append((i, comuna))

    # Consulta de inserción
    insert_query = "INSERT INTO peluqueria (id_peluqueria, id_comuna) VALUES (%s, %s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit()

def usa_producto(cursor,conexion):
    data_to_insert = []
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, N_USA_PRODUCTO*5+1):
        # i = id_usa_producto
        producto = random.randint(1, 100) #depende de cuantos datos tenga la tabla producto    
        year = 2019+i//N_USA_PRODUCTO
        month = random.randint(1,12)
        day = random.randint(1,28)
        fecha = f"{year}-{month}-{day}"
        servicio = random.randint(1,N_SERVICIOS) #Depende de la cantidad de datos en la tabla servicio
        data_to_insert.append((i, producto, servicio, fecha))
    # Consulta de inserción
    insert_query = "INSERT INTO usa_producto (id_usa_producto, id_producto, id_servicio, fecha) VALUES (%s, %s, %s, %s)"

    cursor.executemany(insert_query,data_to_insert)
    conexion.commit()

def compra(cursor,conexion):
    data_to_insert = []
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, N_COMPRA*N_PELUQUERIAS*5+1):
        year = 2019+i//(N_COMPRA*N_PELUQUERIAS)%5
        month = random.randint(1,12)
        day = random.randint(1,28)
        fecha = f"{year}-{month}-{day}"
        peluqueria = 1 + i//(N_COMPRA*5)%N_PELUQUERIAS #depende de cuantos datos tenga la tabla peluqueria
        total = random.randint(5000,300000) 
        data_to_insert.append((i, fecha, total, peluqueria))

    # Consulta de inserción
    insert_query = "INSERT INTO compra (id_compra, fecha, total, id_peluqueria) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit()

def ofrece(cursor,conexion):
    data_to_insert = []
    id_ofrece = 1
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, N_PELUQUERIAS+1):
        for j in range(1,N_SERVICIOS+1):
            if j<=3:
                data_to_insert.append((id_ofrece, i, j))
                id_ofrece+=1
            else:
                if random.choice((0,1))==0:
                    data_to_insert.append((id_ofrece, i, j))
                    id_ofrece+=1

    # Consulta de inserción
    insert_query = "INSERT INTO ofrece (id_ofrece, id_peluqueria, id_servicio) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit()

def cita(cursor,conexion):
    data_to_insert = []
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, N_CITA*5*N_PELUQUERIAS+1):
        peluqueria = 1+i//(N_COMPRA*5)%N_PELUQUERIAS
        cursor.execute(f"select o.id_servicio from ofrece o where o.id_peluqueria = {peluqueria};")
        servicio = random.choice(cursor.fetchall())[0]
        year = 2019+i//(N_CITA*N_PELUQUERIAS)%5
        month = random.randint(1,12)
        day = random.randint(1,28)
        fecha = f"{year}-{month}-{day}"
        rut_cliente = random.randint(10000000,10000000+N_CLIENTE)
        rut_empleado = random.randint(10000000+N_CLIENTE*2, 10000000+N_EMPLEADO+N_CLIENTE*2) #falta la tabla de empleado y ver como seran los ruts
        data_to_insert.append((i, fecha, rut_empleado, servicio, peluqueria, rut_cliente))

    # Consulta de inserción
    insert_query = "INSERT INTO cita (id_cita, fecha, rut_empleado ,id_servicio, id_peluqueria, rut_cliente) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit()    

def detalle_compra(cursor,conexion):
    # Genera los datos de inserción
    data_to_insert = []
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, N_COMPRA*5*N_PELUQUERIAS*2+1):
        cantidad = random.randint(1,20) #suponiendo un maximo 20
        producto = random.randint(1, 100) #depende de cuantos datos tenga la tabla producto
        subtotal = random.randint(1, 200)
        id_compra = random.randint(1,N_COMPRA*5*N_PELUQUERIAS) #depende de cuantos datos tenga la tabla compra
        data_to_insert.append((i, cantidad, subtotal, id_compra, producto))

    # Consulta de inserción
    insert_query = "INSERT INTO detalle_compra (id_detalle_compra, cantidad, subtotal, id_compra, id_producto) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit() 

def sueldo(cursor,conexion):
    data_to_insert = []
    cant_sueldos = random.randint(N_EMPLEADO,N_EMPLEADO*5)
    #ojo : hay que ir actualizando los indices del for a medida de que ingresamos datos!
    for i in range(1, cant_sueldos+1):
        monto = random.randint(300000,500000)
        year = random.randint(2019,2023)
        month = random.randint(1,12)
        day = random.randint(1,28)
        fecha = f"{year}-{month}-{day}"
        rut_empleado = random.randint(10000000+N_CLIENTE*2, 10000000+N_CLIENTE*2+N_EMPLEADO)
        data_to_insert.append((i, fecha, monto, rut_empleado))

    # Consulta de inserción
    insert_query = "INSERT INTO sueldo (id_sueldo, fecha, monto, rut_empleado) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_query,data_to_insert)
    conexion.commit() 
    
if __name__ == "__main__":
    main()
