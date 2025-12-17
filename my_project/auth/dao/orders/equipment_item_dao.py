from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.equipment_item import EquipmentItem


class EquipmentItemDAO(GeneralDAO):
    """
    Data Access Object for EquipmentItem.
    """
    _domain_type = EquipmentItem

    def create(self, item: EquipmentItem) -> None:
        """
        Adds a new equipment item to the database.
        :param item: the equipment item to add
        """
        self._session.add(item)
        self._session.commit()

    def find_all(self) -> List[EquipmentItem]:
        """
        Retrieves all equipment items from the database.
        :return: list of all equipment items
        """
        return self._session.query(EquipmentItem).all()

    def find_by_id(self, item_id: int) -> EquipmentItem:
        """
        Retrieves an equipment item by its ID.
        :param item_id: ID of the equipment item
        :return: the equipment item
        """
        return self._session.query(EquipmentItem).filter(EquipmentItem.id == item_id).first()

    def find_by_condition(self, condition: str) -> List[EquipmentItem]:
        """
        Retrieves equipment items by their condition (e.g., "New", "Used").
        :param condition: condition of the equipment items
        :return: list of matching equipment items
        """
        return self._session.query(EquipmentItem).filter(EquipmentItem.condition == condition).all()

    def find_by_equipment_type(self, equipment_type_id: int) -> List[EquipmentItem]:
        """
        Retrieves equipment items by their equipment type ID.
        :param equipment_type_id: the equipment type ID
        :return: list of equipment items with the specified equipment type
        """
        return self._session.query(EquipmentItem).filter(EquipmentItem.equipment_type_id == equipment_type_id).all()

    def find_by_serial_number(self, serial_number: str) -> EquipmentItem:
        """
        Retrieves an equipment item by its serial number.
        :param serial_number: the serial number of the equipment item
        :return: the equipment item
        """
        return self._session.query(EquipmentItem).filter(EquipmentItem.serial_number == serial_number).first()
