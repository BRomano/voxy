from flask import Blueprint

wordcounting_bp = Blueprint('wordcounting', __name__)
from voxy.wordcounting import routes  # noqa: E402,F401
