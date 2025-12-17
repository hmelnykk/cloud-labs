from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Student(db.Model, IDto):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    number_stud = db.Column(db.String(45), nullable=True)

    # equipment_usages = db.relationship('EquipmentUsage', backref='student')
    # equipment_reservations = db.relationship('EquipmentReservation', backref='student')
    # student_has_projects = db.relationship('StudentHasProjects', backref='student')

    def __repr__(self) -> str:
        return f"Student({self.id}, '{self.name}', '{self.surname}', '{self.number_stud}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "number_stud": self.number_stud,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Student:
        return Student(**dto_dict)

