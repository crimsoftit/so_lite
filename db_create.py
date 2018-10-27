from project import db
from project.models import BlogPost, User

# create the database and the db tables
db.create_all()

# insert data
db.session.add(BlogPost('mercy', 'ni mamayo'))
db.session.add(BlogPost('madhe', 'sisemi kitu'))

db.session.add(User("manu", "sindani254@gmail.com", "Soen@30010010"))
db.session.add(User("admin", "ad@min.com", "admin"))


# commit the changes
db.session.commit()
