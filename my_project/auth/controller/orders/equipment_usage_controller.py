from typing import List
from my_project.auth.service.orders.equipment_usage_service import EquipmentUsageService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.equipment_usage import EquipmentUsage


class EquipmentUsageController(GeneralController):
    """
    Controller for equipment usage.
    """
    _service = EquipmentUsageService()

    def create_usage(self, usage: EquipmentUsage) -> None:
        """
        Records a new equipment usage.
        :param usage: the equipment usage to record
        """
        self._service.create(usage)

    def find_all(self) -> List[EquipmentUsage]:
        """
        Retrieves all equipment usage records.
        :return: list of usage records
        """
        return self._service.get_all()

    def find_by_id(self, usage_id: int) -> EquipmentUsage:
        """
        Retrieves an equipment usage record by ID.
        :param usage_id: ID of the usage record
        :return: the usage record
        """
        return self._service.get_by_id(usage_id)

    def update_usage(self, usage_id: int, usage: EquipmentUsage) -> None:
        """
        Updates an equipment usage record by ID.
        :param usage_id: ID of the usage record
        :param usage: the updated usage record
        """
        self._service.update(usage_id, usage)

    def delete_usage(self, usage_id: int) -> None:
        """
        Deletes an equipment usage record by ID.
        :param usage_id: ID of the usage record
        """
        self._service.delete(usage_id)
