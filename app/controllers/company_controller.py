from flask import jsonify, current_app, request
from app.services.company_service import CompanyService
from app.middlewares.verify_update_keys import verify_update_keys


class CompanyController:
    @staticmethod
    def create_company():
        data = request.get_json()
        db = current_app.db
        service = CompanyService()
        company = service.create_company(data, db)

        return jsonify(company["response"]), company["status_code"]

    @staticmethod
    def read_all_companies():
        start = request.args.get("start", default=1, type=int)
        limit = request.args.get("limit", default=5, type=int)
        sort = request.args.get("sort", default="id", type=str)
        dir = request.args.get("dir", default="asc", type=str)
        service = CompanyService()

        companies = service.read_all_companies(start, limit, sort, dir)

        return jsonify(companies), 200

    @staticmethod
    def update_company(company_CNPJ):
        data = request.get_json()
        db = current_app.db

        verify_keys = verify_update_keys(data)

        if not verify_keys:
            return (
                jsonify(
                    {
                        "message": "Apenas as chave 'nome_fantasia' e 'CNAE' podem ser atualizadas."
                    }
                ),
                400,
            )

        company_service = CompanyService()
        updated = company_service.update_company(
            company_CNPJ, data["nome_fantasia"], data["CNAE"], db
        )

        if updated:
            return jsonify({"message": "Dados atualizados com sucesso."}), 200
        else:
            return (
                jsonify({"message": "CNPJ não encontrado, por favor tente novamente."}),
                404,
            )

    @staticmethod
    def delete_company(company_CNPJ):
        db = current_app.db
        service = CompanyService()

        deleted = service.delete_company(company_CNPJ, db)

        if deleted:
            return jsonify(), 204
        else:
            return (
                jsonify({"message": "CNPJ não encontrado, por favor tente novamente."}),
                404,
            )
