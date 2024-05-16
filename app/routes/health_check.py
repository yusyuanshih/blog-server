from flask import Blueprint

health_check_blueprint = Blueprint("health-check", __name__, url_prefix="/health-check")


@health_check_blueprint.route("/", methods=["GET"])
def health_check():
    return "OK", 200
