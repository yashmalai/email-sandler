from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.bp_reg import bp_register


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bp_register(app)
    return app