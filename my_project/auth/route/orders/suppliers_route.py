from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import suppliers_controller
from my_project.auth.domain.orders.suppliers import Suppliers

suppliers_bp = Blueprint('suppliers', __name__, url_prefix='/suppliers')

@suppliers_bp.get('')
def get_all_suppliers() -> Response:
    """
    Gets all suppliers from the database.
    :return: Response object
    """
    suppliers = suppliers_controller.find_all()
    return make_response(jsonify([supplier.put_into_dto() for supplier in suppliers]), HTTPStatus.OK)

@suppliers_bp.post('')
def create_supplier() -> Response:
    """
    Creates a new supplier in the database.
    :return: Response object
    """
    content = request.get_json()
    supplier = Suppliers.create_from_dto(content)
    suppliers_controller.create_supplier(supplier)
    return make_response(jsonify(supplier.put_into_dto()), HTTPStatus.CREATED)

@suppliers_bp.get('/<int:supplier_id>')
def get_supplier(supplier_id: int) -> Response:
    """
    Gets supplier by ID.
    :param supplier_id: Supplier ID
    :return: Response object
    """
    supplier = suppliers_controller.find_by_id(supplier_id)
    if supplier:
        return make_response(jsonify(supplier.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Supplier not found"}), HTTPStatus.NOT_FOUND)

@suppliers_bp.put('/<int:supplier_id>')
def update_supplier(supplier_id: int) -> Response:
    """
    Updates supplier by ID.
    :param supplier_id: Supplier ID
    :return: Response object
    """
    content = request.get_json()
    supplier = Suppliers.create_from_dto(content)
    suppliers_controller.update_supplier(supplier_id, supplier)
    return make_response("Supplier updated", HTTPStatus.OK)

@suppliers_bp.delete('/<int:supplier_id>')
def delete_supplier(supplier_id: int) -> Response:
    """
    Deletes supplier by ID.
    :param supplier_id: Supplier ID
    :return: Response object
    """
    suppliers_controller.delete_supplier(supplier_id)
    return make_response("Supplier deleted", HTTPStatus.NO_CONTENT)
