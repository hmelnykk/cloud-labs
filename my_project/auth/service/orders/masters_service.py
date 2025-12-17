from typing import List
from my_project.auth.dao.orders.masters_dao import MastersDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.masters import Masters

masters_dao = MastersDAO()
class MasterService(GeneralService):
    """
    Service implementation for managing masters.
    """
    _dao = masters_dao

    def create(self, master: Masters) -> None:
        """
        Creates a new master in the database.
        :param master: Master to be created
        """
        self._dao.create(master)

    def update(self, master_id: int, master: Masters) -> None:
        """
        Updates an existing master in the database.
        :param master_id: ID of the master
        :param master: Master with updated data
        """
        self._dao.update(master_id, master)

    def get_all_masters(self) -> List[Masters]:
        """
        Retrieves all masters from the database.
        :return: List of all masters
        """
        return self._dao.find_all()

    def get_master_by_id(self, master_id: int) -> Masters:
        """
        Retrieves a master by ID.
        :param master_id: ID of the master
        :return: Master
        """
        return self._dao.find_by_id(master_id)

    def get_master_by_name(self, name: str) -> List[Masters]:
        """
        Retrieves a master by name.
        :param name: Name of the master
        :return: List of masters with the specified name
        """
        return self._dao.find_by_name(name)
