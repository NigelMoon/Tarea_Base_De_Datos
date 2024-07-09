-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public IS 'standard public schema';
-- public.bloque definition

-- Drop table

-- DROP TABLE public.bloque;

CREATE TABLE public.bloque (
	id_bloque int4 NOT NULL, -- identificador unico del bloque. Un bloque equivale a una hora,¶1: 8:00 - 9:00 (por ejemplo)¶2: 9:00 - 10:00
	CONSTRAINT bloque_pk PRIMARY KEY (id_bloque)
);
COMMENT ON TABLE public.bloque IS 'tabla de dimensiones que almacena informacion sobre los bloques de horario en una cita';

-- Column comments

COMMENT ON COLUMN public.bloque.id_bloque IS 'identificador unico del bloque. Un bloque equivale a una hora,
1: 8:00 - 9:00 (por ejemplo)
2: 9:00 - 10:00';


-- public.cliente definition

-- Drop table

-- DROP TABLE public.cliente;

CREATE TABLE public.cliente (
	rut_cliente int4 NOT NULL, -- identificador unico del cliente
	nombre varchar NOT NULL, -- nombre del cliente a atender
	CONSTRAINT cliente_pk PRIMARY KEY (rut_cliente)
);
COMMENT ON TABLE public.cliente IS 'tabla de dimension que almacena información acerca del cliente de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.cliente.rut_cliente IS 'identificador unico del cliente';
COMMENT ON COLUMN public.cliente.nombre IS 'nombre del cliente a atender';


-- public.clienteventa definition

-- Drop table

-- DROP TABLE public.clienteventa;

CREATE TABLE public.clienteventa (
	rut_cliente int4 NOT NULL, -- identificador unico del cliente
	nombre varchar NOT NULL,
	CONSTRAINT clienteventa_pk PRIMARY KEY (rut_cliente)
);
COMMENT ON TABLE public.clienteventa IS 'tabla de dimension que almacena información acerca del cliente de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.clienteventa.rut_cliente IS 'identificador unico del cliente';


-- public.comuna definition

-- Drop table

-- DROP TABLE public.comuna;

CREATE TABLE public.comuna (
	id_comuna int4 NOT NULL, -- id de la comuna
	nombre varchar NULL, -- nombre de la comuna
	CONSTRAINT comuna_pk PRIMARY KEY (id_comuna)
);
COMMENT ON TABLE public.comuna IS 'Tabla de dimension que almacena varias comunas';

-- Column comments

COMMENT ON COLUMN public.comuna.id_comuna IS 'id de la comuna';
COMMENT ON COLUMN public.comuna.nombre IS 'nombre de la comuna';


-- public.comuna_c definition

-- Drop table

-- DROP TABLE public.comuna_c;

CREATE TABLE public.comuna_c (
	id_comuna int4 NOT NULL, -- id de la comuna
	nombre varchar NULL, -- nombre de la comuna
	CONSTRAINT comuna_c_pk PRIMARY KEY (id_comuna)
);
COMMENT ON TABLE public.comuna_c IS 'Tabla de dimension que almacena varias comunas';

-- Column comments

COMMENT ON COLUMN public.comuna_c.id_comuna IS 'id de la comuna';
COMMENT ON COLUMN public.comuna_c.nombre IS 'nombre de la comuna';


-- public.comuna_h definition

-- Drop table

-- DROP TABLE public.comuna_h;

CREATE TABLE public.comuna_h (
	id_comuna int4 NOT NULL, -- id de la comuna
	nombre varchar NULL, -- nombre de la comuna
	CONSTRAINT comuna_h_pk PRIMARY KEY (id_comuna)
);
COMMENT ON TABLE public.comuna_h IS 'Tabla de dimension que almacena varias comunas';

-- Column comments

COMMENT ON COLUMN public.comuna_h.id_comuna IS 'id de la comuna';
COMMENT ON COLUMN public.comuna_h.nombre IS 'nombre de la comuna';


-- public.comuna_p definition

-- Drop table

-- DROP TABLE public.comuna_p;

CREATE TABLE public.comuna_p (
	id_comuna int4 NOT NULL, -- id de la comuna
	nombre varchar NULL, -- nombre de la comuna
	CONSTRAINT comuna_p_pk PRIMARY KEY (id_comuna)
);
COMMENT ON TABLE public.comuna_p IS 'Tabla que almacena varias comunas';

