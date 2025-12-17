from typing import List
from my_project.auth.service.orders.equipment_reservation_service import EquipmentReservationService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.equipment_reservation import EquipmentReservation


class EquipmentReservationController(GeneralController):
    """
    Controller for equipment reservations.
    """
    _service = EquipmentReservationService()

    def create_reservation(self, reservation: EquipmentReservation) -> None:
        """
        Creates a new equipment reservation.
        :param reservation: the reservation to create
        """
        self._service.create(reservation)

    def find_all(self) -> List[EquipmentReservation]:
        """
        Retrieves all equipment reservations.
        :return: list of reservations
        """
        return self._service.get_all()

    def find_by_id(self, reservation_id: int) -> EquipmentReservation:
        """
        Retrieves an equipment reservation by ID.
        :param reservation_id: ID of the reservation
        :return: the reservation
        """
        return self._service.get_by_id(reservation_id)

    def update_reservation(self, reservation_id: int, reservation: EquipmentReservation) -> None:
        """
        Updates an equipment reservation by ID.
        :param reservation_id: ID of the reservation
        :param reservation: the updated reservation
        """
        self._service.update(reservation_id, reservation)

    def delete_reservation(self, reservation_id: int) -> None:
        """
        Deletes an equipment reservation by ID.
        :param reservation_id: ID of the reservation
        """
        self._service.delete(reservation_id)
