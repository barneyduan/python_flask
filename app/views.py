from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname':'Miguel'}
  return render_template("index.html",
      title =  'Home',
      user = user)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated():
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    session['remember_me'] = form.remember_me.data
    return oid.try_login(form.openid.data, ask_for=['name', 'email'])
  return render_template('login.html',
    title='Sign In',
    form=form,
    providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        name = resp.name
        if name is None or name == "":
            name = resp.email.split('@')[0]
        user = User(name=name, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))
