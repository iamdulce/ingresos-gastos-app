# App Web Ingresos-Gastos

Programa hecho en python con el framework Flask. App de registro de ingresos y gastos

## Instalación

- En el entorno de python, ejecutar el comando

```
pip install -r requirements.txt
```

La libreria utilizada: flask https://flask.palletsprojects.com/en/2.2.x/

## Ejecución del programa

Para inicializar el servidor:

- Windows: `set FLASK_APP=main.py`
- Mac: `export FLASK_APP=main.py`

Otra alternativa sería crear el archivo oculto .env y dentro agregar las siguientes lineas:

`FLASK_APP = main.py`
`FLASK_DEBUG = true`

## Comando para ejecutar el servidor

```
flask --app main run
```

## Comando para ejecutar el servidor en otro puerto

```
flask --app main -p run 5001
```

## Actualizar el servidor con cambios en tiempo real

```
flask --app main --debug run
```

## Actualizar el servidor con cambios en tiempo real y en otro puerto

```
flask --app main --debug run p 5001
```
