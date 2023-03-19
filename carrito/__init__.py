from flask import Blueprint

carritoc = Blueprint('carritoc', __name__, template_folder='templates')

from . import routes