from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import repairment_controller
from my_project.auth.domain.orders.repairment import Repairment

repairment_bp = Blueprint('repairments', __name__, url_prefix='/repairments')

@repairment_bp.get('')
def get_all_repairments() -> Response:
    """
    Gets all repairments from the database.
    :return: Response object
    """
    repairments = repairment_controller.find_all()
    return make_response(jsonify([repairment.put_into_dto() for repairment in repairments]), HTTPStatus.OK)

@repairment_bp.post('')
def create_repairment() -> Response:
    """
    Creates a new repairment in the database.
    :return: Response object
    """
    content = request.get_json()
    repairment = Repairment.create_from_dto(content)
    repairment_controller.create_repairment(repairment)
    return make_response(jsonify(repairment.put_into_dto()), HTTPStatus.CREATED)

@repairment_bp.get('/<int:repairment_id>')
def get_repairment(repairment_id: int) -> Response:
    """
    Gets repairment by ID.
    :param repairment_id: Repairment ID
    :return: Response object
    """
    repairment = repairment_controller.find_by_id(repairment_id)
    if repairment:
        return make_response(jsonify(repairment.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Repairment not found"}), HTTPStatus.NOT_FOUND)

@repairment_bp.put('/<int:repairment_id>')
def update_repairment(repairment_id: int) -> Response:
    """
    Updates repairment by ID.
    :param repairment_id: Repairment ID
    :return: Response object
    """
    content = request.get_json()
    repairment = Repairment.create_from_dto(content)
    repairment_controller.update_repairment(repairment_id, repairment)
    return make_response("Repairment updated", HTTPStatus.OK)

@repairment_bp.delete('/<int:repairment_id>')
def delete_repairment(repairment_id: int) -> Response:
    """
    Deletes repairment by ID.
    :param repairment_id: Repairment ID
    :return: Response object
    """
    repairment_controller.delete_repairment(repairment_id)
    return make_response("Repairment deleted", HTTPStatus.NO_CONTENT)
