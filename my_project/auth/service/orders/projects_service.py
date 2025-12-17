from typing import List
from my_project.auth.dao.orders.projects_dao import ProjectsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.projects import Projects

projects_dao = ProjectsDAO()
class ProjectService(GeneralService):
    """
    Service implementation for projects.
    """
    _dao = projects_dao

    def create(self, project: Projects) -> None:
        """
        Creates a new project in the database.
        :param project: The project to create
        """
        self._dao.create(project)

    def update(self, project_id: int, project: Projects) -> None:
        """
        Updates a project in the database.
        :param project_id: ID of the project
        :param project: The new project data
        """
        self._dao.update(project_id, project)

    def get_all(self) -> List[Projects]:
        """
        Gets all projects from the database.
        :return: List of all projects
        """
        return self._dao.find_all()

    def get_by_id(self, project_id: int) -> Projects:
        """
        Gets a project by ID.
        :param project_id: ID of the project
        :return: The project
        """
        return self._dao.find_by_id(project_id)
