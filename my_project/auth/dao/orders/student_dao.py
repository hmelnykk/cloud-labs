from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.student import Student


class StudentDAO(GeneralDAO):
    _domain_type = Student

    def create(self, student: Student) -> None:
        self._session.add(student)
        self._session.commit()

    def find_all(self) -> List[Student]:
        return self._session.query(Student).all()

    def find_by_id(self, student_id: int) -> Student:
        return self._session.query(Student).filter(Student.id == student_id).first()

    def find_by_name(self, name: str) -> List[Student]:
        return self._session.query(Student).filter(Student.name == name).all()

    def find_by_number(self, number: str) -> Student:
        return self._session.query(Student).filter(Student.number_stud == number).first()
