#insert db data script
from app import db, models

p = models.Project(id = 1, project_name = 'Roller', last_version = '0.0.6', version_count = 6)
db.session.add(p)
p2 = models.Project(id = 2, project_name = 'F6000')
db.session.add(p2)

u1 = models.Note(id = 1, version = '0.0.1', author = 'barney', note = 'This is to test1', user_id = 1, project_id = 1, enable = True)
db.session.add(u1)

u2 = models.Note(id = 2, version = '0.0.2', author = 'barney', note = 'This is to test2', user_id = 1, project_id = 1, enable = True)
db.session.add(u2)

u3 = models.Note(id = 3, version = '0.0.3', author = 'barney', note = 'This is to test3', user_id = 1, project_id = 1, enable = True)
db.session.add(u3)

u4 = models.Note(id = 4, version = '0.0.4', author = 'barney', note = 'This is to test4', user_id = 1, project_id = 1, enable = True)
db.session.add(u4)

u5 = models.Note(id = 5, version = '0.0.5', author = 'barney', note = 'This is to test5', user_id = 1, project_id = 1, enable = True)
db.session.add(u5)

u6 = models.Note(id = 6, version = '0.0.6', author = 'barney', note = 'This is to test6', user_id = 1, project_id = 1, enable = True)
db.session.add(u6)
db.session.commit()
