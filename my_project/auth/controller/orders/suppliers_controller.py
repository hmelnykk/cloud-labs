from typing import List
from my_project.auth.service.orders.suppliers_service import SupplierService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.suppliers import Suppliers


class SuppliersController(GeneralController):
    """
    Controller for suppliers.
    """
    _service = SupplierService()

    def create_supplier(self, supplier: Suppliers) -> None:
        """
        Creates a new supplier.
        :param supplier: the supplier to create
        """
        self._service.create(supplier)

    def find_all(self) -> List[Suppliers]:
        """
        Retrieves all suppliers.
        :return: list of suppliers
        """
        return self._service.get_all()

    def find_by_id(self, supplier_id: int) -> Suppliers:
        """
        Retrieves a supplier by ID.
        :param supplier_id: ID of the supplier
        :return: the supplier
        """
        return self._service.get_by_id(supplier_id)

    def update_supplier(self, supplier_id: int, supplier: Suppliers) -> None:
        """
        Updates a supplier by ID.
        :param supplier_id: ID of the supplier
        :param supplier: the updated supplier
        """
        self._service.update(supplier_id, supplier)

    def delete_supplier(self, supplier_id: int) -> None:
        """
        Deletes a supplier by ID.
        :param supplier_id: ID of the supplier
        """
        self._service.delete(supplier_id)
