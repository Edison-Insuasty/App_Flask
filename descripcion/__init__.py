from flask import Blueprint

descripcion = Blueprint('descripcion', __name__, template_folder='templates')

from . import routes