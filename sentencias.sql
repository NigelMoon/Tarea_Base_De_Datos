-- a) horario con más citas durante el día por peluquería, identificando la comuna 

-- no muestra la cantidad de citas
create temp table bloques as
select generate_series(1, 10) as num;

with concurrencias as (
    select
        num as bloque,
        c.id_peluqueria as peluqueria,
        co.nombre as comuna,
        row_number() over (partition by c.id_peluqueria, co.nombre order by COUNT(*) desc) as rn
    from bloques
    join cita c on num between c.id_bloque_inicio AND c.id_bloque_fin
    join comuna co on co.id_comuna = c.id_comuna_peluqueria
    group by num, c.id_peluqueria, co.nombre
)
select bloque, peluqueria, comuna
from concurrencias
where rn = 1
order by peluqueria desc;

-- muestra la cantidad de citas
CREATE TEMP TABLE bloques AS
SELECT generate_series(1, 10) AS num;

WITH concurrencias AS (
    SELECT
        num AS bloque,
        COUNT(*) AS concurrencia,
        c.id_peluqueria AS peluqueria,
        co.nombre AS comuna,
        ROW_NUMBER() OVER (PARTITION BY c.id_peluqueria, co.nombre ORDER BY COUNT(*) DESC) AS rn
    from bloques
    join cita c ON num BETWEEN c.id_bloque_inicio AND c.id_bloque_fin
    join comuna co ON co.id_comuna = c.id_comuna_peluqueria
    group by num, c.id_peluqueria, co.nombre
)
select bloque, concurrencia, peluqueria, comuna
from concurrencias
where rn = 1
order by peluqueria DESC;


-- b)lista de clientes que gastan más dinero por peluquería, indicando comuna del cliente y de peluquería, además de cuanto gasto
select distinct on(peluqueria)
    c.rut_cliente AS cliente,
    c.id_peluqueria AS peluqueria,
    comuna_cliente.nombre AS comuna_cliente,
    comuna_peluqueria.nombre AS comuna_peluqueria,
    sum(coalesce(c.costo_servicio, 0) + coalesce(dv.total, 0)) AS gasto_total
from cita c
inner join comuna comuna_cliente ON c.id_comuna_cliente = comuna_cliente.id_comuna
inner join comuna comuna_peluqueria ON c.id_comuna_peluqueria = comuna_peluqueria.id_comuna
left join detalle_venta dv ON c.rut_cliente = dv.rut_cliente AND c.id_peluqueria = dv.id_peluqueria
group by c.rut_cliente, c.id_peluqueria, comuna_cliente.nombre, comuna_peluqueria.nombre
order by peluqueria, gasto_total DESC;
--(ojo : si se cambia de desc a asc, muestra el que ha gastado menos dinero por peluqueria )

-- c) lista de peluqueros que ha ganado más por mes durante el 2023, esto por peluquería 
select rut_empleado as empleado, max(monto) as monto, extract(month from fecha) as mes, id_peluqueria as peluqueria
from empleado_h e
where extract(year from fecha) = 2023
group by empleado, mes, peluqueria
order by peluqueria asc;


-- d) lista de clientes hombres que se cortan el pelo y la barba  Grande nick
with Barberia as (
	select id_cita, rut_cliente, s.nombre_servicio as servicio
	from cita c
	inner join servicios s on s.id_servicio = c.id_servicio
	where sexo = 'M' and (s.nombre_servicio like '%barberia%' or s.nombre_servicio like '%barba%')
),
Cabello as (
	select	id_cita, rut_cliente, s.nombre_servicio as servicio
	from cita c
	inner join servicios s on s.id_servicio = c.id_servicio
	where sexo = 'M' and s.nombre_servicio like '%cabello%' 
)
select ci.rut_cliente as cliente
from cita ci
inner join Barberia b on b.id_cita = ci.id_cita 
inner join Cabello c on c.id_cita = ci.id_cita 
where b.id_cita = c.id_cita;


-- e) lista de clientes que tiñen el pelo, indicando la comuna del cliente, la peluquería donde se atendió y el valor que pagó 
select c.rut_cliente as cliente, s.nombre_servicio, c.id_comuna_cliente as comuna, c.id_peluqueria as peluqueria, c.costo_servicio as total
from cita c
inner join servicios s on s.id_servicio = c.id_servicio
where s.nombre_servicio like '%coloracion%';


-- f) identificar el horario más concurrido por peluquería durante el 2019 y 2020, desagregados por mes 
create temp table bloques as
select generate_series(1, 10) as num;


with concurrencias as (
    select
        num as bloque,
        COUNT(*) as concurrencia,
        c.id_peluqueria as peluqueria,
        extract(month from c.fecha) as mes,
        row_number() OVER (PARTITION BY c.id_peluqueria, extract(month from c.fecha) order by COUNT(*) DESC) as rn
    from bloques
    join cita c on num between c.id_bloque_inicio and c.id_bloque_fin
    where extract(year from c.fecha) between 2019 and 2020
    group by num, c.id_peluqueria, extract(month from c.fecha)
)
select bloque,concurrencia,peluqueria,mes
from concurrencias
where rn = 1
order by peluqueria desc, mes asc;


-- g) identificar al cliente que ha tenido las citas más largas por peluquería, por mes
select  tiempo_h as horas_cita, cliente, mes, peluqueria
from (
    select 
        (id_bloque_fin - id_bloque_inicio + 1) as tiempo_h, 
        extract(month from fecha) as mes, 
        rut_cliente as cliente, 
        id_peluqueria as peluqueria,
        row_number() over (partition by extract(month from fecha), id_peluqueria order by (id_bloque_fin - id_bloque_inicio + 1) desc, rut_cliente) as rn
    from cita c
) t
where rn = 1
order by peluqueria ASC, mes DESC;


-- h) identificar servicio más caro por peluquería
select c.nombre_servicio as servicio, MAX(s.costo_servicio) AS costo_maximo, s.id_peluqueria AS peluqueria 
from ofrece s
join (
    select MAX(costo_servicio) AS max_costo, id_peluqueria
    from ofrece
    group by id_peluqueria
) maximos
on s.id_peluqueria = maximos.id_peluqueria AND s.costo_servicio = maximos.max_costo
join servicios_o c ON c.id_servicio = s.id_servicio
group by s.id_peluqueria, servicio
order by s.id_peluqueria desc;



-- i) identificar al peluquero que ha trabajado más por mes durante el 2019
select distinct on (t.mes) t.empleado, t.cantidad_citas as citas, t.mes
from (select e.rut_empleado as empleado, extract(month from c.fecha) as mes, count(c.id_cita) as cantidad_citas
from empleado e
inner join cita c on c.rut_empleado = e.rut_empleado
where extract(year from c.fecha) = 2019 
group by empleado, mes) t 
order by t.mes, t.cantidad_citas desc;

-- j) identificar lista clientes de totales por comuna, cantidad de peluquerías, cantidad de clientes residentes en la comuna

select
    c.nombre as comuna,
    COUNT(distinct a.id_peluqueria) AS cantidad_peluquerias,
    COUNT(distinct a.rut_cliente) AS cantidad_clientes,
    STRING_AGG(distinct a.rut_cliente::text, ', ') as lista_clientes
from comuna c
inner join cita a on a.id_comuna_peluqueria = c.id_comuna
group by c.nombre
order by c.nombre asc;
