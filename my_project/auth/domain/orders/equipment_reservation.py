from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class EquipmentReservation(db.Model, IDto):
    __tablename__ = "equpment_reservation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservation_start = db.Column(db.Date, nullable=False)
    reservation_end = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(45), nullable=False)
    projects_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    equipment_item_id = db.Column(db.Integer, db.ForeignKey("equipment_item.id"), nullable=False)

    # project = db.relationship('Projects', back_populates='equipment_reservations')
    # student = db.relationship('Student', back_populates='equipment_reservations')
    # equipment_item = db.relationship('EquipmentItem', back_populates='equipment_reservations')

    def __repr__(self) -> str:
        return f"EquipmentReservation({self.id}, '{self.reservation_start}', '{self.reservation_end}', '{self.status}', {self.projects_id}, {self.student_id}, {self.equipment_item_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "reservation_start": self.reservation_start,
            "reservation_end": self.reservation_end,
            "status": self.status,
            "projects_id": self.projects_id,
            "student_id": self.student_id,
            "equipment_item_id": self.equipment_item_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EquipmentReservation:
        return EquipmentReservation(**dto_dict)
