from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from models import *

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.before_request
def before_request():
  g.user = current_user
  g.role = Role.query.filter(Role.id == g.user.role_id)

@lm.unauthorized_handler
def handle_needs_login():
  flash('You need to be logged')
  return redirect(url_for('login', next = request.path))

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
    return  redirect_back('index')
  return render_template('login.html',
    title = 'Sign In',
    form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@app.route('/index')
@login_required
def index():
  user = g.user
  projects = search_author_project(user)
  return render_template('index.html',
    title = 'Release',
    projects = projects)

@app.route('/project/<string:name>')
@login_required
def project(name):
  user = g.user
  projects = search_author_project(user)
  notes = db.session.query(Note, Project).\
    join(Project, Note.project_id == Project.id).\
    filter(Project.project_name == name)
  return render_template('project.html',
    title = 'Release',
    projects = projects,
    results = notes,
    user = user)


def redirect_back(home):
  next = request.args.get('next')
  if not next:
    next = url_for(home)
  return redirect(next)

def search_author_project(user):
	if user is None:
		return None
	if user.role_id == 1:
		return Project.query.all()
	else:
		projects_index = db.session.query(ProjectUserRole.project_id).\
		  filter(ProjectUserRole.user_id == user.id)
		return db.session.query(Project).\
		  filter(Project.id.in_([index.project_id for index in projects_index]))