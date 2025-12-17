from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.equipment import Equipment


class EquipmentDAO(GeneralDAO):
    """
    Data Access Object for Equipment.
    """
    _domain_type = Equipment

    def create(self, equipment: Equipment) -> None:
        self._session.add(equipment)
        self._session.commit()

    def find_all(self) -> List[Equipment]:
        return self._session.query(Equipment).all()

    def find_by_id(self, equipment_id: int) -> Equipment:
        return self._session.query(Equipment).filter(Equipment.id == equipment_id).first()

    def find_by_name(self, name: str) -> List[Equipment]:
        return self._session.query(Equipment).filter(Equipment.name == name).all()

    def find_by_status(self, status: str) -> List[Equipment]:
        return self._session.query(Equipment).filter(Equipment.status == status).all()
