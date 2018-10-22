from app import db
from models import BlogPost

# create the database and the db tables
db.create_all()

# insert data
db.session.add(BlogPost('mercy', 'ni mamayo'))
db.session.add(BlogPost('madhe', 'sisemi kitu'))

# commit the changes
db.session.commit()
