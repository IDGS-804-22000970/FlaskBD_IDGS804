from . import maestros
from flask import render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from maestros.routes import maestros, maestros
from models import db
from models import Alumnos, Maestros


@maestros.route("/maestros",methods=['GET','POST'])
@maestros.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form,maestros=maestros)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"