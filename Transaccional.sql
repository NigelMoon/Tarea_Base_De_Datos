-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public IS 'standard public schema';
-- public.bloque definition

-- Drop table

-- DROP TABLE public.bloque;

CREATE TABLE public.bloque (
	id_bloque int4 NOT NULL, -- id del bloque (hora de inicio)
	CONSTRAINT bloque_pk PRIMARY KEY (id_bloque)
);
COMMENT ON TABLE public.bloque IS 'detalles de los bloques de una hora';

-- Column comments

COMMENT ON COLUMN public.bloque.id_bloque IS 'id del bloque (hora de inicio)';


-- public.comuna definition

-- Drop table

-- DROP TABLE public.comuna;

CREATE TABLE public.comuna (
	id_comuna int4 NOT NULL, -- id de la comuna
	nombre varchar NULL, -- nombre de la comuna
	CONSTRAINT comuna_pk PRIMARY KEY (id_comuna)
);
COMMENT ON TABLE public.comuna IS 'Tabla que almacena varias comunas';

-- Column comments

COMMENT ON COLUMN public.comuna.id_comuna IS 'id de la comuna';
COMMENT ON COLUMN public.comuna.nombre IS 'nombre de la comuna';


-- public.producto definition

-- Drop table

-- DROP TABLE public.producto;

CREATE TABLE public.producto (
	precio_compra int4 NULL, -- coste de comprar el producto a su respectivo proveedor
	nombre_producto varchar NULL, -- nombre del producto
	id_producto int4 NOT NULL, -- identificador del producto
	precio_venta int4 NULL, -- precio por el cual se vende el producto
	CONSTRAINT productos_pk PRIMARY KEY (id_producto)
);
COMMENT ON TABLE public.producto IS 'Datos sobre un producto tanto de uso interno de la peluquería como de venta';

-- Column comments

COMMENT ON COLUMN public.producto.precio_compra IS 'coste de comprar el producto a su respectivo proveedor';
COMMENT ON COLUMN public.producto.nombre_producto IS 'nombre del producto';
COMMENT ON COLUMN public.producto.id_producto IS 'identificador del producto';
COMMENT ON COLUMN public.producto.precio_venta IS 'precio por el cual se vende el producto';


-- public.servicios definition

-- Drop table

-- DROP TABLE public.servicios;

CREATE TABLE public.servicios (
	nombre_servicio varchar NULL, -- tipo del servicio
	id_servicio int4 NOT NULL, -- identificador del servicio
	costo_servicio int4 NULL, -- costo del servicio ofrecido en cierta peluqueria
	CONSTRAINT servicios_pk PRIMARY KEY (id_servicio)
);
COMMENT ON TABLE public.servicios IS 'Tabla que almacena los servicios ofrecidos por una peluquería';

-- Column comments

COMMENT ON COLUMN public.servicios.nombre_servicio IS 'tipo del servicio';
COMMENT ON COLUMN public.servicios.id_servicio IS 'identificador del servicio';
COMMENT ON COLUMN public.servicios.costo_servicio IS 'costo del servicio ofrecido en cierta peluqueria';


-- public.cliente definition

-- Drop table

-- DROP TABLE public.cliente;

CREATE TABLE public.cliente (
	sexo varchar NULL, -- Sexo del cliente
	nombre varchar NULL, -- nombre del cliente
	id_comuna int4 NULL, -- comuna a la que pertenece el cliente
	rut_cliente int4 NOT NULL, -- rut del cliente
	CONSTRAINT cliente_pk PRIMARY KEY (rut_cliente),
	CONSTRAINT cliente_comuna_fk FOREIGN KEY (id_comuna) REFERENCES public.comuna(id_comuna)
);
COMMENT ON TABLE public.cliente IS 'datos generales del cliente';

-- Column comments

