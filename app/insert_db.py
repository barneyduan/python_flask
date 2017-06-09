#insert db data script
from app import db, models
import time
'''
p = models.Project(id = 1, project_name = 'Roller', last_version = '0.0.6', version_count = 6)
db.session.add(p)
p2 = models.Project(id = 2, project_name = 'F6000')
db.session.add(p2)

n1 = models.Note(id = 1, version = '0.0.1', author = 'barney', note = 'This is to test1', project_id = 1, enable = True)
db.session.add(n1)
db.session.commit()
time.sleep(5)

n2 = models.Note(id = 2, version = '0.0.2', author = 'barney', note = 'This is to test2', project_id = 1, enable = True)
db.session.add(n2)
db.session.commit()
time.sleep(5)

n3 = models.Note(id = 3, version = '0.0.3', author = 'barney', note = 'This is to test3', project_id = 1, enable = True)
db.session.add(n3)
db.session.commit()
time.sleep(5)

n4 = models.Note(id = 4, version = '0.0.4', author = 'barney', note = 'This is to test4', project_id = 1, enable = True)
db.session.add(n4)
db.session.commit()
time.sleep(5)

n5 = models.Note(id = 5, version = '0.0.5', author = 'barney', note = 'This is to test5', project_id = 1, enable = True)
db.session.add(n5)
db.session.commit()
time.sleep(5)

n6 = models.Note(id = 6, version = '0.0.6', author = 'barney', note = 'This is to test6', project_id = 1, enable = True)
db.session.add(n6)
db.session.commit()


x1 = models.Authority(id = 1, author_name = 'release')
db.session.add(x1)
x2 = models.Authority(id = 2, author_name = 'cancel')
db.session.add(x2)
db.session.commit()

u1 = models.User(id = 1, name = 'barney', email = 'duanlian@163.com', account = 'debug', passwrd = '123456', role_id = 1)
db.session.add(u1)
u2 = models.User(id = 2, name = 'victor', email = 'victor@123.com', account = 'debug1', passwrd = '123456', role_id = 2)
db.session.add(u2)
db.session.commit()

r1 = models.Role(id = 1, role_name = 'root')
db.session.add(r1)
r2 = models.Role(id = 2, role_name = 'admin')
db.session.add(r2)
db.session.commit()
'''

ra1 = models.role_authority(role_id = 1, author_id = 1)
ra2 = models.role_authority(role_id = 1, author_id = 2)
db.session.add(ra1)
db.session.add(ra2)
db.session.commit()

pur1 = models.ProjectUserRole(id = 1, project_id = 1, user_id = 1, role_id = 1)
db.session.add(pur1)
pur2 = models.ProjectUserRole(id = 2, project_id = 1, user_id = 2, role_id = 2)
db.session.add(pur2)
pur3 = models.ProjectUserRole(id = 3, project_id = 2, user_id = 1, role_id = 1)
db.session.add(pur3)
db.session.commit()

