from flask import Blueprint

ofertas = Blueprint('ofertas', __name__, template_folder='templates')

from . import routes