-- Column comments

COMMENT ON COLUMN public.comuna_p.id_comuna IS 'id de la comuna';
COMMENT ON COLUMN public.comuna_p.nombre IS 'nombre de la comuna';


-- public.empleado definition

-- Drop table

-- DROP TABLE public.empleado;

CREATE TABLE public.empleado (
	rut_empleado int4 NOT NULL, -- identificador unico del empleado
	nombre_empleado varchar NOT NULL,
	apellido_empleado varchar NOT NULL,
	CONSTRAINT empleado_pk PRIMARY KEY (rut_empleado)
);
COMMENT ON TABLE public.empleado IS 'Tabla de dimensiones que almacena información de un empleado de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.empleado.rut_empleado IS 'identificador unico del empleado';


-- public.peluqueria definition

-- Drop table

-- DROP TABLE public.peluqueria;

CREATE TABLE public.peluqueria (
	id_peluqueria int4 NOT NULL, -- identificador unico de la peluqueria
	CONSTRAINT peluqueria_pk PRIMARY KEY (id_peluqueria)
);
COMMENT ON TABLE public.peluqueria IS 'Tabla de dimensión que almacena información de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.peluqueria.id_peluqueria IS 'identificador unico de la peluqueria';


-- public.peluqueria_h definition

-- Drop table

-- DROP TABLE public.peluqueria_h;

CREATE TABLE public.peluqueria_h (
	id_peluqueria int4 NOT NULL, -- identificador unico de la peluqueria
	CONSTRAINT peluqueria_h_pk PRIMARY KEY (id_peluqueria)
);
COMMENT ON TABLE public.peluqueria_h IS 'Tabla de dimensión que almacena información de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.peluqueria_h.id_peluqueria IS 'identificador unico de la peluqueria';


-- public.peluqueria_s definition

-- Drop table

-- DROP TABLE public.peluqueria_s;

CREATE TABLE public.peluqueria_s (
	id_peluqueria int4 NOT NULL, -- identificador unico de la peluqueria
	CONSTRAINT peluqueria_s_pk PRIMARY KEY (id_peluqueria)
);
COMMENT ON TABLE public.peluqueria_s IS 'Tabla de dimensiones centrada en peluqueria';

-- Column comments

COMMENT ON COLUMN public.peluqueria_s.id_peluqueria IS 'identificador unico de la peluqueria';


-- public.peluqueria_v definition

-- Drop table

-- DROP TABLE public.peluqueria_v;

CREATE TABLE public.peluqueria_v (
	id_peluqueria int4 NOT NULL, -- identificador unico de la peluqueria
	CONSTRAINT peluqueria__v_pk PRIMARY KEY (id_peluqueria)
);
COMMENT ON TABLE public.peluqueria_v IS 'Tabla de dimensión que almacena información de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.peluqueria_v.id_peluqueria IS 'identificador unico de la peluqueria';


-- public.producto definition

-- Drop table

-- DROP TABLE public.producto;

CREATE TABLE public.producto (
	nombre_producto varchar NULL, -- nombre del producto
	id_producto int4 NOT NULL, -- identificador del producto
	CONSTRAINT productos_pk PRIMARY KEY (id_producto)
);
COMMENT ON TABLE public.producto IS 'Datos sobre un producto tanto de uso interno de la peluquería como de venta';

-- Column comments

COMMENT ON COLUMN public.producto.nombre_producto IS 'nombre del producto';
COMMENT ON COLUMN public.producto.id_producto IS 'identificador del producto';


-- public.servicios definition

-- Drop table

-- DROP TABLE public.servicios;

CREATE TABLE public.servicios (
	id_servicio int4 NOT NULL, -- identificador unico del servicio
	nombre_servicio varchar NOT NULL, -- nombre del servicio
	CONSTRAINT servicios_pk PRIMARY KEY (id_servicio)
);
COMMENT ON TABLE public.servicios IS 'Tabla de dimension que almacena datos de los servicios que ofrece una peluqueria';

-- Column comments

COMMENT ON COLUMN public.servicios.id_servicio IS 'identificador unico del servicio';
COMMENT ON COLUMN public.servicios.nombre_servicio IS 'nombre del servicio';


-- public.servicios_o definition

-- Drop table

-- DROP TABLE public.servicios_o;

