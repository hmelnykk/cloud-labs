from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.projects import Projects


class ProjectsDAO(GeneralDAO):
    """
    Data Access Object for Projects.
    """
    _domain_type = Projects

    def create(self, project: Projects) -> None:
        self._session.add(project)
        self._session.commit()

    def find_all(self) -> List[Projects]:
        return self._session.query(Projects).all()

    def find_by_id(self, project_id: int) -> Projects:
        return self._session.query(Projects).filter(Projects.id == project_id).first()

    def find_by_name(self, name: str) -> List[Projects]:
        return self._session.query(Projects).filter(Projects.name == name).all()
