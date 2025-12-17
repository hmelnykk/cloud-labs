from typing import List
from my_project.auth.service.orders.student_service import StudentService
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.student import Student

student_service = StudentService()

class StudentController(GeneralController):
    """
    Controller for students.
    """
    _service = student_service

    def create_student(self, student: Student) -> None:
        """
        Creates a new student.
        :param student: the student to create
        """
        self._service.create(student)

    def find_all(self) -> List[Student]:
        """
        Retrieves all students.
        :return: list of students
        """
        return self._service.get_all()

    def find_by_id(self, student_id: int) -> Student:
        """
        Retrieves a student by ID.
        :param student_id: ID of the student
        :return: the student
        """
        return self._service.get_by_id(student_id)

    def update_student(self, student_id: int, student: Student) -> None:
        """
        Updates a student by ID.
        :param student_id: ID of the student
        :param student: the updated student
        """
        self._service.update(student_id, student)

    def delete_student(self, student_id: int) -> None:
        """
        Deletes a student by ID.
        :param student_id: ID of the student
        """
        self._service.delete(student_id)
