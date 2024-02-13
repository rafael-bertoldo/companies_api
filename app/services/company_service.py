from app.models.company_model import Company
from sqlalchemy.exc import IntegrityError


class CompanyService:
    @staticmethod
    def create_company(data, db):
        try:
            verifyCompany = Company.query.filter_by(CNPJ=data["CNPJ"]).first()

            if verifyCompany:
                return {
                        "response": {
                        "message": "CNPJ já cadastrado"
                        },
                        "status_code": 409
                    }

            company = Company(**data)

            db.session.add(company)
            db.session.commit()

            print(company)

            return {
                "response": company,
                "status_code": 201
            }

        except IntegrityError:
            db.session.rollback()
            return {"message": "Verifique os dados e tente novamente"}

    @staticmethod
    def read_all_companies(start: int, limit: int, sort: str, dir: str):

        query = Company.query.order_by(getattr(Company, sort))

        if dir == "desc":
            query = Company.query.order_by(getattr(Company, sort).desc())

        companies = query.paginate(page=start, per_page=limit, error_out=False)

        baseUrl = "http://127.0.0.1:5000/api/companies"
        prev_start = f"{baseUrl}?start={start - 1}&limit={limit}"
        next_start = f"{baseUrl}?start={start + 1}&limit={limit}"

        total = (companies.total + limit - 1) // limit

        result = {
            "pagina_anterior": None if start <= 1 else prev_start,
            "proxima_pagina": None if start >= total else next_start,
            "data": [company.serialize() for company in companies.items],
        }

        return result

    @staticmethod
    def update_company(company_CNPJ: str, nome_fantasia: str, CNAE: str, db):
        try:
            company = Company.query.filter_by(CNPJ=company_CNPJ).first()

            if company is None:
                return False

            company.nome_fantasia = nome_fantasia
            company.CNAE = CNAE

            db.session.commit()

            return True
        except IntegrityError:
            db.session.rollback()
            return {"message": "Verifique os dados e tente novamente."}

    @staticmethod
    def delete_company(company_CNPJ: str, db):
        try:
            company = Company.query.filter_by(CNPJ=company_CNPJ).first()

            if company is None:
                return False

            db.session.delete(company)
            db.session.commit()

            return True
        except IntegrityError:
            db.session.rollback()
            return {"message": "Verifique os dados e tente novamente."}
