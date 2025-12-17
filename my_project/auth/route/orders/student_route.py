from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.student_controller import StudentController
from my_project.auth.domain.orders.student import Student

student_bp = Blueprint('student', __name__, url_prefix='/student')
controller = StudentController()

@student_bp.get('')
def get_all_students() -> Response:
    students = controller.find_all()
    return make_response(jsonify([student.put_into_dto() for student in students]), HTTPStatus.OK)

@student_bp.post('')
def create_student() -> Response:
    content = request.get_json()
    student = Student.create_from_dto(content)
    controller.create(student)
    return make_response(jsonify(student.put_into_dto()), HTTPStatus.CREATED)

@student_bp.get('/<int:student_id>')
def get_student(student_id: int) -> Response:
    student = controller.find_by_id(student_id)
    if student:
        return make_response(jsonify(student.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Student not found"}), HTTPStatus.NOT_FOUND)

@student_bp.put('/<int:student_id>')
def update_student(student_id: int) -> Response:
    content = request.get_json()
    student = Student.create_from_dto(content)
    controller.update(student_id, student)
    return make_response("Student updated", HTTPStatus.OK)

@student_bp.delete('/<int:student_id>')
def delete_student(student_id: int) -> Response:
    controller.delete(student_id)
    return make_response("Student deleted", HTTPStatus.NO_CONTENT)
