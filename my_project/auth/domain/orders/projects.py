from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Projects(db.Model, IDto):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    # equipment_items = db.Column(db.ForeignKey(''))

    # equipment_items_id = db.relationship('EquipmentItem', secondary='equipment', backref=db.backref('projects', lazy=True))
    # secondary='student_has_projects',

    # students = db.relationship('Student',  backref=db.backref('projects', lazy=True))

    def __repr__(self) -> str:
        return f"Projects({self.id}, '{self.name}', '{self.description}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Projects:
        return Projects(**dto_dict)
