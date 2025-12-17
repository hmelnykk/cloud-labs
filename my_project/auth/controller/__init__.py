"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import the specific controllers for each table
from .orders.student_controller import StudentController
from .orders.projects_controller import ProjectsController
from .orders.equipment_controller import EquipmentController
from .orders.equipment_item_controller import EquipmentItemController
from .orders.equipment_type_controller import EquipmentTypeController
from .orders.equipment_usage_controller import EquipmentUsageController
from .orders.masters_controller import MastersController
from .orders.repairment_controller import RepairmentController
from .orders.suppliers_controller import SuppliersController
from .orders.equipment_reservation_controller import EquipmentReservationController

# Initialize the controllers
student_controller = StudentController()
project_controller = ProjectsController()
equipment_controller = EquipmentController()
equipment_item_controller = EquipmentItemController()
equipment_type_controller = EquipmentTypeController()
equipment_usage_controller = EquipmentUsageController()
masters_controller = MastersController()
repairment_controller = RepairmentController()
suppliers_controller = SuppliersController()
equipment_reservation_controller = EquipmentReservationController()
