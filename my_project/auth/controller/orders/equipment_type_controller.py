from typing import List
from my_project.auth.service.orders.equipment_type_service import EquipmentTypeService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.equipment_type import EquipmentType


class EquipmentTypeController(GeneralController):
    """
    Controller for equipment types.
    """
    _service = EquipmentTypeService()

    def create_equipment_type(self, equipment_type: EquipmentType) -> None:
        """
        Creates a new equipment type.
        :param equipment_type: the equipment type to create
        """
        self._service.create(equipment_type)

    def find_all(self) -> List[EquipmentType]:
        """
        Retrieves all equipment types.
        :return: list of equipment types
        """
        return self._service.get_all()

    def find_by_id(self, type_id: int) -> EquipmentType:
        """
        Retrieves an equipment type by ID.
        :param type_id: ID of the equipment type
        :return: the equipment type
        """
        return self._service.get_by_id(type_id)

    def update_equipment_type(self, type_id: int, equipment_type: EquipmentType) -> None:
        """
        Updates an equipment type by ID.
        :param type_id: ID of the equipment type
        :param equipment_type: the updated equipment type
        """
        self._service.update(type_id, equipment_type)

    def delete_equipment_type(self, type_id: int) -> None:
        """
        Deletes an equipment type by ID.
        :param type_id: ID of the equipment type
        """
        self._service.delete(type_id)
