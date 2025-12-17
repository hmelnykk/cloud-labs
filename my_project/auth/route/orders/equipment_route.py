from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
# from my_project.auth.controller.orders import equipment_controller
from my_project.auth.domain.orders.equipment import Equipment
from my_project.auth.controller.orders.equipment_controller import EquipmentController

equipment_controller = EquipmentController()

equipment_bp = Blueprint('equipment', __name__, url_prefix='/equipment')
controller = equipment_controller

@equipment_bp.get('')
def get_all_equipments() -> Response:
    equipments = controller.find_all()
    return make_response(jsonify([eq.put_into_dto() for eq in equipments]), HTTPStatus.OK)

@equipment_bp.post('')
def create_equipment() -> Response:
    content = request.get_json()
    equipment = Equipment.create_from_dto(content)
    controller.create(equipment)
    return make_response(jsonify(equipment.put_into_dto()), HTTPStatus.CREATED)

@equipment_bp.get('/<int:equipment_id>')
def get_equipment(equipment_id: int) -> Response:
    equipment = controller.find_by_id(equipment_id)
    if equipment:
        return make_response(jsonify(equipment.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Equipment not found"}), HTTPStatus.NOT_FOUND)

@equipment_bp.put('/<int:equipment_id>')
def update_equipment(equipment_id: int) -> Response:
    content = request.get_json()
    equipment = Equipment.create_from_dto(content)
    controller.update(equipment_id, equipment)
    return make_response("Equipment updated", HTTPStatus.OK)

@equipment_bp.delete('/<int:equipment_id>')
def delete_equipment(equipment_id: int) -> Response:
    controller.delete(equipment_id)
    return make_response("Equipment deleted", HTTPStatus.NO_CONTENT)
