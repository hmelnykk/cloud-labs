from typing import List
from my_project.auth.dao.orders.suppliers_dao import SuppliersDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.suppliers import Suppliers

suppliers_dao = SuppliersDAO()
class SupplierService(GeneralService):
    """
    Service implementation for managing suppliers.
    """
    _dao = suppliers_dao

    def create(self, supplier: Suppliers) -> None:
        """
        Creates a new supplier in the database.
        :param supplier: Supplier to be created
        """
        self._dao.create(supplier)

    def update(self, supplier_id: int, supplier: Suppliers) -> None:
        """
        Updates an existing supplier in the database.
        :param supplier_id: ID of the supplier
        :param supplier: Supplier with updated data
        """
        self._dao.update(supplier_id, supplier)

    def get_all_suppliers(self) -> List[Suppliers]:
        """
        Retrieves all suppliers from the database.
        :return: List of all suppliers
        """
        return self._dao.find_all()

    def get_supplier_by_id(self, supplier_id: int) -> Suppliers:
        """
        Retrieves a supplier by ID.
        :param supplier_id: ID of the supplier
        :return: Supplier
        """
        return self._dao.find_by_id(supplier_id)

    def get_supplier_by_name(self, name: str) -> List[Suppliers]:
        """
        Retrieves a supplier by name.
        :param name: Name of the supplier
        :return: List of suppliers with the specified name
        """
        return self._dao.find_by_name(name)
