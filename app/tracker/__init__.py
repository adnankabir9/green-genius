# Example for app/auth/__init__.py
# Repeat similar pattern for other blueprints
from flask import Blueprint

tracker = Blueprint('tracker', __name__)

from app.tracker import routes