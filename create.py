from application import db
from application.models import Prayers

db.drop_all()
db.create_all()
