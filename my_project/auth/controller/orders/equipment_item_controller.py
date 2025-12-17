from typing import List
from my_project.auth.service.orders.equipment_item_service import EquipmentItemService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.equipment_item import EquipmentItem


class EquipmentItemController(GeneralController):
    """
    Controller for equipment items.
    """
    _service = EquipmentItemService()

    def create_item(self, item: EquipmentItem) -> None:
        """
        Creates a new equipment item.
        :param item: the equipment item to create
        """
        self._service.create(item)

    def find_all(self) -> List[EquipmentItem]:
        """
        Retrieves all equipment items.
        :return: list of equipment items
        """
        return self._service.get_all()

    def find_by_id(self, item_id: int) -> EquipmentItem:
        """
        Retrieves an equipment item by ID.
        :param item_id: ID of the equipment item
        :return: the equipment item
        """
        return self._service.get_by_id(item_id)

    def update_item(self, item_id: int, item: EquipmentItem) -> None:
        """
        Updates an equipment item by ID.
        :param item_id: ID of the equipment item
        :param item: the updated equipment item
        """
        self._service.update(item_id, item)

    def delete_item(self, item_id: int) -> None:
        """
        Deletes an equipment item by ID.
        :param item_id: ID of the equipment item
        """
        self._service.delete(item_id)

    def get_items_by_condition(self, condition: str) -> List[EquipmentItem]:
        """
        Retrieves equipment items by their condition.
        :param condition: the condition of the items (e.g., "New", "Used")
        :return: list of equipment items matching the condition
        """
        return self._service.get_by_condition(condition)

    def get_items_by_equipment_type(self, equipment_type_id: int) -> List[EquipmentItem]:
        """
        Retrieves equipment items by their type.
        :param equipment_type_id: the ID of the equipment type
        :return: list of equipment items matching the type
        """
        return self._service.get_by_equipment_type(equipment_type_id)
