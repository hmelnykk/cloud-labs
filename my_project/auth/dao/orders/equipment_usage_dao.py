from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.equipment_usage import EquipmentUsage


class EquipmentUsageDAO(GeneralDAO):
    """
    Data Access Object for EquipmentUsage.
    """
    _domain_type = EquipmentUsage

    def create(self, usage: EquipmentUsage) -> None:
        self._session.add(usage)
        self._session.commit()

    def find_all(self) -> List[EquipmentUsage]:
        return self._session.query(EquipmentUsage).all()

    def find_by_id(self, usage_id: int) -> EquipmentUsage:
        return self._session.query(EquipmentUsage).filter(EquipmentUsage.id == usage_id).first()

    def find_by_student_id(self, student_id: int) -> List[EquipmentUsage]:
        return self._session.query(EquipmentUsage).filter(EquipmentUsage.student_id == student_id).all()

    def find_by_project_id(self, project_id: int) -> List[EquipmentUsage]:
        return self._session.query(EquipmentUsage).filter(EquipmentUsage.projects_id == project_id).all()
