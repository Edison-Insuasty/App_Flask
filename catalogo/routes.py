from flask import Flask, render_template, request, redirect, url_for, jsonify
from administrador import *
from . import menu
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from flask import *
from werkzeug.utils import secure_filename
from index import *
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

@menu.route('/menu')
def menu():

    direccion1 = gettext('Dirección')
    salir = gettext('SALIR')
    inicio = gettext('INICIO')
    menu1 = gettext('MENU')
    descripcion1 = gettext('DESCRIPCIÓN')
    promociones = gettext('PROMOCIONES')
    contacto1 = gettext('CONTACTO')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')

    results5 = {'inicio':inicio,'menu1':menu1,'descripcion1':descripcion1,'promociones':promociones,
                'contacto1':contacto1,'salir':salir, 'direccion1':direccion1,'carrera':carrera,
                'barrio':barrio,'redes':redes,'parrilla1':parrilla1,'tenemos':tenemos}

    detalles = gettext('DETALLES')
    promo = gettext('Promo')
    nombre = gettext('Nombre')
    precio = gettext('Precio')
    descripcion2 = gettext('Descripción')
    agregar1 = gettext('AGREGAR AL CARRO')
    ir = gettext('IR A MENU')
    ir1 = gettext('IR A PROMOCIÓNES')

    results6 = {'menu1':menu1,'detalles':detalles,'promo':promo,'nombre':nombre,'precio':precio,
                'descripcion2':descripcion2,'agregar1':agregar1,'ir': ir,'ir1':ir1}

    date = gettext('DATE EL GUSTO DE PROBAR EL DELICIOSO SAZON EN PARRILLA DEL SUR') 
    nuestros = gettext('NUESTROS PRODUCTOS')

    results12 = {'menu1':menu1,'date':date,'nuestros':nuestros}

    if 'conectado' in session:
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT idpro, nompro, descripcion, imagen, precio FROM productos WHERE  idpro < 100 ORDER BY idpro ASC")
            itemData = cur.fetchall()
            itemData = parse(itemData)   
        return render_template('menu.html', itemData=itemData, dataLogin = dataLoginSesion(),results5=results5, results6=results6,results12=results12)
    else:
        return abort(401)