CREATE TABLE public.servicios_o (
	nombre_servicio varchar NULL, -- nombre del servicio
	id_servicio int4 NOT NULL, -- identificador del servicio
	CONSTRAINT servicios_o_pk PRIMARY KEY (id_servicio)
);
COMMENT ON TABLE public.servicios_o IS 'tabla de dimesiones que almacena informacion de los servicios';

-- Column comments

COMMENT ON COLUMN public.servicios_o.nombre_servicio IS 'nombre del servicio';
COMMENT ON COLUMN public.servicios_o.id_servicio IS 'identificador del servicio';


-- public.sueldo definition

-- Drop table

-- DROP TABLE public.sueldo;

CREATE TABLE public.sueldo (
	id_sueldo int4 NOT NULL, -- identificador unico del sueldo de un empleado
	CONSTRAINT sueldo_pk PRIMARY KEY (id_sueldo)
);
COMMENT ON TABLE public.sueldo IS 'Tabla de dimensiones que almacena información acerca del sueldo de un empleado';

-- Column comments

COMMENT ON COLUMN public.sueldo.id_sueldo IS 'identificador unico del sueldo de un empleado';


-- public.venta definition

-- Drop table

-- DROP TABLE public.venta;

CREATE TABLE public.venta (
	id_venta int4 NOT NULL, -- identificador unico de la venta
	CONSTRAINT venta_pk PRIMARY KEY (id_venta)
);
COMMENT ON TABLE public.venta IS 'tabla de dimensiones que almacena información acerca de una venta';

-- Column comments

COMMENT ON COLUMN public.venta.id_venta IS 'identificador unico de la venta';


-- public.cita definition

-- Drop table

-- DROP TABLE public.cita;

CREATE TABLE public.cita (
	id_cita int4 NOT NULL, -- identificador unico de cita
	fecha date NOT NULL, -- fecha de la cita
	rut_empleado int4 NOT NULL, -- identificador unico del empleado a cargo de atender la cita
	id_peluqueria int4 NOT NULL, -- identificador unico de la peluqueria donde será la cita
	id_servicio int4 NOT NULL, -- identificador unico del servicio a ofrecer durante la cita
	rut_cliente int4 NOT NULL, -- identificador unico del cliente a atender durante la cita
	id_comuna_cliente int4 NOT NULL, -- identificador de la comuna del cliente
	id_comuna_empleado int4 NOT NULL, -- Identificador de la comuna del empleado a cargo de la cita
	id_bloque_inicio int4 NOT NULL, -- Identificador del bloque en el que se inicia la cita
	costo_servicio int4 NULL, -- costo del servicio proporcionado
	id_comuna_peluqueria int4 NULL, -- identificador unico de la comuna en donde está localizada la peluqueria
	sexo varchar NULL, -- sexo del cliente a atender
	id_bloque_fin int4 NOT NULL, -- Identificador del bloque en el que se finaliza la cita¶(si una cita utiliza solo un bloque entonces bloque_inicio = bloque_fin)
	CONSTRAINT cita_pk PRIMARY KEY (id_cita),
	CONSTRAINT cita_bloque_fk FOREIGN KEY (id_bloque_inicio) REFERENCES public.bloque(id_bloque),
	CONSTRAINT cita_cliente_fk FOREIGN KEY (rut_cliente) REFERENCES public.cliente(rut_cliente),
	CONSTRAINT cita_empleado_fk FOREIGN KEY (rut_empleado) REFERENCES public.empleado(rut_empleado),
	CONSTRAINT cita_peluqueria_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria(id_peluqueria),
	CONSTRAINT cita_servicios_fk FOREIGN KEY (id_servicio) REFERENCES public.servicios(id_servicio),
	CONSTRAINT comuna_c_fk FOREIGN KEY (id_comuna_cliente) REFERENCES public.comuna(id_comuna),
	CONSTRAINT comuna_e_fk FOREIGN KEY (id_comuna_empleado) REFERENCES public.comuna(id_comuna)
);
COMMENT ON TABLE public.cita IS 'primera tabla de hechos del modelo de analisis';

-- Column comments

