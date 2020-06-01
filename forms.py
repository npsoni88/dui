from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

class CreateContainer(FlaskForm):
    containername = StringField(label="Container Name")
    containerimage = StringField(label="Container Image")
    is_interactive_tty = BooleanField('STD Input Open (-it)', default=True)
    submit = SubmitField('create')

class ManageContainers(FlaskForm):
    stop_container = SubmitField('Stop')
    remove_container = SubmitField('Delete')
    start_container = SubmitField('Start')