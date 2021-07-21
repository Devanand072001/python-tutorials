from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, IntegerField
# from flask.ext.wtf.html5 import NumberInput
from flask_bootstrap import Bootstrap
# import phonenumbers
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class SignupForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(
        min=5, max=32, message="username must be atleast 5 characters long")])
    email = StringField(label="Email", validators=[
        DataRequired(), Email(message="enter valid email")])
    # date_of_birth = DateField('Date of birth', format="%dd/%mm%yyyy")
    password = PasswordField("Password", validators=[DataRequired(), Length(
        max=32, message="password must be 8 characters long")])
    confirm_password = PasswordField(label="Confirm passoword", validators=[
        DataRequired(), EqualTo('password', message="password mismatch")])

    gender = SelectField(
        'Gender',
        choices=[('male', 'Male'), ('female', 'Female'),
                 ('donot wish specify', 'Donot wish specify')], validators=[DataRequired()]
    )
    grade = SelectField(label="Grade", choices=[('VI', "VI"), ('VII', "VII"), ("VIII", "VIII"), "IX,IX", ("X", "X")],
                        validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])

    remember_me = BooleanField(label="Remember me")
    submit = SubmitField(label="Submit")

    # def validate_phone(self, phone):
    #     try:
    #         p = phonenumbers.parse(phone.data)
    #         if not phonenumbers.is_valid_number(p):
    #             raise ValueError()
    #     except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
    #         raise ValidationError('Invalid phone number')
