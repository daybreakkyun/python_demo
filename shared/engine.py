from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_restx import Api

db = SQLAlchemy()
app = Flask(__name__)
ma = Marshmallow(app)
api = Api()


def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://xrpltools:xrpltools@localhost:3306/demo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api.init_app(app)
    return app