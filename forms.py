from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="Ingresa nombre valido")
    ])
    apaterno=StringField('aPaterno',[
        validators.DataRequired(message="El campo es requerido"),

    ])
    email=EmailField('Correo',[
        validators.email(message="Ingrese un correo valido"),

    ])