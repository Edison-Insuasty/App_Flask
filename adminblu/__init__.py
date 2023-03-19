from flask import Blueprint

adminblu = Blueprint('adminblu', __name__, template_folder='templates')

from . import routes