from flask_restful import Resource
from flask import jsonify, request

from app.models import Customer, Invoice
from app.schemas import CustomerSchema, InvoiceSchema


class CustomerResource(Resource):
    def get(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        schema = CustomerSchema()
        return jsonify(schema.dump(customer))

    def delete(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return '', 204
