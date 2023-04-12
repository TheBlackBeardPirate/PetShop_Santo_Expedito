from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)

from .views import cliente_view, animal_view
from .models import cliente_model, animal_model
