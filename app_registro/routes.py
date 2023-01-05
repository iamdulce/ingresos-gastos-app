from app_registro import app
from flask import render_template

@app.route("/")
def index():
	#diccionario de elementos a vista en html
	datos = [
		{
			'fecha': '18/12/2022',
			'concepto': 'Regalo de Reyes',
			'cantidad': -275.50
		},
		{
			'fecha': '19/12/2022',
			'concepto': 'Cobro de trabajo',
			'cantidad': 1200
		},
		{
			'fecha': '20/12/2022',
			'concepto': 'Ropa de Navidad',
			'cantidad': -150.50
		}
	]

	return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new")
def create():
	return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar")

@app.route("/update")
def edit():
	return render_template("update.html", pageTitle="Modificar", typeAction = "Modificación", buttonAction = "Editar")

@app.route("/delete")
def remove():
	return render_template("delete.html", pageTitle="Eliminar")


