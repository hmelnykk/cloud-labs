from typing import List
from my_project.auth.dao.orders.repairment_dao import RepairmentDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.repairment import Repairment

repairment_dao = RepairmentDAO()
class RepairmentService(GeneralService):
    """
    Service implementation for managing repairments.
    """
    _dao = repairment_dao

    def create(self, repairment: Repairment) -> None:
        """
        Creates a new repairment record in the database.
        :param repairment: Repairment to be created
        """
        self._dao.create(repairment)

    def update(self, repairment_id: int, repairment: Repairment) -> None:
        """
        Updates an existing repairment record in the database.
        :param repairment_id: ID of the repairment
        :param repairment: Repairment with updated data
        """
        self._dao.update(repairment_id, repairment)

    def get_all_repairments(self) -> List[Repairment]:
        """
        Retrieves all repairment records from the database.
        :return: List of all repairments
        """
        return self._dao.find_all()

    def get_repairment_by_id(self, repairment_id: int) -> Repairment:
        """
        Retrieves a repairment record by ID.
        :param repairment_id: ID of the repairment
        :return: Repairment
        """
        return self._dao.find_by_id(repairment_id)

    def get_repairments_by_supplier(self, supplier_name: str) -> List[Repairment]:
        """
        Retrieves repairments by supplier name.
        :param supplier_name: Name of the supplier
        :return: List of repairments by the specified supplier
        """
        return self._dao.find_by_supplier_name(supplier_name)
