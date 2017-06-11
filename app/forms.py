from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
  account = StringField('account', validators = [DataRequired()])
  passwrd = StringField('passwrd', validators = [DataRequired()])

class AdminPanel(Form):
	project_name = SubmitField('project_name')
