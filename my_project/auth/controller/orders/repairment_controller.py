from typing import List
from my_project.auth.service.orders.repairment_service import RepairmentService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.repairment import Repairment


class RepairmentController(GeneralController):
    """
    Controller for repairments.
    """
    _service = RepairmentService()

    def create_repairment(self, repairment: Repairment) -> None:
        """
        Creates a new repairment.
        :param repairment: the repairment to create
        """
        self._service.create(repairment)

    def find_all(self) -> List[Repairment]:
        """
        Retrieves all repairments.
        :return: list of repairments
        """
        return self._service.get_all()

    def find_by_id(self, repairment_id: int) -> Repairment:
        """
        Retrieves a repairment by ID.
        :param repairment_id: ID of the repairment
        :return: the repairment
        """
        return self._service.get_by_id(repairment_id)

    def update_repairment(self, repairment_id: int, repairment: Repairment) -> None:
        """
        Updates a repairment by ID.
        :param repairment_id: ID of the repairment
        :param repairment: the updated repairment
        """
        self._service.update(repairment_id, repairment)

    def delete_repairment(self, repairment_id: int) -> None:
        """
        Deletes a repairment by ID.
        :param repairment_id: ID of the repairment
        """
        self._service.delete(repairment_id)
