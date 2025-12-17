
from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EquipmentType(db.Model, IDto):
    __tablename__ = "equipment_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    # equipment_items = db.relationship('EquipmentItem', backref='equipment_type')

    def __repr__(self) -> str:
        return f"EquipmentType({self.id}, '{self.name}', '{self.description}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EquipmentType:
        return EquipmentType(**dto_dict)
