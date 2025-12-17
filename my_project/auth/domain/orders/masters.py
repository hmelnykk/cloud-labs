from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Masters(db.Model, IDto):
    __tablename__ = "masters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=True)

    # secondary='student_has_projects',
    # students = db.relationship('Student',  backref=db.backref('masters', lazy=True))

    def __repr__(self) -> str:
        return f"Masters({self.id}, '{self.name}', '{self.surname}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Masters:
        return Masters(**dto_dict)
