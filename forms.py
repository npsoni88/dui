from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

class CreateContainer(FlaskForm):
    containername = StringField(label="Container Name")
    containerimage = StringField(label="Container Image")
    is_detached = BooleanField('Detached (-d)', default=True)
    is_interactive_tty = BooleanField('STD Input Open (-it)', default=True)
    submit = SubmitField('create')