COMMENT ON COLUMN public.cliente.sexo IS 'Sexo del cliente';
COMMENT ON COLUMN public.cliente.nombre IS 'nombre del cliente';
COMMENT ON COLUMN public.cliente.id_comuna IS 'comuna a la que pertenece el cliente';
COMMENT ON COLUMN public.cliente.rut_cliente IS 'rut del cliente';


-- public.peluqueria definition

-- Drop table

-- DROP TABLE public.peluqueria;

CREATE TABLE public.peluqueria (
	id_peluqueria int4 NOT NULL, -- identificador de la peluquería
	id_comuna int4 NULL, -- id de la comuna a la que pertenece la sede
	direccion varchar NULL, -- direccion de la peluqueria
	CONSTRAINT peluqueria_pk PRIMARY KEY (id_peluqueria),
	CONSTRAINT peluqueria_comuna_fk FOREIGN KEY (id_comuna) REFERENCES public.comuna(id_comuna)
);
COMMENT ON TABLE public.peluqueria IS 'Tabla de dimensión que almacena información de una peluqueria';

-- Column comments

COMMENT ON COLUMN public.peluqueria.id_peluqueria IS 'identificador de la peluquería';
COMMENT ON COLUMN public.peluqueria.id_comuna IS 'id de la comuna a la que pertenece la sede';
COMMENT ON COLUMN public.peluqueria.direccion IS 'direccion de la peluqueria';


-- public.transaccion_stock definition

-- Drop table

-- DROP TABLE public.transaccion_stock;

CREATE TABLE public.transaccion_stock (
	id_transaccion_stock int4 NOT NULL, -- Identificador de la transaccion
	cant_transaccion int4 NULL, -- Cantidad del producto involucrado en la transaccion
	fecha date NULL, -- Fecha en que ocurre la transacción/evento
	tipo_transaccion varchar NULL, -- Tipo de la transaccion del producto ("compra","venta", o "uso_servicio")
	id_producto int4 NOT NULL, -- Identificador asociado a producto
	CONSTRAINT transaccion_stock_pk PRIMARY KEY (id_transaccion_stock),
	CONSTRAINT transaccion_stock_producto_fk FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto)
);
COMMENT ON TABLE public.transaccion_stock IS 'Transacciones en donde el stock varía según evento (compra/venta de productos, venta de servicios)';

-- Column comments

COMMENT ON COLUMN public.transaccion_stock.id_transaccion_stock IS 'Identificador de la transaccion';
COMMENT ON COLUMN public.transaccion_stock.cant_transaccion IS 'Cantidad del producto involucrado en la transaccion';
COMMENT ON COLUMN public.transaccion_stock.fecha IS 'Fecha en que ocurre la transacción/evento';
COMMENT ON COLUMN public.transaccion_stock.tipo_transaccion IS 'Tipo de la transaccion del producto ("compra","venta", o "uso_servicio")';
COMMENT ON COLUMN public.transaccion_stock.id_producto IS 'Identificador asociado a producto';


-- public.usa_producto definition

-- Drop table

-- DROP TABLE public.usa_producto;

CREATE TABLE public.usa_producto (
	id_usa_producto int4 NOT NULL, -- Identificador usa producto
	id_producto int4 NULL, -- Identificador del producto usado
	id_servicio int4 NULL, -- Identificador del servicio
	fecha date NULL, -- Fecha en la que se uso el producto
	CONSTRAINT usa_producto_pk PRIMARY KEY (id_usa_producto),
	CONSTRAINT usa_producto_producto_fk FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto),
	CONSTRAINT usa_producto_servicios_fk FOREIGN KEY (id_servicio) REFERENCES public.servicios(id_servicio)
);
COMMENT ON TABLE public.usa_producto IS 'Tabla que almacena el uso de un producto en un servicio';

-- Column comments

COMMENT ON COLUMN public.usa_producto.id_usa_producto IS 'Identificador usa producto';
COMMENT ON COLUMN public.usa_producto.id_producto IS 'Identificador del producto usado';
COMMENT ON COLUMN public.usa_producto.id_servicio IS 'Identificador del servicio';
COMMENT ON COLUMN public.usa_producto.fecha IS 'Fecha en la que se uso el producto';


