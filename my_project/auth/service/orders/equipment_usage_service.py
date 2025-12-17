from typing import List
from my_project.auth.dao.orders.equipment_usage_dao import EquipmentUsageDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.equipment_usage import EquipmentUsage

equipment_usage_dao = EquipmentUsageDAO()
class EquipmentUsageService(GeneralService):
    """
    Service implementation for equipment usage.
    """
    _dao = equipment_usage_dao

    def create(self, equipment_usage: EquipmentUsage) -> None:
        """
        Creates a new equipment usage record in the database.
        :param equipment_usage: The equipment usage record to create
        """
        self._dao.create(equipment_usage)

    def update(self, usage_id: int, equipment_usage: EquipmentUsage) -> None:
        """
        Updates an equipment usage record in the database.
        :param usage_id: ID of the equipment usage record
        :param equipment_usage: The new equipment usage data
        """
        self._dao.update(usage_id, equipment_usage)

    def get_all(self) -> List[EquipmentUsage]:
        """
        Gets all equipment usage records from the database.
        :return: List of all equipment usage records
        """
        return self._dao.find_all()

    def get_by_id(self, usage_id: int) -> EquipmentUsage:
        """
        Gets an equipment usage record by ID.
        :param usage_id: ID of the equipment usage record
        :return: The equipment usage record
        """
        return self._dao.find_by_id(usage_id)
