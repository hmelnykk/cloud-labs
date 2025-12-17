from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.repairment import Repairment


class RepairmentDAO(GeneralDAO):
    """
    Data Access Object for Repairment.
    """
    _domain_type = Repairment

    def create(self, repairment: Repairment) -> None:
        """
        Adds a new repairment record to the database.
        :param repairment: The repairment entity to be added.
        """
        self._session.add(repairment)
        self._session.commit()

    def find_all(self) -> List[Repairment]:
        """
        Retrieves all repairments from the database.
        :return: List of all repairments.
        """
        return self._session.query(Repairment).all()

    def find_by_id(self, repairment_id: int) -> Repairment:
        """
        Retrieves a repairment by its ID.
        :param repairment_id: ID of the repairment.
        :return: The repairment entity, or None if not found.
        """
        return self._session.query(Repairment).filter(Repairment.id == repairment_id).first()

    def find_by_master_id(self, master_id: int) -> List[Repairment]:
        """
        Retrieves all repairments handled by a specific master.
        :param master_id: ID of the master.
        :return: List of repairments assigned to the master.
        """
        return self._session.query(Repairment).filter(Repairment.masters_id == master_id).all()