-- public.venta definition

-- Drop table

-- DROP TABLE public.venta;

CREATE TABLE public.venta (
	id_venta int4 NOT NULL, -- Identificador de la venta
	fecha date NULL, -- Fecha en que se realizó la venta
	total int4 NULL, -- Total vendido (calculado por los subtotales de detalle_venta)
	rut_cliente int4 NULL, -- RUT del cliente
	id_peluqueria int4 NULL, -- Identificador de peluqueria
	CONSTRAINT venta_pk PRIMARY KEY (id_venta),
	CONSTRAINT venta_cliente_fk FOREIGN KEY (rut_cliente) REFERENCES public.cliente(rut_cliente),
	CONSTRAINT venta_peluqueria_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria(id_peluqueria)
);
COMMENT ON TABLE public.venta IS 'Tabla que almacena el total de una venta de la peluqueria hacia un cliente';

-- Column comments

COMMENT ON COLUMN public.venta.id_venta IS 'Identificador de la venta';
COMMENT ON COLUMN public.venta.fecha IS 'Fecha en que se realizó la venta';
COMMENT ON COLUMN public.venta.total IS 'Total vendido (calculado por los subtotales de detalle_venta)';
COMMENT ON COLUMN public.venta.rut_cliente IS 'RUT del cliente';
COMMENT ON COLUMN public.venta.id_peluqueria IS 'Identificador de peluqueria';


-- public.compra definition

-- Drop table

-- DROP TABLE public.compra;

CREATE TABLE public.compra (
	id_compra int4 NOT NULL, -- Identificador de la compra
	fecha date NULL, -- Fecha en que ocurre la compra
	total int4 NULL, -- Monto total de la compra (calculado con la suma de los subtotales)
	id_peluqueria int4 NULL, -- Identificador de la peluqueria que realiza la compra
	CONSTRAINT compra_pk PRIMARY KEY (id_compra),
	CONSTRAINT compra_peluqueria_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria(id_peluqueria)
);
COMMENT ON TABLE public.compra IS 'Tabla que almacena el total de una compra de productos para la peluqueria';

-- Column comments

COMMENT ON COLUMN public.compra.id_compra IS 'Identificador de la compra';
COMMENT ON COLUMN public.compra.fecha IS 'Fecha en que ocurre la compra';
COMMENT ON COLUMN public.compra.total IS 'Monto total de la compra (calculado con la suma de los subtotales)';
COMMENT ON COLUMN public.compra.id_peluqueria IS 'Identificador de la peluqueria que realiza la compra';


-- public.detalle_compra definition

-- Drop table

-- DROP TABLE public.detalle_compra;

CREATE TABLE public.detalle_compra (
	id_detalle_compra int4 NOT NULL, -- identificador del detalle de la compra
	cantidad int4 NULL, -- Cantidad comprada de un mismo producto
	subtotal int4 NULL, -- Subtotal de la compra, calculado por precio_compra del producto * cantidad
	id_compra int4 NULL, -- Identificador de la compra en que está el detalle
	id_producto int4 NULL, -- Identificador del producto que se compró
	CONSTRAINT detalle_compra_pk PRIMARY KEY (id_detalle_compra),
	CONSTRAINT detalle_compra_compra_fk FOREIGN KEY (id_compra) REFERENCES public.compra(id_compra),
	CONSTRAINT detalle_compra_producto_fk FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto)
);
COMMENT ON TABLE public.detalle_compra IS 'Detalle de un producto en especifico dentro de una compra';

-- Column comments

COMMENT ON COLUMN public.detalle_compra.id_detalle_compra IS 'identificador del detalle de la compra';
COMMENT ON COLUMN public.detalle_compra.cantidad IS 'Cantidad comprada de un mismo producto';
COMMENT ON COLUMN public.detalle_compra.subtotal IS 'Subtotal de la compra, calculado por precio_compra del producto * cantidad';
COMMENT ON COLUMN public.detalle_compra.id_compra IS 'Identificador de la compra en que está el detalle';
COMMENT ON COLUMN public.detalle_compra.id_producto IS 'Identificador del producto que se compró';


