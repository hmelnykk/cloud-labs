"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import the specific services for each table
from .orders.student_service import StudentService
from .orders.projects_service import ProjectService
from .orders.equipment_service import EquipmentService
from .orders.equipment_item_service import EquipmentItemService
from .orders.equipment_type_service import EquipmentTypeService
from .orders.equipment_usage_service import EquipmentUsageService
from .orders.masters_service import MasterService
from .orders.repairment_service import RepairmentService
from .orders.suppliers_service import SupplierService
from .orders.equipment_reservation_service import EquipmentReservationService

# Initialize the services
student_service = StudentService()
project_service = ProjectService()
equipment_service = EquipmentService()
equipment_item_service = EquipmentItemService()
equipment_type_service = EquipmentTypeService()
equipment_usage_service = EquipmentUsageService()
masters_service = MasterService()
repairment_service = RepairmentService()
suppliers_service = SupplierService()
equipment_reservation_service = EquipmentReservationService()
