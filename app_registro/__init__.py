from flask import Flask

app = Flask(__name__) #Inicializo el servidor y ejecuto desde el archivo main

from app_registro.routes import * #Referencia a todas las rutas creadas