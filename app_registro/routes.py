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
            mi_fichero = open("data/movimientos.csv", "a", newline="") 
            #Llamo al archivo preparado para crear un nuevo registro
            escritura = csv.writer(mi_fichero, delimiter=",", quotechar="'") 
            #preparo el formato csv a que tendrá un nuevo registro

            #---->Para identificar y crear id(#). Consulto el archivo donde se guardan los últimos registros
            fichero_r = open("data/last_id.csv", "r") 
            registro = fichero_r.read()
            if registro == "":
                new_id = 1
            else:
                new_id = int(registro)+1
            fichero_r.close()

            fichero_w = open("data/last_id.csv", "w")
            fichero_w.write(str(new_id))
            fichero_w.close

            escritura.writerow([new_id, request.form['date'], request.form['concept'], request.form['quantity']])
            #Uso el metodo writerow de write para escribir el registro

        mi_fichero.close()

    return redirect("/")

@app.route("/update/<int:id>")
def edit(id):
    return f"{id} a editar"
    #return render_template("update.html", pageTitle="Modificar", typeAction = "Modificación", buttonAction = "Editar")

@app.route("/delete/<int:id>")
def remove(id):
    return f"{id} a borrar"
    #return render_template("delete.html", pageTitle="Eliminar")


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