from flask import Blueprint

from .post import post_blueprint
from .comment import comment_blueprint


api_blueprint = Blueprint("api", __name__, url_prefix="/api")

api_blueprint.register_blueprint(post_blueprint)
api_blueprint.register_blueprint(comment_blueprint)
