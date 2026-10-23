# Biblioteca Universitaria

## Descripción
Esta página web es sobre una biblioteca universitaria. Aquí se puede consultar información, libros disponibles, servicios y datos de contacto.

## Tecnologías
- **Python y Flask:** para crear las páginas y sus rutas.
- **HTML:** para organizar la información.
- **Jinja2:** para usar variables y compartir plantillas.
- **Bootstrap 4.6:** para el menú de navegación.

## Archivos
- **server.py:** contiene las rutas de las cuatro páginas.
- **layout.html:** tiene la estructura principal y el menú.
- **index.html:** muestra la información general y el horario.
- **catalogo.html:** muestra los materiales disponibles.
- **servicios.html:** explica los servicios de la biblioteca.
- **contacto.html:** contiene la dirección, el correo y el horario.

Se utilizaron variables como `titulo` y `mensaje`, la función `url_for()` y la herencia de plantillas con Jinja2.

## Cómo ejecutar
1. Instalar Flask con `pip install flask`.
2. Ejecutar `python server.py`.
3. Abrir `http://127.0.0.1:5000/` en el navegador.


