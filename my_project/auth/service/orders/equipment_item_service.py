from typing import List
from my_project.auth.dao.orders.equipment_item_dao import EquipmentItemDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.equipment_item import EquipmentItem

equipment_item_dao = EquipmentItemDAO()
class EquipmentItemService(GeneralService):
    """
    Service implementation for equipment items.
    """
    _dao = equipment_item_dao

    def create(self, equipment_item: EquipmentItem) -> None:
        """
        Creates a new equipment item in the database.
        :param equipment_item: The equipment item to create
        """
        self._dao.create(equipment_item)

    def update(self, equipment_item_id: int, equipment_item: EquipmentItem) -> None:
        """
        Updates an equipment item in the database.
        :param equipment_item_id: ID of the equipment item
        :param equipment_item: The new equipment item data
        """
        self._dao.update(equipment_item_id, equipment_item)

    def get_all(self) -> List[EquipmentItem]:
        """
        Gets all equipment items from the database.
        :return: List of all equipment items
        """
        return self._dao.find_all()

    def get_by_id(self, equipment_item_id: int) -> EquipmentItem:
        """
        Gets an equipment item by ID.
        :param equipment_item_id: ID of the equipment item
        :return: The equipment item
        """
        return self._dao.find_by_id(equipment_item_id)
