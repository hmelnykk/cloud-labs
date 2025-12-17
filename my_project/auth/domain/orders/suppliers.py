from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Suppliers(db.Model, IDto):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    contact = db.Column(db.String(45), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id"), nullable=False)
    equipment_equipment_item_id = db.Column(db.Integer, db.ForeignKey("equipment_item.id"), nullable=False)

    # equipment = db.relationship('Equipment', backref='suppliers')

    def __repr__(self) -> str:
        return f"Suppliers({self.id}, '{self.name}', '{self.contact}', {self.equipment_id}, {self.equipment_equipment_item_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "contact": self.contact,
            "equipment_id": self.equipment_id,
            "equipment_equipment_item_id": self.equipment_equipment_item_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Suppliers:
        return Suppliers(**dto_dict)

