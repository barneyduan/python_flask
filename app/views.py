from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User, Note

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.before_request
def before_request():
  g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
  user = g.user
  return render_template("index.html",
    title =  'Home',
    user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if g.user is not None and g.user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    account = request.form.get('account')
    passwrd = request.form.get('passwrd')
    user = User.query.filter_by(account = account, passwrd = passwrd).first()
    if user is None:
      flash('Invalid Login, Please try again')
      return redirect(url_for('login'))
    g.user = user
    login_user(user)
    flash('Logged in successfully')
    next = request.form.get('next')
    return redirect(next or url_for('index')) 
  return render_template('login.html',
    title='Sign In',
    form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/userpage')
@login_required
def userpage():
  return
