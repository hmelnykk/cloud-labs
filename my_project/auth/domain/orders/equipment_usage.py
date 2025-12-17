from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EquipmentUsage(db.Model, IDto):
    __tablename__ = "equipment_usage"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    time_used = db.Column(db.String(45), nullable=False)
    projects_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    equipment_item_id = db.Column(db.Integer, db.ForeignKey("equipment_item.id"), nullable=False)

    # project = db.relationship('Projects', backref='equipment_usages')
    # student = db.relationship('Student', backref='equipment_usages')
    # equipment_item = db.relationship('EquipmentItem', backref='equipment_usages')

    def __repr__(self) -> str:
        return (
            f"EquipmentUsage({self.id}, '{self.check_in}', '{self.check_out}', "
            f"'{self.time_used}', {self.projects_id}, {self.student_id}, {self.equipment_item_id})"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "time_used": self.time_used,
            "projects_id": self.projects_id,
            "student_id": self.student_id,
            "equipment_item_id": self.equipment_item_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EquipmentUsage:
        return EquipmentUsage(**dto_dict)