COMMENT ON COLUMN public.cita.id_cita IS 'identificador unico de cita';
COMMENT ON COLUMN public.cita.fecha IS 'fecha de la cita';
COMMENT ON COLUMN public.cita.rut_empleado IS 'identificador unico del empleado a cargo de atender la cita';
COMMENT ON COLUMN public.cita.id_peluqueria IS 'identificador unico de la peluqueria donde será la cita';
COMMENT ON COLUMN public.cita.id_servicio IS 'identificador unico del servicio a ofrecer durante la cita';
COMMENT ON COLUMN public.cita.rut_cliente IS 'identificador unico del cliente a atender durante la cita';
COMMENT ON COLUMN public.cita.id_comuna_cliente IS 'identificador de la comuna del cliente';
COMMENT ON COLUMN public.cita.id_comuna_empleado IS 'Identificador de la comuna del empleado a cargo de la cita';
COMMENT ON COLUMN public.cita.id_bloque_inicio IS 'Identificador del bloque en el que se inicia la cita';
COMMENT ON COLUMN public.cita.costo_servicio IS 'costo del servicio proporcionado';
COMMENT ON COLUMN public.cita.id_comuna_peluqueria IS 'identificador unico de la comuna en donde está localizada la peluqueria';
COMMENT ON COLUMN public.cita.sexo IS 'sexo del cliente a atender';
COMMENT ON COLUMN public.cita.id_bloque_fin IS 'Identificador del bloque en el que se finaliza la cita
(si una cita utiliza solo un bloque entonces bloque_inicio = bloque_fin)';


-- public.detalle_venta definition

-- Drop table

-- DROP TABLE public.detalle_venta;

CREATE TABLE public.detalle_venta (
	id_detalle_venta int4 NOT NULL, -- Identificador de la transaccion
	id_venta int4 NOT NULL, -- identificador unico de la venta asociada al detalle
	id_producto int4 NOT NULL, -- identificador unico del producto asociada a la venta
	precio_venta int4 NULL, -- Precio al que se vende el producto en la peluqueria
	total int4 NULL, -- Total de la venta
	fecha date NOT NULL, -- fecha donde se produce la venta
	sexo varchar NOT NULL, -- sexo del cliente a atender
	id_comuna int4 NOT NULL, -- identificador unico de la comuna en la que reside el cliente
	rut_cliente int4 NULL, -- Identificador del cliente que hace la compra
	id_peluqueria int4 NOT NULL,
	id_comuna_peluqueria int4 NULL,
	subtotal int4 NULL, -- Subtotal calculado por el precio_venta de un producto * cantidad
	cantidad int4 NULL, -- cantidad de producto en la venta
	CONSTRAINT detalle_venta_pk PRIMARY KEY (id_detalle_venta),
	CONSTRAINT detalle_venta_clienteventa_fk FOREIGN KEY (rut_cliente) REFERENCES public.clienteventa(rut_cliente),
	CONSTRAINT detalle_venta_comuna_c_fk FOREIGN KEY (id_comuna) REFERENCES public.comuna_c(id_comuna),
	CONSTRAINT detalle_venta_peluqueria_v_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria_v(id_peluqueria),
	CONSTRAINT detalle_venta_producto_fk FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto),
	CONSTRAINT detalle_venta_venta_fk FOREIGN KEY (id_venta) REFERENCES public.venta(id_venta),
	CONSTRAINT transaccion_stock_comuna_c_fk FOREIGN KEY (id_comuna_peluqueria) REFERENCES public.comuna_c(id_comuna)
);
COMMENT ON TABLE public.detalle_venta IS 'tabla de hechos que almacena información detallada sobre las transacciones en donde el stock varía según la venta de productos';

-- Column comments

COMMENT ON COLUMN public.detalle_venta.id_detalle_venta IS 'Identificador de la transaccion';
COMMENT ON COLUMN public.detalle_venta.id_venta IS 'identificador unico de la venta asociada al detalle';
COMMENT ON COLUMN public.detalle_venta.id_producto IS 'identificador unico del producto asociada a la venta';
COMMENT ON COLUMN public.detalle_venta.precio_venta IS 'Precio al que se vende el producto en la peluqueria';
COMMENT ON COLUMN public.detalle_venta.total IS 'Total de la venta';
COMMENT ON COLUMN public.detalle_venta.fecha IS 'fecha donde se produce la venta';
COMMENT ON COLUMN public.detalle_venta.sexo IS 'sexo del cliente a atender';
COMMENT ON COLUMN public.detalle_venta.id_comuna IS 'identificador unico de la comuna en la que reside el cliente';
COMMENT ON COLUMN public.detalle_venta.rut_cliente IS 'Identificador del cliente que hace la compra';
COMMENT ON COLUMN public.detalle_venta.subtotal IS 'Subtotal calculado por el precio_venta de un producto * cantidad';
COMMENT ON COLUMN public.detalle_venta.cantidad IS 'cantidad de producto en la venta';


