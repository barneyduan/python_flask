from datetime import datetime
from app import db
from flask.ext.login import UserMixin

class Note(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  version = db.Column(db.String(10), index = True, unique = True)
  author = db.Column(db.String(10), index = True, unique = False)
  note = db.Column(db.String(100))
  enable = db.Column(db.Boolean,  unique = False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  project_id = db.Column(db.Integer,  db.ForeignKey('project.id'))
  time = db.Column(db.DateTime, default = datetime.now())

  def __repr__(self):
    return '<Note %r>' % (self.version)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(10), index = True, unique = True)
  email = db.Column(db.String(120), index = True, unique = True)
  account = db.Column(db.String(100), index = True, unique = True)
  passwrd = db.Column(db.String(100), index = True)
  authority = db.Column(db.Integer)

  def __repr__(self):
    return '<User %r>' % (self.name)

class Project(db.Model):
    id = db.Column(db.Integer,  primary_key = True)
    project_name = db.Column(db.String(100),  unique = True)
    last_version = db.Column(db.String(20),  unique = True)
    version_count = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Project %r>' %(self.project_name)
