from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
  account = StringField('account', validators = [DataRequired()])
  passwrd = StringField('passwrd', validators = [DataRequired()])
