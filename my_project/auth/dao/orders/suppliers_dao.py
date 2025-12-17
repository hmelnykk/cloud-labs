from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.suppliers import Suppliers


class SuppliersDAO(GeneralDAO):
    """
    Data Access Object for Suppliers.
    """
    _domain_type = Suppliers

    def create(self, supplier: Suppliers) -> None:
        self._session.add(supplier)
        self._session.commit()

    def find_all(self) -> List[Suppliers]:
        return self._session.query(Suppliers).all()

    def find_by_id(self, supplier_id: int) -> Suppliers:
        return self._session.query(Suppliers).filter(Suppliers.id == supplier_id).first()

    def find_by_name(self, name: str) -> List[Suppliers]:
        return self._session.query(Suppliers).filter(Suppliers.name == name).all()
