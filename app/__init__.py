from flask import Flask
from app.configs import database, migration
from app.routes import api_route
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():

    app = Flask(__name__)

    SWAGGER_URL = "/api/docs"
    API_URL = "/static/swagger.json"

    database.init_app(app)
    migration.init_app(app)
    app.register_blueprint(api_route.bp)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Companies API"}
    )
    app.register_blueprint(swaggerui_blueprint)

    return app
