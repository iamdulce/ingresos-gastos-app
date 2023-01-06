from app_registro import app
from flask import render_template
import csv

@app.route("/")
def index():
	#Se remplaza el diccionario datos por archivos csv
	fichero = open("data/movimientos.txt", "r") #Llama al archivo
	csvReader = csv.reader(fichero, delimiter=",", quotechar="'") #accede a cada registro del archivo y le da nuevo formato

	datos = []

	for item in csvReader:
		datos.append(item) #recorre el obj csvReader y carga cada registro en el array vacío

	return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new",methods=["POST", "GET"])
def create():
	return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar")

@app.route("/update")
def edit():
	return render_template("update.html", pageTitle="Modificar", typeAction = "Modificación", buttonAction = "Editar")

@app.route("/delete")
def remove():
	return render_template("delete.html", pageTitle="Eliminar")


