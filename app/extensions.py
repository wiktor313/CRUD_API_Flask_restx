from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api()
db = SQLAlchemy()

'''flask shell
from app.models import *
db.create_all()
exit()
'''