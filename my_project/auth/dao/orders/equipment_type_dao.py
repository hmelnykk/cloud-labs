from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.equipment_type import EquipmentType


class EquipmentTypeDAO(GeneralDAO):
    """
    Data Access Object for EquipmentType.
    """
    _domain_type = EquipmentType

    def create(self, equipment_type: EquipmentType) -> None:
        self._session.add(equipment_type)
        self._session.commit()

    def find_all(self) -> List[EquipmentType]:
        return self._session.query(EquipmentType).all()

    def find_by_id(self, type_id: int) -> EquipmentType:
        return self._session.query(EquipmentType).filter(EquipmentType.id == type_id).first()

    def find_by_name(self, name: str) -> List[EquipmentType]:
        return self._session.query(EquipmentType).filter(EquipmentType.name == name).all()
