from . import contacto
from flask import render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from index import *
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

@contacto.route('/contacto')
def contacto():

    inicio = gettext('INICIO')
    menu1 = gettext('MENU')
    descripcion1 = gettext('DESCRIPCIÓN')
    promociones = gettext('PROMOCIONES')
    contacto1 = gettext('CONTACTO')
    salir = gettext('SALIR')
    direccion1 = gettext('Dirección')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')

    results5 = {'inicio':inicio,'menu1':menu1,'descripcion1':descripcion1,'promociones':promociones,
                'contacto1':contacto1,'salir':salir, 'direccion1':direccion1,'carrera':carrera,
                'barrio':barrio,'redes':redes,'parrilla1':parrilla1,'tenemos':tenemos}

    correo = gettext('Correo')
    telefono = gettext('Teléfono')

    results11 = {'contacto1':contacto1,'correo':correo,'telefono':telefono}

    if 'conectado' in session:
        return render_template('contacto.html', dataLogin = dataLoginSesion(),results5=results5,results11=results11)
    else:
        return abort(401)