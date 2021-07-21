from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

from  wtforms.validators import DataRequired

class FormName(FlaskForm):
    name = StringField(validators=[DataRequired()])
    submit = SubmitField()
