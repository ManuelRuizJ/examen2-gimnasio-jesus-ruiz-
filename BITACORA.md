# Bitácora del examen

**Nombre: Jesus Manuel Ruiz Fuentes**
**Repositorio: https://github.com/ManuelRuizJ/examen2-gimnasio-jesus-ruiz-**

Copia el bloque de abajo una vez por cada falla que encuentres. Llénalo en el momento, no al final.

---

## Falla 1 (Parte 1 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
No estaba isntalada gimansio en settigns.py, se importo y se soluciono el primero progrlema de mirgrate, se relaizo la migracion, y se corrigio el codigo de cargar_datos, se cmabio la funcion de create() a get_or_create() para las que ya estaban creadas

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
lo explique en sintoma perdon por la mala orfanizacion

**Corrección:** qué cambiaste y en qué archivo(s).


**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).


**Commit:** el mensaje del commit de esta corrección.
corrreccion en el comando de cargar datos, antes solo lo creaba sin importar si ya existia, por eso se cambio a get_or_create
ManuelRuizJ
ManuelRuizJ
committed
1 hour ago
migracion correcta
ManuelRuizJ
ManuelRuizJ
committed
1 hour ago
fix: instalar app en settings.py
ManuelRuizJ
ManuelRuizJ
committed
1 hour ago
---

---

## Falla N (Ticket 1 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al correr aparecia un error

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
estaba incorrecto el url de refencia a url.py, estaba como detalle_clase y era clase_detalle

**Corrección:** qué cambiaste y en qué archivo(s).
se cambio el orden

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

## Falla N (Ticket 2 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al buscar clases con solo espacio, mandaba todos, aunque estuvieran llenas o canceladas

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
un _lte en ves de un _lt y falta dee estado ACTIVA

**Corrección:** qué cambiaste y en qué archivo(s).
se cambio models.py en el .filter()

**Verificación:** cómo comprobaste que quedó (comando, URL, consulta en el shell, prueba).

**Commit:** el mensaje del commit de esta corrección.


---

---

## Falla N (Ticket 3 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al correr aparecia un error

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
estaba incorrecto el url de refencia a url.py, estaba como detalle_clase y era clase_detalle

**Corrección:** qué cambiaste y en qué archivo(s).
se cambio el orden

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

no me dio tiempo de acpmpletar la bitacora, acompletare el examen en otroa rama, perdon y gracias jeje

---

## Falla N (Ticket 4 )

**Síntoma:** qué viste. Pega la última línea del error o describe el comportamiento.
al correr aparecia un error

**Causa raíz:** por qué pasaba. Explícalo como se lo explicarías a Kevin.
estaba incorrecto el url de refencia a url.py, estaba como detalle_clase y era clase_detalle

**Corrección:** qué cambiaste y en qué archivo(s).
se cambio el orden

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

## Declaración de uso de IA

Marca una opción.

- [ ] No usé asistentes de IA en este examen.
- [ ] Sí usé asistentes de IA. Para cada uso: herramienta, qué le pedí, qué usé de su respuesta y qué revisé o cambié yo.
