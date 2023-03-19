from flask import Blueprint

menu = Blueprint('menu', __name__, template_folder='templates')

from . import routes