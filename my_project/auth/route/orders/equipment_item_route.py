from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.equipment_item_controller import EquipmentItemController

equipment_item_bp = Blueprint('equipment_item', __name__, url_prefix='/equipment-item')
controller = EquipmentItemController()

@equipment_item_bp.get('')
def get_all_equipment_items() -> Response:
    equipment_items = controller.find_all()
    return make_response(jsonify([ei.put_into_dto() for ei in equipment_items]), HTTPStatus.OK)

@equipment_item_bp.post('')
def create_equipment_item() -> Response:
    content = request.get_json()
    equipment_item = EquipmentItem.create_from_dto(content)
    controller.create(equipment_item)
    return make_response(jsonify(equipment_item.put_into_dto()), HTTPStatus.CREATED)

@equipment_item_bp.get('/<int:equipment_item_id>')
def get_equipment_item(equipment_item_id: int) -> Response:
    equipment_item = controller.find_by_id(equipment_item_id)
    if equipment_item:
        return make_response(jsonify(equipment_item.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Equipment item not found"}), HTTPStatus.NOT_FOUND)

@equipment_item_bp.put('/<int:equipment_item_id>')
def update_equipment_item(equipment_item_id: int) -> Response:
    content = request.get_json()
    equipment_item = EquipmentItem.create_from_dto(content)
    controller.update(equipment_item_id, equipment_item)
    return make_response("Equipment item updated", HTTPStatus.OK)

@equipment_item_bp.delete('/<int:equipment_item_id>')
def delete_equipment_item(equipment_item_id: int) -> Response:
    controller.delete(equipment_item_id)
    return make_response("Equipment item deleted", HTTPStatus.NO_CONTENT)
