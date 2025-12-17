from typing import List
from my_project.auth.service.orders.masters_service import MasterService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.masters import Masters


class MastersController(GeneralController):
    """
    Controller for masters.
    """
    _service = MasterService()

    def create_master(self, master: Masters) -> None:
        """
        Creates a new master.
        :param master: the master to create
        """
        self._service.create(master)

    def find_all(self) -> List[Masters]:
        """
        Retrieves all masters.
        :return: list of masters
        """
        return self._service.get_all()

    def find_by_id(self, master_id: int) -> Masters:
        """
        Retrieves a master by ID.
        :param master_id: ID of the master
        :return: the master
        """
        return self._service.get_by_id(master_id)

    def update_master(self, master_id: int, master: Masters) -> None:
        """
        Updates a master by ID.
        :param master_id: ID of the master
        :param master: the updated master
        """
        self._service.update(master_id, master)

    def delete_master(self, master_id: int) -> None:
        """
        Deletes a master by ID.
        :param master_id: ID of the master
        """
        self._service.delete(master_id)
