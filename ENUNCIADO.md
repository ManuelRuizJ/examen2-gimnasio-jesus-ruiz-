# Segundo examen parcial: el proyecto del becario

**Tópicos Avanzados de Cómputo (LIIS1217)** · Duración: 2 horas · Individual

## La situación

El Gimnasio Titán quiere dejar de llevar sus clases en hojas de cálculo. Kevin, el becario que empezó el sistema, terminó su servicio la semana pasada y lo dejó a medias. Dijo que "ya casi estaba".

Tú lo heredas. Tu trabajo es dejarlo funcionando, documentar lo que encontraste y, si te da tiempo, avanzar con lo que falta.

El proyecto usa Django, Django REST Framework y SQLite. Todo lo necesario lo vimos en el bloque de Django.

**Cómo funciona el gimnasio:** hay disciplinas (Yoga, Spinning, Crossfit, Pilates, Box), socios con una membresía que vence en cierta fecha y clases. Cada clase tiene disciplina, instructor, día, hora, sala, cupo, estado (activa o cancelada) y socios inscritos.

## Guía de tiempo sugerida

| Tiempo | Actividad |
|---|---|
| 0:00 a 0:15 | Clonar, crear tu repositorio y preparar el entorno |
| 0:15 a 1:00 | Parte 1 |
| 1:00 a 1:50 | Parte 2 |
| 1:50 a 2:00 | Revisar bitácora, último push y entrega en Moodle |

Si terminas las Partes 1 y 2 antes de tiempo, sigue con la Parte 3.

No te quedes atorado en una falla más de 15 minutos: anota en la bitácora lo que llevas y sigue con la siguiente.

## Antes de empezar

1. Crea en tu GitHub un repositorio **vacío** (sin README) llamado `examen2-gimnasio-<tu-nombre>`.
2. Clona el repositorio del profesor y apúntalo al tuyo:

```
# Terminal
git clone <URL que da el profesor> examen2
cd examen2
git remote set-url origin <URL de tu repositorio vacío>
git push -u origin main
```

3. Crea el entorno virtual e instala dependencias:

```
# Terminal (macOS / Linux)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```
# Terminal (Windows)
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Consejo: antes de tocar código, revisa el historial con `git log --stat`. Los commits de Kevin dicen mucho de lo que pasó.

## Parte 1. Hacer que arranque (24 puntos)

Objetivo: que estos tres comandos terminen sin errores, en este orden.

```
# Terminal
python manage.py migrate
python manage.py cargar_datos
python manage.py runserver
```

Hay **tres** problemas en este camino. Por lo general, al corregir uno aparece el siguiente. Lee el error completo, de abajo hacia arriba, y corrige la causa en el archivo correcto.

Si un error menciona una columna que no existe, revisa con `git log --stat` qué cambió Kevin en los modelos y qué archivos le faltaron a ese commit.

Sabrás que terminaste cuando `cargar_datos` diga "Carga terminada", el sitio abra en `http://127.0.0.1:8000/` (aunque esa página todavía falle, eso es el Ticket 1) y el admin muestre 40 socios y 20 clases. Para entrar al admin crea un superusuario con `python manage.py createsuperuser`.

## Parte 2. Tickets de recepción (40 puntos)

Con el sistema arriba, recepción reportó lo siguiente. Los tickets describen lo que ve el usuario; la causa la encuentras tú. Un cambio que solo esconde el error (borrar la línea que truena, comentar código) no cuenta como corrección.

**Ticket 1.** "Al abrir la página principal (`http://127.0.0.1:8000/`) aparece una pantalla amarilla de error."

**Ticket 2.** "La página principal dice que hay 20 clases con lugares disponibles, y no puede ser: Spinning del lunes a las 7:00 (SPN-01) está llena, 20 de 20, y Box del viernes (BOX-03) se canceló. Las dos salen en `?con_lugar=1`." Una clase tiene lugar si está activa **y** tiene menos inscritos que su cupo. Con los datos de recepción deben ser 16.

**Ticket 3.** "En el buscador (`/clases/buscar/`) escribo 'yoga' y salen 39 resultados. Solo tenemos 4 clases de yoga."

**Ticket 4.** "La app de recepción intenta crear una clase nueva por la API y el servidor responde error 500." La app envía esto, y la respuesta debe ser 201:

```
POST /api/clases/
{
  "codigo": "YOG-05",
  "disciplina": "Yoga",
  "instructor": "Rocío Estrada",
  "dia": "sab",
  "hora": "10:00",
  "cupo": 15,
  "sala": "Sala Zen"
}
```

Pruébalo desde la página de la API en el navegador (`http://127.0.0.1:8000/api/clases/`, formulario de abajo, pestaña "Raw data") o con Thunder Client.

## Parte 3. Lo que Kevin no alcanzó a hacer (16 puntos)

Solo después de las partes 1 y 2. Respeta exactamente rutas y nombres, porque la app de recepción ya los usa.

**F1. Inscribir a un socio (10 pts).** `POST /api/clases/{id}/inscribir/` con el cuerpo `{"socio": "GYM-007"}` inscribe al socio y responde 200 con la clase actualizada. Debe responder 400 con un mensaje claro, sin inscribir a nadie, si:

- la clase está cancelada,
- la clase ya está llena,
- el socio ya estaba inscrito en esa clase,
- la membresía del socio está vencida (su `vence_membresia` es anterior a hoy).

**F2. Filtros de clases (6 pts).** `GET /api/clases/` acepta los parámetros opcionales `disciplina` (nombre, sin distinguir mayúsculas) y `con_lugar=true`. Se pueden combinar: `/api/clases/?disciplina=yoga&con_lugar=true`. Pista: lo que corregiste en el Ticket 2 te sirve aquí.

**Extra (+5 pts).** `GET /api/reportes/mas-demandadas/` responde las 5 clases con más inscritos, de mayor a menor (en empate, por código), con este formato:

```
[
  {"codigo": "SPN-01", "disciplina": "Spinning", "inscritos": 20, "cupo": 20, "ocupacion": 100},
  ...
]
```

`ocupacion` es el porcentaje redondeado a entero.

## Bitácora y commits (20 puntos)

Llena `BITACORA.md` conforme avanzas, no al final. Por cada falla registra:

- **Síntoma:** qué viste, con el mensaje de error.
- **Causa:** por qué pasaba.
- **Corrección:** qué cambiaste y en qué archivo.
- **Verificación:** cómo comprobaste que quedó.

Haz **un commit por cada corrección** con un mensaje que diga qué arreglaste, por ejemplo `fix: el buscador repetía clases`. Haz `git push` varias veces durante el examen, no solo al final.

**Uso de IA.** Se recomienda resolver el examen sin asistentes de IA. Si los usas, decláralo en la sección final de la bitácora: qué le pediste, qué usaste de la respuesta y qué verificaste tú. Un uso no declarado se trata como plagio.

## Entrega

1. Último `git push` a tu repositorio.
2. En Moodle sube `BITACORA.md` y escribe la URL de tu repositorio. Si es privado, agrega al profesor como colaborador.

Lo que no esté en tu repositorio a la hora de cierre no se califica.

## Puntuación

| Parte | Puntos |
|---|---|
| Parte 1. Arranque (3 fallas) | 24 |
| Parte 2. Tickets (4) | 40 |
| Parte 3. F1 y F2 | 16 |
| Bitácora, commits y declaración de IA | 20 |
| **Total** | **100** |
| Extra: reporte | +5 |

Una corrección sin su explicación en la bitácora vale la mitad. Un cambio que solo esconde el error (borrar la línea que truena, comentar código) no cuenta como corrección.
