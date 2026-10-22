# Bitácora del examen

**Nombre: Jesus Manuel Ruiz Fuentes**
**Repositorio: https://github.com/ManuelRuizJ/examen2-gimnasio-jesus-ruiz-**

Copia el bloque de abajo una vez por cada falla que encuentres. Llénalo en el momento, no al final.

---

## Falla 1, 2 y 3 (Parte 1 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
No estaba isntalada gimansio en settigns.py, se importo y se soluciono el primero progrlema de mirgrate, se relaizo la migracion, y se corrigio el codigo de cargar_datos, se cmabio la funcion de create() a get_or_create() para las que ya estaban creadas

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
lo explique en sintoma perdon por la mala orfanizacion

**Corrección:** qué cambiaste y en qué archivo(s).
se agrego gimansio a installled_aps en settings.py
Se hixo las migtraciones para actulizar la db
se cambio el create() por get_or_create() en el comnado de cargar_datos para evitar errores cuadno una disciplina ya existe

**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).
Se hicieorn las migraciones con ➜  examen2 git:(bitacora-completa) ✗ python manage.py makemigrations gimnasio y se verifico que en cada paso iniciara sin errores


**Commit:** el mensaje del commit de esta corrección.
fix: instalar app en settings.py

migracion correcta

Corrección en el comando de carga de datos para utilizar get_or_create().


---

## Falla 4 (Ticket 1 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al abrir la pagina principal aparecia un error relacionado con el nombre de una url

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
estaba incorrecto el url de refencia a url.py, estaba como detalle_clase y era clase_detalle

**Corrección:** qué cambiaste y en qué archivo(s).
se cambio el orden de detalle_clase a clase_detalle

**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).
se cargo correctamente el inicio
(venv) ➜  examen2 git:(main) ✗ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 22, 2026 - 12:57:28
Django version 6.1.2, using settings 'config.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/
[22/Oct/2026 12:57:34] "GET / HTTP/1.1" 200 5483


**Commit:** el mensaje del commit de esta corrección.
correcion al nombre de urll de detalle_clase a clase_detalle

---


---

## Falla 5 (Ticket 2 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al buscar clases con espacio disponible, mandaba todos, aunque estuvieran llenas o canceladas

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
un _lte en ves de un _lt y faltaba el filtro de clases que son de estado ACTIVA

**Corrección:** qué cambiaste y en qué archivo(s).
se cambio models.py en el .filter() en el metodo con_lugar()

**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).
se revido en la pagina y se uso el filtor en ?con_ligar=1, y ahora si filtraba exitosamente las clases que estaban con estado activo y que aun tenian cupo

**Commit:** el mensaje del commit de esta corrección.
correcion lugar minimo, se usaba _lte en el filter, al parecer solo era porque sobreba una e (_lt es el correcto), ademas se agrego el esatado, para que no aparezcan las que tengan un estado Cancelada


---

## Falla 6 (Ticket 3 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al buscar la clase yoga en el bucador aparecian 39 resultados, eunque solo se esperaban 4 (clases)

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
La consulte bussca en los nombres de quienes estan incritos, esto traia a todas las veces que estaban incritos sin importar si esa clase ya la habia traido

**Corrección:** qué cambiaste y en qué archivo(s).
se agrego la funcion .distinct() a la funcion clase_buscar para evitar que se repitan

**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).
ahora al filtrar por ?q=yoga se filtra correctamente las clases sin repetirse

**Commit:** el mensaje del commit de esta corrección.
se agrego la funcion .distinct() en la funcion clase_buscar, que srive para eliminar filas duplicadas en una cosnulta


---

## Falla 7 (Ticket 4 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
Al probar el POST en /api/clases habia un problema

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
el serializer de clase nececitaba definir como converti el campo de disciplina , para ello se uso un SlugRelatedField que utiliza el campo nombre y hace la cosnulta, ademas que el capo inscritos solo se usa como solo lecutra

**Corrección:** qué cambiaste y en qué archivo(s).
En gimnasio/serializers.py, se modifico ClaseSerializer para configurar los campos disciplina e inscritos

**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).
se creo una nueva clase y dio un 201 de created


[22/Oct/2026 14:17:08] "POST /api/clases/ HTTP/1.1" 201 16710



**Commit:** el mensaje del commit de esta corrección.
correcion al nombre de urll de detalle_clase a clase_detalle

---

## Declaración de uso de IA

Marca una opción.

- [ ] No usé asistentes de IA en este examen.
- [ ] Sí usé asistentes de IA. Para cada uso: herramienta, qué le pedí, qué usé de su respuesta y qué revisé o cambié yo.
