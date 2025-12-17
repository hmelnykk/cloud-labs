from typing import List
from my_project.auth.dao.orders.equipment_dao import EquipmentDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.equipment import Equipment

equipment_dao = EquipmentDAO()

class EquipmentService(GeneralService):
    """
    Service implementation for equipment.
    """
    _dao = equipment_dao

    def create(self, equipment: Equipment) -> None:
        """
        Creates a new equipment in the database.
        :param equipment: The equipment to create
        """
        self._dao.create(equipment)

    def update(self, equipment_id: int, equipment: Equipment) -> None:
        """
        Updates equipment in the database.
        :param equipment_id: ID of the equipment
        :param equipment: The new equipment data
        """
        self._dao.update(equipment_id, equipment)

    def get_all(self) -> List[Equipment]:
        """
        Gets all equipment from the database.
        :return: List of all equipment
        """
        return self._dao.find_all()

    def get_by_id(self, equipment_id: int) -> Equipment:
        """
        Gets equipment by ID.
        :param equipment_id: ID of the equipment
        :return: The equipment
        """
        return self._dao.find_by_id(equipment_id)
