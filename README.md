## Introducción
Una empresa que se dedica al transporte de containers desea desarrollar una aplicación que le permita gestionar su negocio. La empresa cuenta con una flota de barcos y camiones que le permiten transportar los mencionados containers entre distintos paises donde la empresa posee sedes.

## Requerimientos del sistema
Como se mencionó en la sección anterior, el objetivo de la empresa es obtener una aplicación que le permita gestionar el traslado de containers alrededor del mundo.
La empresa cuenta con una flota de barcos de distintas características, que le permiten transportar distintos tipos de containers. Por ejemplo, posee barcos que sólo pueden transportar containers básicos, mientras que otros barcos mas especializados permiten transportar containers de mayor tamaño, con contenido especial, etc.

### Barcos
La empresa posee dentro de su flota de barcos, 2 tipos de barcos. Por un lado posee barcos que sólo pueden transportar containers de tipo básico y barcos que pueden transportar cualquier tipo de container. Cada barco posee un identificador único, también define la cantidad maxima de containers que puede transportar y el peso máximo que soporta.
Todos los barcos poseen una estructura especializada que permite organizar, asegurar y transportar los contenedores. En el caso de los barcos de tipo básico, dicha estructura sólo está diseñada para soportar contenedores cuyas dimensiones coincidan con las de un contenedor de tipo básico; mientras que en el caso de los barcos especializados dicha estructura permite transportar cualquier tipo de contenedor cuyas medidas sean superiores a las de un contenedor básico.

### Camiones
La mayoría de los clientes de la empresa, retiran la mercadería por el puerto, una vez que el container es descargado del barco que lo transporta. Para aquellos clientes que no poseen transporte propio, la empresa ofrece el servicio de entrega en puerta, por lo que la empresa cuenta con una flota de 5 camiones. Este servicio tiene un costo fijo de $20000 por viaje realizado.
> Un camión sólo puede transportar 1 container a la vez. 

### Contenedores
En general un contenedor tiene un identificador único, mediante el cual la empresa consigue mantener la trazabilidad del mismo. A su vez, la empresa destina ciertos containers para el transporte de materiales especiales como puede ser explosivos, desechos químicos o radioactivos.
Cada contenedor define un precio base que se debe pagar para transportar una determinada carga en el mismo, a esto debe sumarse el precio que se debe pagar por la carga en sí misma. Ver el apartado de precios más adelante.

#### Básico
El contenedor Básico estándar también conocido como contenedor de 20 pies, es el contenedor más usados a nivel mundial en el transporte marítimo de mercancías. El contenedor estándar se diferencia de otros modelos de contenedor principalmente en que está cerrado herméticamente y no cuenta con sistemas de refrigeración o ventilación, como es el caso de los contenedores refrigerados o ventilados. 

#### Básico HC (High Cube)
El contenedor Básico HC, también conocido como contenedor de 40 pies, es idéntico al contenedor básico pero con mayores dimensiones, volumen y kilos soportados.


#### Flat Rack
Los contenedores flat rack están diseñados para dar cabida a todas aquellas cargas cuyas medidas, distribución de los bultos o peso no permiten su transporte en contenedores estándar Los flat rack están hechos de planchas de metal que se ajustan a una estructura estándar de 20 o 40 pies. Los laterales son abatibles y no disponen de techo o parte superior. Esto los hace adecuados para el transporte de: 
>Mercancías muy pesadas que deben ser cargadas en el contenedor con grúas o equipamientos especializados. Un ejemplo típico de mercancías transportadas en flat rack son las de la industria de la maquinaria.

>Mercancías con una altura superior a la de un contenedor de 20 o 40 pies High Cube o con volúmenes muy irregulares, como vehículos industriales o tuberías.

                
-----
### Reglas de Negocio

1. Un barco no puede cargar más containers del máximo definido 
2. Un barco no puede cargar más peso del máximo definido 
3. Un barco no puede cargar un container para el cual no fue diseñado. 
4. Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser transportado por un barco diseñado para tal fin. 
5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo. 
6. Un contenedor sin características especiales no puede transportar material 

----
# 2da ETAPA

### ACTUALIZACION Barcos 
En esta nueva etapa, la empresa decide que es tiempo de comenzar a registrar el consumo de combustible
de sus barcos. Se estima que el consumo de combustible de cualquier barco es aproximadamente 6L por
hora. La cantidad de combustible que un barco puede cargar, depende de cada barco.

Con el objetivo de mejorar el consumo de combustible de los barcos, la empresa está comenzando a
probar, en algunos barcos, un sistema de velas inteligentes que permiten ahorrar hasta un 100% del
combustible durante el tiempo que estén en uso.

Se desea poder conocer en todo momento:
- con qué tipo de dispositivo se encuentra trabajando el barco, vela o motor.
- el combustible restante.

### ACTUALIZACION Contenedores 
Con el objetivo de seguir expandiendo el negocio de transporte de mercaderías, la empresa incorpora a
sus servicios el transporte de mercaderías que requieren tratamiento especial como por ejemplo los
alimentos. Para ello incorpora un tipo de container con ventilación.

El contenedor ventilado es un tipo de contenedor que dispone de un sistema de ventilación gracias a unas
aberturas laterales que permiten la circulación del aire. Su sistema de ventilación permite por un lado la
expulsión del aire caliente del interior y por otro la entrada de aire fresco del exterior, asegurando así que
no se produce condensación de gases o humedad que puedan afectar a la carga. Esta característica lo
convierte en el tipo de contenedor más adecuado para el transporte de mercancías que necesitan mantener
una temperatura constante y sin cambios abruptos. Uno de los principales productos transportados en este
tipo de contenedor es el café, por eso también se conoce al contenedor ventilado como contenedor del
café.

Las dimensiones de este tipo de contenedor son iguales a las de un contenedor básico.

Por último se incorpora un nuevo tipo de container denominado "Open Top" que es similar a un
contenedor de tipo "Flat rack" pero permite agregar un cobertor a la carga. El tipo de mercancías que se
transporta en este tipo de contenedor es esencialmente el mismo que en un contenedor flat rack, pero con
medidas más regulares en los laterales. Es decir, es apropiado para cargas que son demasiado pesadas y
necesitan ser levantadas con grúas o que son demasiado altas y no caben en un contenedor de HC. A
diferencia del flat rack, que tampoco tiene techo, el contenedor open top sí tiene paredes laterales y
además se puede cubrir la parte superior con una lona para que las mercancías viajen más protegidas.
Este tipo de contendor agrega al precio un adicional fijo ya que es poco probable que el contenedor
vuelva a ser utilizado en el viaje de vuelta.

### NUEVO Modulo contable
La aplicación debe contar con un módulo cuya función principal es obtenger el resultado económico de
un determinado barco. El resultado económico de un barco se puede calcular como el beneficio obtenido
a partir de los containers transportados menos los gastos de combustible reportados.

### ACTUALIZACION Modulo GPS
El modulo de GPS en esta etapa permitirá calcular distancia y tiempo promedio que demora una
embarcación en recorrer el trayecto entre 2 sedes.

### NUEVO Cargas

Con más experiencia en la industria del transporte de cargas, la empresa comienza a clasificar mejor los
tipos de cargas que carga en sus containers. A partir de este momento, la empresa puede identificar cargas
de tipo alimenticia, químicas (pinturas, combustibles, desechos), maquinarias. Esta distinción permite
establecer nuevas reglas de negocio, como por ejemplo:

- Las cargas alimenticias deben viajar en containers de tipo ventilado .
- Las cargas alimenticias no pueden viajar junto a cargas de tipo químicas.
- Fin

