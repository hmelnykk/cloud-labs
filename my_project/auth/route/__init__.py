"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    # Import your Blueprint routes for the tables
    from .orders.equipment_reservation_route import equipment_reservation_bp
    from .orders.projects_route import projects_bp
    from .orders.equipment_item_route import equipment_item_bp
    from .orders.equipment_route import equipment_bp
    from .orders.suppliers_route import suppliers_bp
    from .orders.masters_route import masters_bp
    from .orders.equipment_type_route import equipment_type_bp
    from .orders.repairment_route import repairment_bp
    from .orders.student_route import student_bp
    from .orders.equipment_usage_route import equipment_usage_bp

    # Register all Blueprints
    app.register_blueprint(equipment_reservation_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(equipment_item_bp)
    app.register_blueprint(equipment_bp)
    app.register_blueprint(suppliers_bp)
    app.register_blueprint(masters_bp)
    app.register_blueprint(equipment_type_bp)
    app.register_blueprint(repairment_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(equipment_usage_bp)
