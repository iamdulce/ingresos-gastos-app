from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import datetime
from config import *
import os #modilo para renombrar y eliminar archivos

@app.route("/")
def index():
    #Se remplaza el diccionario datos por archivos csv
    fichero = open(MOVIMIENTOS_FILE, "r") 
    #Llama al archivo en modo lectura
    lectura = csv.reader(fichero, delimiter=",", quotechar="'") 
    #preparo cada registro del archivo y le da nuevo formato csv

    datos = []

    for item in lectura:
        datos.append(item) 
        #Recorre el obj csvReader y carga cada registro en el array vacío pra nostrarlos en pantalla
    
    fichero.close()
    return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new",methods=["POST", "GET"])
def create():
    if request.method == "GET":
        return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar", dataForm = {})
    else:
        error = validateForm(request.form)

        if error:
            return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar", msjError = error, dataForm = request.form)
        else:
            mi_fichero = open(MOVIMIENTOS_FILE, "a", newline="") 
            #Llamo al archivo preparado para crear un nuevo registro
            escritura = csv.writer(mi_fichero, delimiter=",", quotechar="'") 
            #preparo el formato csv a que tendrá un nuevo registro

            #---->Para identificar y crear id(#). Consulto el archivo donde se guardan los últimos registros
            fichero_r = open(LAST_ID_FILE, "r") 
            registro = fichero_r.read()
            if registro == "":
                new_id = 1
            else:
                new_id = int(registro)+1
            fichero_r.close()

            fichero_w = open(LAST_ID_FILE, "w")
            fichero_w.write(str(new_id))
            fichero_w.close

            escritura.writerow([new_id, request.form['date'], request.form['concept'], request.form['quantity']])
            #Uso el metodo writerow de write para escribir el registro

        mi_fichero.close()

    return redirect("/")

@app.route("/update/<int:id>")
def edit(id):
    #return f"{id} a editar"
    return render_template("update.html", pageTitle="Modificar", typeAction = "Modificación", buttonAction = "Editar", dataForm = {})

@app.route("/delete/<int:id>",methods= ["GET", "POST"])
def remove(id):
    #return f"{id} a borrar"
     
    if request.method == "GET":
        mi_fichero = open(MOVIMIENTOS_FILE, "r")
        lectura = csv.reader(mi_fichero, delimiter=",", quotechar="'") 
        registro_buscado = []

        for registro in lectura:
            if registro[0] == str(id):
                registro_buscado = registro
        mi_fichero.close()
        #?????

        if len(registro_buscado) > 0:
            return render_template("delete.html", pageTitle="Eliminar", registro= registro_buscado)
        else: 
            return redirect("/")

    else: 
        fichero_old = open(MOVIMIENTOS_FILE, "r")
        #Llamo al archivo de registros
        fichero_new = open(MOVIMIENTOS_FILE_NEW, "w", newline="")
        #Llamo a un archivo nuevo (recién creado)

        lectura = csv.reader(fichero_old, delimiter=",", quotechar="'") 
        escritura = csv.writer(fichero_new, delimiter=",", quotechar="'")

        for registro in lectura:
            if registro[0] != str(id):
                escritura.writerow(registro)
                #????

        fichero_old.close()
        fichero_new.close()

        os.remove(MOVIMIENTOS_FILE)
        os.rename(MOVIMIENTOS_FILE_NEW, MOVIMIENTOS_FILE)

        return redirect("/")


def validateForm(requestForm):
    hoy = datetime.today().isoformat()
    #Se pasa a string
    errores = []
    if requestForm['date'] > hoy:
        errores.append("Fecha invalida: Introduce una fecha anterior a la actual")
    if requestForm['concept'] == "":
        errores.append("Concepto vacío: Introduce un concepto al registro")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) == 0.0:
        errores.append('Cantidad vacía o cero: Introduce una cantidad positiva o negativa')
    return errores


'''
OTRA FORMA DE HACERLO si importo date en lugar de datetime (sin función de validación de errores)
hoy = datetime.now()
fecha_ingresada = datetime.strptime(request.form['date'], "%Y-%m-%d").date() 
#doy formato a la fecha ingresada
if fecha_ingresada <= hoy.date():
    print("fecha correcta",hoy.date())
     escritura.writerow([request.form['date'], request.form['concept'], request.form['quantity']]) 
    #registro los datos recibidos desde el request.form y agrego con el metodo writerow
else:
    return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar")
'''