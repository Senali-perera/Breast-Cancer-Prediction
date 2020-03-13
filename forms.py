from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BookingForm(FlaskForm):
    patientname = StringField('Patient name', validators=[DataRequired()])
    NIC = StringField('NIC', validators=[DataRequired()])
    Phonenum = IntegerField('Phone number', validators=[DataRequired()])
    submit = SubmitField('Submit')


