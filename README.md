# Sistema de Cotizaciones - Capital & Farmer

## Instalación
1. Clone el repositorio
2. pip install fastapi uvicorn
3. pip install localStoragePy
4. pip install fastapi uvicorn sqlalchemy
5. pip install jinja2
6. pip install python-multipart
7. python.exe -m pip install --upgrade pip (opcional)
8. uvicorn main:app --reload (para inicilizar app)

## Uso
- Acceder a http://127.0.0.1:8000/
- Completar formulario de cotización :  Nombre de cliente
                                        Correo electronico
                                        Tipo de servicio
                                        Descripción del Caso
- Se creó una funcion que ejecuta el formulario principal
- Se creó el api submit el cual enviará la data del formulario a guardar en la bd
    - dentro de submit se implementó codigo para validar, calcular y concatenar numero de cotización
    - dentro de submit se implementó codigo para calcular el precio del servicio de acuerdo al servicio seleccionado
    - dentro de submit se imeplementó codigo para obtener la fecha actual que finalmente será la fecha de creación
- Se creó api cotizaciones de tipo get, la cual devolverá una lista con las cotizaciones guardadas

## APIs utilizadas
- Get
http://127.0.0.1:8000/cotizaciones

-Post
http://127.0.0.1:8000/submit

form-data

nombre = text
correo = text
servicio = text
descripcion = text

## Funcionalidades bonus
- [Listar lo que implementaste extra]
