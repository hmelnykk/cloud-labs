from typing import List
from my_project.auth.service.orders.projects_service import ProjectService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.projects import Projects


class ProjectsController(GeneralController):
    """
    Controller for projects.
    """
    _service = ProjectService()

    def create_project(self, project: Projects) -> None:
        """
        Creates a new project.
        :param project: the project to create
        """
        self._service.create(project)

    def find_all(self) -> List[Projects]:
        """
        Retrieves all projects.
        :return: list of projects
        """
        return self._service.get_all()

    def find_by_id(self, project_id: int) -> Projects:
        """
        Retrieves a project by ID.
        :param project_id: ID of the project
        :return: the project
        """
        return self._service.get_by_id(project_id)

    def update_project(self, project_id: int, project: Projects) -> None:
        """
        Updates a project by ID.
        :param project_id: ID of the project
        :param project: the updated project
        """
        self._service.update(project_id, project)

    def delete_project(self, project_id: int) -> None:
        """
        Deletes a project by ID.
        :param project_id: ID of the project
        """
        self._service.delete(project_id)
