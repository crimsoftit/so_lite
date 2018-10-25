from app import db
from models import User

# insert data
db.session.add(User("manu", "sindani254@gmail.com", "Soen@30010010"))
db.session.add(User("admin", "ad@min.com", "admin"))

# commit the changes
db.session.commit()
