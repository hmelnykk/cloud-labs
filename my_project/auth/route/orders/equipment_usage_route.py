from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.equipment_usage_controller import EquipmentUsageController

equipment_usage_bp = Blueprint('equipment_usage', __name__, url_prefix='/equipment-usage')
controller = EquipmentUsageController()

@equipment_usage_bp.get('')
def get_all_equipment_usages() -> Response:
    equipment_usages = controller.find_all()
    return make_response(jsonify([eu.put_into_dto() for eu in equipment_usages]), HTTPStatus.OK)

@equipment_usage_bp.post('')
def create_equipment_usage() -> Response:
    content = request.get_json()
    equipment_usage = EquipmentUsage.create_from_dto(content)
    controller.create(equipment_usage)
    return make_response(jsonify(equipment_usage.put_into_dto()), HTTPStatus.CREATED)

@equipment_usage_bp.get('/<int:equipment_usage_id>')
def get_equipment_usage(equipment_usage_id: int) -> Response:
    equipment_usage = controller.find_by_id(equipment_usage_id)
    if equipment_usage:
        return make_response(jsonify(equipment_usage.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Equipment usage not found"}), HTTPStatus.NOT_FOUND)

@equipment_usage_bp.put('/<int:equipment_usage_id>')
def update_equipment_usage(equipment_usage_id: int) -> Response:
    content = request.get_json()
    equipment_usage = EquipmentUsage.create_from_dto(content)
    controller.update(equipment_usage_id, equipment_usage)
    return make_response("Equipment usage updated", HTTPStatus.OK)

@equipment_usage_bp.delete('/<int:equipment_usage_id>')
def delete_equipment_usage(equipment_usage_id: int) -> Response:
    controller.delete(equipment_usage_id)
    return make_response("Equipment usage deleted", HTTPStatus.NO_CONTENT)
