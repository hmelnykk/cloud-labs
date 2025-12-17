from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EquipmentItem(db.Model, IDto):
    __tablename__ = "equipment_item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    condition = db.Column(db.String(45), nullable=False)
    purchase_date = db.Column(db.Date, nullable=True)
    serial_number = db.Column(db.String(45), nullable=False)
    equipment_type_id = db.Column(db.Integer, db.ForeignKey("equipment_type.id"), nullable=False)

    # equipment_type = db.relationship('EquipmentType', back_populates='equipment_items')
    # equipment = db.relationship('Equipment', back_populates='equipment_item_id')

    def __repr__(self) -> str:
        return (
            f"EquipmentItem({self.id}, '{self.condition}', '{self.purchase_date}', "
            f"'{self.serial_number}', {self.equipment_type_id})"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "condition": self.condition,
            "purchase_date": self.purchase_date,
            "serial_number": self.serial_number,
            "equipment_type_id": self.equipment_type_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EquipmentItem:
        return EquipmentItem(**dto_dict)