-- public.detalle_venta definition

-- Drop table

-- DROP TABLE public.detalle_venta;

CREATE TABLE public.detalle_venta (
	id_detalle_venta int4 NOT NULL, -- Identificador del detalle de la venta
	subtotal int4 NULL, -- Subtotal calculado por el precio_venta de un producto * cantidad
	cantidad int4 NULL, -- Cantidad de productos vendida
	id_venta int4 NULL, -- Identificador de la venta a la que pertenece el detalle
	id_producto int4 NULL, -- Identificador del producto vendido
	CONSTRAINT detalle_venta_pk PRIMARY KEY (id_detalle_venta),
	CONSTRAINT detalle_venta_producto_fk FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto),
	CONSTRAINT detalle_venta_venta_fk FOREIGN KEY (id_venta) REFERENCES public.venta(id_venta)
);
COMMENT ON TABLE public.detalle_venta IS 'Detalle de la venta de un producto';

-- Column comments

COMMENT ON COLUMN public.detalle_venta.id_detalle_venta IS 'Identificador del detalle de la venta';
COMMENT ON COLUMN public.detalle_venta.subtotal IS 'Subtotal calculado por el precio_venta de un producto * cantidad';
COMMENT ON COLUMN public.detalle_venta.cantidad IS 'Cantidad de productos vendida';
COMMENT ON COLUMN public.detalle_venta.id_venta IS 'Identificador de la venta a la que pertenece el detalle';
COMMENT ON COLUMN public.detalle_venta.id_producto IS 'Identificador del producto vendido';


-- public.empleado definition

-- Drop table

-- DROP TABLE public.empleado;

CREATE TABLE public.empleado (
	rut_empleado int4 NOT NULL, -- RUT del empleado
	sueldo int4 NULL, -- sueldo del empleado
	nombre_empleado varchar NULL, -- nombre del empleado
	apellido_empleado varchar NULL, -- apellido del empleado
	id_peluqueria int4 NULL, -- peluqueria en la que trabaja el empleado
	id_comuna int4 NULL, -- comuna a la que pertenece el empleado
	CONSTRAINT empleado_pk PRIMARY KEY (rut_empleado),
	CONSTRAINT empleado_comuna_fk FOREIGN KEY (id_comuna) REFERENCES public.comuna(id_comuna),
	CONSTRAINT empleado_peluqueria_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria(id_peluqueria)
);

-- Column comments

COMMENT ON COLUMN public.empleado.rut_empleado IS 'RUT del empleado';
COMMENT ON COLUMN public.empleado.sueldo IS 'sueldo del empleado';
COMMENT ON COLUMN public.empleado.nombre_empleado IS 'nombre del empleado';
COMMENT ON COLUMN public.empleado.apellido_empleado IS 'apellido del empleado';
COMMENT ON COLUMN public.empleado.id_peluqueria IS 'peluqueria en la que trabaja el empleado';
COMMENT ON COLUMN public.empleado.id_comuna IS 'comuna a la que pertenece el empleado';


-- public.ofrece definition

-- Drop table

-- DROP TABLE public.ofrece;

CREATE TABLE public.ofrece (
	id_peluqueria int4 NULL, -- id de la peluqueria
	id_servicio int4 NULL, -- id del servicio
	id_ofrece int4 NOT NULL, -- id de la relación ofrece
	CONSTRAINT ofrece_pk PRIMARY KEY (id_ofrece),
	CONSTRAINT ofrece_peluqueria_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria(id_peluqueria),
	CONSTRAINT ofrece_servicios_fk FOREIGN KEY (id_servicio) REFERENCES public.servicios(id_servicio)
);
COMMENT ON TABLE public.ofrece IS 'Tabla que almacena los servicios -con sus respectivos precios- ofrecidos por una peluquería.';

