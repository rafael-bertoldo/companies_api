from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.company_model import Company

    Migrate(app, app.db)