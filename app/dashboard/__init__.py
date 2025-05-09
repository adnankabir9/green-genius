# Example for app/auth/__init__.py
# Repeat similar pattern for other blueprints
from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

from app.dashboard import routes