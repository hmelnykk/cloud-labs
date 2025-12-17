from typing import List
from my_project.auth.dao.orders.student_dao import StudentDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.student import Student

student_dao = StudentDAO()
class StudentService(GeneralService):
    """
    Service implementation for students.
    """
    _dao = student_dao

    def create(self, student: Student) -> None:
        """
        Creates a new student in the database.
        :param student: The student to create
        """
        self._dao.create(student)

    def update(self, student_id: int, student: Student) -> None:
        """
        Updates a student in the database.
        :param student_id: ID of the student
        :param student: The new student data
        """
        self._dao.update(student_id, student)

    def get_all(self) -> List[Student]:
        """
        Gets all students from the database.
        :return: List of all students
        """
        return self._dao.find_all()

    def get_by_id(self, student_id: int) -> Student:
        """
        Gets a student by ID.
        :param student_id: ID of the student
        :return: The student
        """
        return self._dao.find_by_id(student_id)
