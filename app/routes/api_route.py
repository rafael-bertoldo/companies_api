from flask import Blueprint
from . import company_route

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(company_route.bp)