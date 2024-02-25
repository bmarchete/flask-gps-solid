from flask import Blueprint

from adapters.api.handlers.routes_handler import get_travel_distance

routes_bp = Blueprint("routes", __name__, url_prefix="/routes")

routes_bp.add_url_rule("distance", methods=["GET"], view_func=get_travel_distance)
