from models import Maestros
from . import maestros
from flask import Flask, render_template, request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from maestros.routes import maestros, maestros
from models import db
from models import Alumnos, Maestros


@maestros.route("/maestros", methods=['GET','POST'])
@maestros.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMaes.html",form=create_form,maestros=maestros)
    


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

# CREAR
@maestros.route("/maestros/crear", methods=['GET', 'POST'])
def crear():
    form = forms.MaestroForm(request.form)

    if request.method == 'POST' and form.validate():
        maestro = Maestros(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/crear.html", form=form)


# DETALLES
@maestros.route("/maestros/detalles/<int:matricula>")
def detalles(matricula):
    maestro = Maestros.query.get_or_404(matricula)

    return render_template("maestros/detalles.html",
                           matricula=maestro.matricula,
                           nombre=maestro.nombre,
                           apellidos=maestro.apellidos,
                           especialidad=maestro.especialidad,
                           email=maestro.email)


# EDITAR
@maestros.route("/maestros/editar/<int:matricula>", methods=['GET', 'POST'])
def editar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    form = forms.MaestroForm(request.form, obj=maestro)

    if request.method == 'POST' and form.validate():
        maestro.matricula = form.matricula.data
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data

        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/editar.html", form=form)


# ELIMINAR
@maestros.route("/maestros/eliminar/<int:matricula>", methods=['GET', 'POST'])
def eliminar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    form = forms.MaestroForm(request.form, obj=maestro)

    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/eliminar.html", form=form)