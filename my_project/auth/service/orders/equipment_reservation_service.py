from typing import List
from my_project.auth.dao.orders.equipment_reservation_dao import EquipmentReservationDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.equipment_reservation import EquipmentReservation

equipment_reservation_dao = EquipmentReservationDAO()
class EquipmentReservationService(GeneralService):
    """
    Service implementation for managing equipment reservations.
    """
    _dao = equipment_reservation_dao

    def create(self, equipment_reservation: EquipmentReservation) -> None:
        """
        Creates a new equipment reservation in the database.
        :param equipment_reservation: EquipmentReservation to be created
        """
        self._dao.create(equipment_reservation)

    def update(self, reservation_id: int, equipment_reservation: EquipmentReservation) -> None:
        """
        Updates an existing equipment reservation in the database.
        :param reservation_id: ID of the reservation
        :param equipment_reservation: EquipmentReservation with updated data
        """
        self._dao.update(reservation_id, equipment_reservation)

    def get_all_reservations(self) -> List[EquipmentReservation]:
        """
        Retrieves all equipment reservations from the database.
        :return: List of all equipment reservations
        """
        return self._dao.find_all()

    def get_reservation_by_id(self, reservation_id: int) -> EquipmentReservation:
        """
        Retrieves an equipment reservation by ID.
        :param reservation_id: ID of the reservation
        :return: EquipmentReservation
        """
        return self._dao.find_by_id(reservation_id)

    def get_reservations_by_supplier(self, supplier_name: str) -> List[EquipmentReservation]:
        """
        Retrieves equipment reservations by supplier name.
        :param supplier_name: Name of the supplier
        :return: List of reservations by the specified supplier
        """
        return self._dao.find_by_supplier_name(supplier_name)