-- public.empleado_h definition

-- Drop table

-- DROP TABLE public.empleado_h;

CREATE TABLE public.empleado_h (
	id_peluqueria int4 NOT NULL, -- identificador unico de la peluqueria en donde trabaja el empleado
	rut_empleado int4 NOT NULL, -- identificador unico del empleado
	nombre_empleado varchar NOT NULL, -- nombre del empleado
	apellido_empleado varchar NOT NULL, -- apellido del empleado
	id_comuna int4 NOT NULL, -- identificador unico de la comuna donde reside el empleado
	fecha date NOT NULL,
	monto int4 NOT NULL,
	id_sueldo int4 NOT NULL,
	id_comuna_peluqueria int4 NOT NULL, -- Identificador de la comuna donde esta ubicada la peluqueria
	CONSTRAINT empleado_h_pk PRIMARY KEY (rut_empleado),
	CONSTRAINT comuna_pe_fk FOREIGN KEY (id_comuna_peluqueria) REFERENCES public.comuna_h(id_comuna),
	CONSTRAINT empleado_h_comuna_h_fk FOREIGN KEY (id_comuna) REFERENCES public.comuna_h(id_comuna),
	CONSTRAINT empleado_h_peluqueria_h_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria_h(id_peluqueria),
	CONSTRAINT empleado_h_sueldo_fk FOREIGN KEY (id_sueldo) REFERENCES public.sueldo(id_sueldo)
);
COMMENT ON TABLE public.empleado_h IS 'Tabla de dimensiones que almacena información de un empleado de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.empleado_h.id_peluqueria IS 'identificador unico de la peluqueria en donde trabaja el empleado';
COMMENT ON COLUMN public.empleado_h.rut_empleado IS 'identificador unico del empleado';
COMMENT ON COLUMN public.empleado_h.nombre_empleado IS 'nombre del empleado';
COMMENT ON COLUMN public.empleado_h.apellido_empleado IS 'apellido del empleado';
COMMENT ON COLUMN public.empleado_h.id_comuna IS 'identificador unico de la comuna donde reside el empleado';
COMMENT ON COLUMN public.empleado_h.id_comuna_peluqueria IS 'Identificador de la comuna donde esta ubicada la peluqueria';


-- public.ofrece definition

-- Drop table

-- DROP TABLE public.ofrece;

CREATE TABLE public.ofrece (
	id_ofrece int4 NOT NULL, -- identificador del servicio
	id_peluqueria int4 NOT NULL, -- identificador de la peluquería
	id_comuna int4 NULL, -- id de la comuna a la que pertenece la sede
	costo_servicio int4 NULL, -- costo del servicio ofrecido en cierta peluqueria
	id_servicio int4 NOT NULL, -- identificador del servicio
	CONSTRAINT servicios_p_pk PRIMARY KEY (id_ofrece),
	CONSTRAINT ofrece_comuna_p_fk FOREIGN KEY (id_comuna) REFERENCES public.comuna_p(id_comuna),
	CONSTRAINT ofrece_peluqueria_s_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria_s(id_peluqueria),
	CONSTRAINT ofrece_servicios_o_fk FOREIGN KEY (id_servicio) REFERENCES public.servicios_o(id_servicio)
);
COMMENT ON TABLE public.ofrece IS 'Tabla de hechos que almacena la conexion entre peluqueria y los servicios ofrecidos en la peluquería';

-- Column comments

COMMENT ON COLUMN public.ofrece.id_ofrece IS 'identificador del servicio';
COMMENT ON COLUMN public.ofrece.id_peluqueria IS 'identificador de la peluquería';
COMMENT ON COLUMN public.ofrece.id_comuna IS 'id de la comuna a la que pertenece la sede';
COMMENT ON COLUMN public.ofrece.costo_servicio IS 'costo del servicio ofrecido en cierta peluqueria';
COMMENT ON COLUMN public.ofrece.id_servicio IS 'identificador del servicio';