from app import db

class Note(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  version = db.Column(db.String(10), index = True, unique = True)
  author = db.Column(db.String(10), index = True, unique = False)
  note = db.Column(db.String(100))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def is_authenticated(self):
    return True

  def is_activate(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id)
    except NameError:
      return str(self.id)

  def __repr__(self):
    return '<Note %r>' % (self.version)

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(10), index = True, unique = True)
  email = db.Column(db.String(120), index = True, unique = True)

  def is_authenticated(self):
    return True

  def is_activate(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id)
    except NameError:
      return str(self.id)

  def __repr__(self):
    return '<User %r>' % (self.name)
