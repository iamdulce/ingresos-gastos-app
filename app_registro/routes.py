from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import datetime

@app.route("/")
def index():
    #Se remplaza el diccionario datos por archivos csv
    fichero = open("data/movimientos.csv", "r") 
    #Llama al archivo en modo lectura
    lectura = csv.reader(fichero, delimiter=",", quotechar="'") 
    #accede a cada registro del archivo y le da nuevo formato csv

    datos = []

    for item in lectura:
        datos.append(item) 
        #Recorre el obj csvReader y carga cada registro en el array vacío

    return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new",methods=["POST", "GET"])
def create():
    if request.method == "GET":
        return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar", dataForm = {})
    else:
        fichero = open("data/movimientos.csv", "a", newline="") 
        #Llamo al archivo preparado para crear un nuevo registro
        escritura = csv.writer(fichero, delimiter=",", quotechar="'") 
        #Uso el método writer y le doy formato csv a los registros
        
        error = validateForm(request.form)

        if error:
            return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar", msjError = error, dataForm = request.form)
        else:
            escritura.writerow([request.form['date'], request.form['concept'], request.form['quantity']])

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
            print("fecha incorrecta")
            return render_template("new.html", pageTitle="Alta", typeAction = "Alta", buttonAction = "Guardar")
        '''

        fichero.close()

    return redirect("/")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Modificar", typeAction = "Modificación", buttonAction = "Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Eliminar")


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
