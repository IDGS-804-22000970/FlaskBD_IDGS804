from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)
db.init_app(app)



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404



@app.route("/",methods=['GET','POST'])
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():

    if request.method == "POST":
        nombre = request.form.get("nombre")
        apaterno = request.form.get("apaterno")
        email = request.form.get("email")

        nuevo_alumno = Alumnos(
            nombre=nombre,
            apaterno=apaterno,
            email=email
        )

        db.session.add(nuevo_alumno)
        db.session.commit()

        flash("Alumno guardado correctamente")
        return redirect(url_for("alumnos"))

    lista_alumnos = Alumnos.query.all()
    return render_template("Alumnos.html", alumnos=lista_alumnos)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # crea la tabla si no existe

    app.run(debug=True)
