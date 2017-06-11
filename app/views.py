from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm, AdminPanel
from flask_login import login_user, logout_user, current_user, login_required
from models import *

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.before_request
def before_request():
  g.user = current_user
  g.role = None

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

@app.route('/admin/<string:role>', methods = ['GET', 'POST'])
@login_required
def admin(role):
  if not check_admin_role(role):
    flash('Wrong authorized role, Please check again!')
    return redirect(url_for('index'))
  user = g.user
  projects = search_author_project(user)
  form = AdminPanel()
  if form.validate_on_submit():
    project_name = request.form['project_name']
    project_chosed = Project.query.\
      filter_by(project_name = project_name).first()
    notes = db.session.query(Note, Project).\
      join(Project, Note.project_id == Project.id).\
      filter(Project.project_name == project_name)
    project_members = search_project_members(project_chosed)
    return render_template('admin.html',
      title = 'Release',
      projects = projects,
      results = notes,
      members = project_members,
      form = form)
  else:
    return render_template('admin.html',
      title = 'Release',
      projects = projects,
      results = None,
      members = None,
      form = form)

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

def check_admin_role(role):
  if not (role in ['root', 'admin', 'user']):
    return False
  user_role = g.user.role.role_name
  if role != user_role:
    return False
  return True

def search_project_members(project):
  if project is None:
    return None
  user_index = db.session.query(ProjectUserRole.user_id).\
    filter(ProjectUserRole.project_id == project.id)
  return db.session.query(User).\
    filter(User.id.in_([index.user_id for index in user_index]))
