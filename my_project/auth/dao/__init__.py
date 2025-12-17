"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import the specific DAO classes for each table
from .orders.student_dao import StudentDAO
from .orders.projects_dao import ProjectsDAO
from .orders.equipment_dao import EquipmentDAO
from .orders.equipment_item_dao import EquipmentItemDAO
from .orders.equipment_type_dao import EquipmentTypeDAO
from .orders.equipment_usage_dao import EquipmentUsageDAO
from .orders.masters_dao import MastersDAO
from .orders.repairment_dao import RepairmentDAO
from .orders.suppliers_dao import SuppliersDAO
from .orders.equipment_reservation_dao import EquipmentReservationDAO

# Initialize the DAOs
student_dao = StudentDAO()
project_dao = ProjectsDAO()
equipment_dao = EquipmentDAO()
equipment_item_dao = EquipmentItemDAO()
equipment_type_dao = EquipmentTypeDAO()
equipment_usage_dao = EquipmentUsageDAO()
masters_dao = MastersDAO()
repairment_dao = RepairmentDAO()
suppliers_dao = SuppliersDAO()
equipment_reservation_dao = EquipmentReservationDAO()
