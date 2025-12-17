from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Repairment(db.Model, IDto):
    __tablename__ = "repairment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    master_name = db.Column(db.String(45), nullable=False)
    masters_id = db.Column(db.Integer, db.ForeignKey("masters.id"), nullable=False)
    equipment_item_id = db.Column(db.Integer, db.ForeignKey("equipment_item.id"), nullable=False)

    # master = db.relationship('Masters', backref='repairments')
    # equipment_item = db.relationship('EquipmentItem', backref='repairments')

    def __repr__(self) -> str:
        return (
            f"Repairment({self.id}, '{self.start_date}', '{self.end_date}', "
            f"'{self.master_name}', {self.masters_id}, {self.equipment_item_id})"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "master_name": self.master_name,
            "masters_id": self.masters_id,
            "equipment_item_id": self.equipment_item_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Repairment:
        return Repairment(**dto_dict)