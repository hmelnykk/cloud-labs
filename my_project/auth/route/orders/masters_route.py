from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import masters_controller
from my_project.auth.domain.orders.masters import Masters

masters_bp = Blueprint('masters', __name__, url_prefix='/masters')

@masters_bp.get('')
def get_all_masters() -> Response:
    """
    Gets all masters from the database.
    :return: Response object
    """
    masters = masters_controller.find_all()
    return make_response(jsonify([master.put_into_dto() for master in masters]), HTTPStatus.OK)

@masters_bp.post('')
def create_master() -> Response:
    """
    Creates a new master in the database.
    :return: Response object
    """
    content = request.get_json()
    master = Masters.create_from_dto(content)
    masters_controller.create_master(master)
    return make_response(jsonify(master.put_into_dto()), HTTPStatus.CREATED)

@masters_bp.get('/<int:master_id>')
def get_master(master_id: int) -> Response:
    """
    Gets master by ID.
    :param master_id: Master ID
    :return: Response object
    """
    master = masters_controller.find_by_id(master_id)
    if master:
        return make_response(jsonify(master.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Master not found"}), HTTPStatus.NOT_FOUND)

@masters_bp.put('/<int:master_id>')
def update_master(master_id: int) -> Response:
    """
    Updates master by ID.
    :param master_id: Master ID
    :return: Response object
    """
    content = request.get_json()
    master = Masters.create_from_dto(content)
    masters_controller.update_master(master_id, master)
    return make_response("Master updated", HTTPStatus.OK)

@masters_bp.delete('/<int:master_id>')
def delete_master(master_id: int) -> Response:
    """
    Deletes master by ID.
    :param master_id: Master ID
    :return: Response object
    """
    masters_controller.delete_master(master_id)
    return make_response("Master deleted", HTTPStatus.NO_CONTENT)
