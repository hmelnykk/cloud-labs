from typing import List
from my_project.auth.service import EquipmentService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.equipment import Equipment


class EquipmentController(GeneralController):
    """
    Controller for equipment.
    """
    _service = EquipmentService()

    def create_equipment(self, equipment: Equipment) -> None:
        """
        Creates a new equipment.
        :param equipment: the equipment to create
        """
        self._service.create(equipment)

    def find_all(self) -> List[Equipment]:
        """
        Retrieves all equipment.
        :return: list of equipment
        """
        return self._service.get_all()

    def find_by_id(self, equipment_id: int) -> Equipment:
        """
        Retrieves equipment by ID.
        :param equipment_id: ID of the equipment
        :return: the equipment
        """
        return self._service.get_by_id(equipment_id)

    def update_equipment(self, equipment_id: int, equipment: Equipment) -> None:
        """
        Updates equipment by ID.
        :param equipment_id: ID of the equipment
        :param equipment: the updated equipment
        """
        self._service.update(equipment_id, equipment)

    def delete_equipment(self, equipment_id: int) -> None:
        """
        Deletes equipment by ID.
        :param equipment_id: ID of the equipment
        """
        self._service.delete(equipment_id)
