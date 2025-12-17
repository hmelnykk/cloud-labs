from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.masters import Masters


class MastersDAO(GeneralDAO):
    """
    Data Access Object for Masters.
    """
    _domain_type = Masters

    def create(self, master: Masters) -> None:
        self._session.add(master)
        self._session.commit()

    def find_all(self) -> List[Masters]:
        return self._session.query(Masters).all()

    def find_by_id(self, master_id: int) -> Masters:
        return self._session.query(Masters).filter(Masters.id == master_id).first()

    def find_by_email(self, email: str) -> Masters:
        return self._session.query(Masters).filter(Masters.email == email).first()
