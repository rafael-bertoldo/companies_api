from flask import Blueprint
from app.controllers.company_controller import CompanyController


bp = Blueprint("companies_bp", __name__, url_prefix="/companies")

bp.post("")(CompanyController.create_company)
bp.get("")(CompanyController.read_all_companies)
bp.patch("/<company_CNPJ>")(CompanyController.update_company)
bp.delete("/<company_CNPJ>")(CompanyController.delete_company)
