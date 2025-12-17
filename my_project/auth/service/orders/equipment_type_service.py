from typing import List
from my_project.auth.dao.orders.equipment_type_dao import EquipmentTypeDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.equipment_type import EquipmentType

equipment_type_dao = EquipmentTypeDAO()
class EquipmentTypeService(GeneralService):
    """
    Service implementation for equipment types.
    """
    _dao = equipment_type_dao

    def create(self, equipment_type: EquipmentType) -> None:
        """
        Creates a new equipment type in the database.
        :param equipment_type: The equipment type to create
        """
        self._dao.create(equipment_type)

    def update(self, equipment_type_id: int, equipment_type: EquipmentType) -> None:
        """
        Updates an equipment type in the database.
        :param equipment_type_id: ID of the equipment type
        :param equipment_type: The new equipment type data
        """
        self._dao.update(equipment_type_id, equipment_type)

    def get_all(self) -> List[EquipmentType]:
        """
        Gets all equipment types from the database.
        :return: List of all equipment types
        """
        return self._dao.find_all()

    def get_by_id(self, equipment_type_id: int) -> EquipmentType:
        """
        Gets an equipment type by ID.
        :param equipment_type_id: ID of the equipment type
        :return: The equipment type
        """
        return self._dao.find_by_id(equipment_type_id)
