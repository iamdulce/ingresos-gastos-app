from app_registro import app
from flask import render_template

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/new")
def create():
	return render_template("new_register.html")
