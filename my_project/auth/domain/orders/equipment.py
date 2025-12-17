from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Equipment(db.Model, IDto):
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    equipment_item_id = db.Column(db.Integer, db.ForeignKey("equipment_item.id"), nullable=False)

    # equipment_item = db.relationship('EquipmentItem', backref='equipments')

    def __repr__(self) -> str:
        return f"Equipment({self.id}, '{self.name}', '{self.description}', '{self.status}', {self.equipment_item_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "equipment_item_id": self.equipment_item_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Equipment:
        return Equipment(**dto_dict)
