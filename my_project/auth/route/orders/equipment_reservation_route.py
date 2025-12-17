from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import equipment_reservation_controller
from my_project.auth.domain.orders.equipment_reservation import EquipmentReservation

equipment_reservation_bp = Blueprint('equipment_reservation', __name__, url_prefix='/equipment_reservations')

@equipment_reservation_bp.get('')
def get_all_reservations() -> Response:
    """
    Gets all equipment reservations from the database.
    :return: Response object
    """
    reservations = equipment_reservation_controller.find_all()
    return make_response(jsonify([reservation.put_into_dto() for reservation in reservations]), HTTPStatus.OK)

@equipment_reservation_bp.post('')
def create_reservation() -> Response:
    """
    Creates a new equipment reservation in the database.
    :return: Response object
    """
    content = request.get_json()
    reservation = EquipmentReservation.create_from_dto(content)
    equipment_reservation_controller.create_reservation(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)

@equipment_reservation_bp.get('/<int:reservation_id>')
def get_reservation(reservation_id: int) -> Response:
    """
    Gets reservation by ID.
    :param reservation_id: Reservation ID
    :return: Response object
    """
    reservation = equipment_reservation_controller.find_by_id(reservation_id)
    if reservation:
        return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Reservation not found"}), HTTPStatus.NOT_FOUND)

@equipment_reservation_bp.put('/<int:reservation_id>')
def update_reservation(reservation_id: int) -> Response:
    """
    Updates reservation by ID.
    :param reservation_id: Reservation ID
    :return: Response object
    """
    content = request.get_json()
    reservation = EquipmentReservation.create_from_dto(content)
    equipment_reservation_controller.update_reservation(reservation_id, reservation)
    return make_response("Reservation updated", HTTPStatus.OK)

@equipment_reservation_bp.delete('/<int:reservation_id>')
def delete_reservation(reservation_id: int) -> Response:
    """
    Deletes reservation by ID.
    :param reservation_id: Reservation ID
    :return: Response object
    """
    equipment_reservation_controller.delete_reservation(reservation_id)
    return make_response("Reservation deleted", HTTPStatus.NO_CONTENT)
