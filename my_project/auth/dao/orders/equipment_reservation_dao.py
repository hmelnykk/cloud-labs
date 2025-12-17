from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.equipment_reservation import EquipmentReservation

class EquipmentReservationDAO(GeneralDAO):
    """
    Data Access Object for Equipment Reservations.
    """
    _domain_type = EquipmentReservation

    def create(self, equipment_reservation: EquipmentReservation) -> None:
        """
        Adds a new equipment reservation to the database.
        """
        self._session.add(equipment_reservation)
        self._session.commit()

    def find_all(self) -> List[EquipmentReservation]:
        """
        Retrieves all equipment reservations from the database.
        :return: List of EquipmentReservation
        """
        return self._session.query(EquipmentReservation).all()

    def find_by_id(self, reservation_id: int) -> EquipmentReservation:
        """
        Retrieves a specific equipment reservation by its ID.
        :param reservation_id: The ID of the reservation
        :return: EquipmentReservation object
        """
        return self._session.query(EquipmentReservation).filter(EquipmentReservation.id == reservation_id).first()

    def find_by_status(self, status: str) -> List[EquipmentReservation]:
        """
        Retrieves all equipment reservations with the specified status.
        :param status: The status of the reservations
        :return: List of EquipmentReservation
        """
        return self._session.query(EquipmentReservation).filter(EquipmentReservation.status == status).all()

    def find_by_project_id(self, project_id: int) -> List[EquipmentReservation]:
        """
        Retrieves all equipment reservations for a specific project ID.
        :param project_id: The project ID
        :return: List of EquipmentReservation
        """
        return self._session.query(EquipmentReservation).filter(EquipmentReservation.projects_id == project_id).all()

    def update(self, reservation_id: int, equipment_reservation: EquipmentReservation) -> None:
        """
        Updates an existing equipment reservation.
        :param reservation_id: ID of the reservation to update
        :param equipment_reservation: New data for the reservation
        """
        reservation = self.find_by_id(reservation_id)
        if reservation:
            reservation.reservation_start = equipment_reservation.reservation_start
            reservation.reservation_end = equipment_reservation.reservation_end
            reservation.status = equipment_reservation.status
            reservation.projects_id = equipment_reservation.projects_id
            reservation.student_id = equipment_reservation.student_id
            reservation.equipment_item_id = equipment_reservation.equipment_item_id
            self._session.commit()