-- Column comments

COMMENT ON COLUMN public.ofrece.id_peluqueria IS 'id de la peluqueria';
COMMENT ON COLUMN public.ofrece.id_servicio IS 'id del servicio';
COMMENT ON COLUMN public.ofrece.id_ofrece IS 'id de la relación ofrece';


-- public.sueldo definition

-- Drop table

-- DROP TABLE public.sueldo;

CREATE TABLE public.sueldo (
	id_sueldo int4 NOT NULL,
	fecha date NOT NULL,
	monto int4 NOT NULL,
	rut_empleado int4 NOT NULL,
	CONSTRAINT sueldo_pk PRIMARY KEY (id_sueldo),
	CONSTRAINT empleado_fk FOREIGN KEY (rut_empleado) REFERENCES public.empleado(rut_empleado)
);


-- public.cita definition

-- Drop table

-- DROP TABLE public.cita;

CREATE TABLE public.cita (
	fecha date NULL, -- fecha de la cita
	rut_empleado int4 NULL, -- RUT del empleado con el que se agendó la cita
	id_servicio int4 NULL, -- id del servicio ofrecido en la cita
	id_cita int4 NOT NULL, -- id de la cita
	id_peluqueria int4 NULL, -- id de la peluqueria donde ocurre la cita
	rut_cliente int4 NULL, -- rut del cliente que agendó la cita
	CONSTRAINT cita_pk PRIMARY KEY (id_cita),
	CONSTRAINT cita_cliente_fk FOREIGN KEY (rut_cliente) REFERENCES public.cliente(rut_cliente),
	CONSTRAINT cita_empleado_fk FOREIGN KEY (rut_empleado) REFERENCES public.empleado(rut_empleado),
	CONSTRAINT cita_peluqueria_fk FOREIGN KEY (id_peluqueria) REFERENCES public.peluqueria(id_peluqueria),
	CONSTRAINT cita_servicios_fk FOREIGN KEY (id_servicio) REFERENCES public.servicios(id_servicio)
);
COMMENT ON TABLE public.cita IS 'Tabla que almacena datos de una cita';

-- Column comments

COMMENT ON COLUMN public.cita.fecha IS 'fecha de la cita';
COMMENT ON COLUMN public.cita.rut_empleado IS 'RUT del empleado con el que se agendó la cita';
COMMENT ON COLUMN public.cita.id_servicio IS 'id del servicio ofrecido en la cita';
COMMENT ON COLUMN public.cita.id_cita IS 'id de la cita';
COMMENT ON COLUMN public.cita.id_peluqueria IS 'id de la peluqueria donde ocurre la cita';
COMMENT ON COLUMN public.cita.rut_cliente IS 'rut del cliente que agendó la cita';


-- public.ocurre definition

-- Drop table

-- DROP TABLE public.ocurre;

CREATE TABLE public.ocurre (
	id_cita int4 NULL, -- id de la cita
	id_bloque int4 NULL, -- id del bloque en donde ocurre la cita
	id_ocurre int4 NOT NULL, -- identificador de la relacion "ocurre"
	CONSTRAINT ocurre_pk PRIMARY KEY (id_ocurre),
	CONSTRAINT ocurre_bloque_fk FOREIGN KEY (id_bloque) REFERENCES public.bloque(id_bloque),
	CONSTRAINT ocurre_cita_fk FOREIGN KEY (id_cita) REFERENCES public.cita(id_cita)
);
COMMENT ON TABLE public.ocurre IS 'Tabla que almacena en que bloque ocurre una cita (una misma cita puede ocurrir en dos o más bloques seguidos)';

-- Column comments

COMMENT ON COLUMN public.ocurre.id_cita IS 'id de la cita';
COMMENT ON COLUMN public.ocurre.id_bloque IS 'id del bloque en donde ocurre la cita';
COMMENT ON COLUMN public.ocurre.id_ocurre IS 'identificador de la relacion "ocurre"';