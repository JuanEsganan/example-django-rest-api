Ejemplo en español de Django rest API.

Con este proyecto básico, pretendo demostrar las habilidades para configurar y empezar un proyecto básico usando Django REST API, en el primer commit (2b6f179b9bb10c2fa6ba5b2d026b89494de12e27), se encontrará la configuración inicial, donde se crea el proyecto y:

- se empieza la app llamada "tareas"
- se crean migraciones iniciales
- se instala django rest framework
- se instala django-corsheaders (modulo adicional para conectar backend con frontend), se debe agregar a la lista de apps del proyecto y también a la lista de Middlewares

Crear API:

Del modelo que vayamos a utilizar o base de datos, debemos seleccionar los datos que van a ser enviados desde el back-end para que puedan ser convertidos a .JSON, esto se hace desde el archivo "serializer.py" y se debe crear la clase.
Luego hay que configurar las "views.py" con la creación de una clase que defina los datos que se desean "serializar(convertir)" con los datos a mostrar de la DB y ya se puede empezar con las tareas cotidianas de un CRUD.
En el "urls.ps" se guardan las rutas que el frontend va a consultar.   
