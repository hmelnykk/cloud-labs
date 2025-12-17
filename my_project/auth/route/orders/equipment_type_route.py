from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.equipment_type_controller import EquipmentTypeController

equipment_type_bp = Blueprint('equipment_type', __name__, url_prefix='/equipment-type')
controller = EquipmentTypeController()

@equipment_type_bp.get('')
def get_all_equipment_types() -> Response:
    equipment_types = controller.find_all()
    return make_response(jsonify([et.put_into_dto() for et in equipment_types]), HTTPStatus.OK)

@equipment_type_bp.post('')
def create_equipment_type() -> Response:
    content = request.get_json()
    equipment_type = EquipmentType.create_from_dto(content)
    controller.create(equipment_type)
    return make_response(jsonify(equipment_type.put_into_dto()), HTTPStatus.CREATED)

@equipment_type_bp.get('/<int:equipment_type_id>')
def get_equipment_type(equipment_type_id: int) -> Response:
    equipment_type = controller.find_by_id(equipment_type_id)
    if equipment_type:
        return make_response(jsonify(equipment_type.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Equipment type not found"}), HTTPStatus.NOT_FOUND)

@equipment_type_bp.put('/<int:equipment_type_id>')
def update_equipment_type(equipment_type_id: int) -> Response:
    content = request.get_json()
    equipment_type = EquipmentType.create_from_dto(content)
    controller.update(equipment_type_id, equipment_type)
    return make_response("Equipment type updated", HTTPStatus.OK)

@equipment_type_bp.delete('/<int:equipment_type_id>')
def delete_equipment_type(equipment_type_id: int) -> Response:
    controller.delete(equipment_type_id)
    return make_response("Equipment type deleted", HTTPStatus.NO_CONTENT)
