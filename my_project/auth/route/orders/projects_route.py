from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.projects_controller import ProjectsController

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')
controller = ProjectsController()

@projects_bp.get('')
def get_all_projects() -> Response:
    projects = controller.find_all()
    return make_response(jsonify([project.put_into_dto() for project in projects]), HTTPStatus.OK)

@projects_bp.post('')
def create_project() -> Response:
    content = request.get_json()
    project = Project.create_from_dto(content)
    controller.create(project)
    return make_response(jsonify(project.put_into_dto()), HTTPStatus.CREATED)

@projects_bp.get('/<int:project_id>')
def get_project(project_id: int) -> Response:
    project = controller.find_by_id(project_id)
    if project:
        return make_response(jsonify(project.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Project not found"}), HTTPStatus.NOT_FOUND)

@projects_bp.put('/<int:project_id>')
def update_project(project_id: int) -> Response:
    content = request.get_json()
    project = Project.create_from_dto(content)
    controller.update(project_id, project)
    return make_response("Project updated", HTTPStatus.OK)

@projects_bp.delete('/<int:project_id>')
def delete_project(project_id: int) -> Response:
    controller.delete(project_id)
    return make_response("Project deleted", HTTPStatus.NO_CONTENT)
