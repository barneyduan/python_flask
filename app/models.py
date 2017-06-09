from datetime import datetime
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True, unique = True)
  name = db.Column(db.String(20), index = True, unique = True)
  email = db.Column(db.String(64), index = True, unique = True)
  account = db.Column(db.String(64), index = True, unique = True)
  passwrd = db.Column(db.String(64), index = True)
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

  def __repr__(self):
    return '<User %r>' % (self.name)

role_authority = db.Table('RoleAuthority',
  db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
  db.Column('author_id', db.Integer, db.ForeignKey('authority.id'))
)

class Role(db.Model):
  id = db.Column(db.Integer, primary_key = True, unique = True)
  role_name = db.Column(db.String(20))
  users = db.relationship('User', backref = 'role')
  authority = db.relationship('Authority', secondary = role_authority,
    back_populates = 'roles')

  def __repr__(self):
    return '<Role %r>' % (self.role_name)

class Authority(db.Model):
  id = db.Column(db.Integer, primary_key = True, unique = True)
  author_name = db.Column(db.Integer, index = True, unique = True)
  roles = db.relationship('Role', secondary = role_authority,
    back_populates = 'authority')

  def __repr__(self):
    return '<Authority %r>' % (self.author_name)

class Project(db.Model):
    id = db.Column(db.Integer,  primary_key = True, unique = True)
    project_name = db.Column(db.String(64),  unique = True)
    last_version = db.Column(db.String(20),  unique = True)
    version_count = db.Column(db.Integer)
    notes = db.relationship('Note', backref = 'project')
    
    def __repr__(self):
        return '<Project %r>' %(self.project_name)

# each package version item in one project
class Note(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  version = db.Column(db.String(10), index = True, unique = True)
  author = db.Column(db.String(10), index = True, unique = False)
  note = db.Column(db.String(100))
  enable = db.Column(db.Boolean,  unique = False)
  project_id = db.Column(db.Integer,  db.ForeignKey('project.id'))
  time = db.Column(db.DateTime, default = datetime.now())

  def __repr__(self):
    return '<Note %r>' % (self.version)

#class RoleAuthority(db.Column):
  #id = db.Column(db.Integer, primary_key = True, unique = True)
  #role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
  #author_id = db.Column(db.Integer, db.ForeignKey('authority.id'))

class ProjectUserRole(db.Model):
  id = db.Column(db.Integer, primary_key = True, unique = True)
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'))





