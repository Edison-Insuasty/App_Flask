from flask import Flask, render_template, request, redirect, url_for, jsonify
from administrador import *
from flask import *
import os
from werkzeug.utils import secure_filename 
from . import ofertas
from os import listdir
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from index import *
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

@ofertas.route('/ofertas')
def archivos():

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

    descripcion3 = gettext('DESCRIPCIÓN PROMOCIÓN')
    detalles = gettext('DETALLES')
    promo = gettext('Promo')
    nombre = gettext('Nombre')
    precio = gettext('Precio')
    descripcion2 = gettext('Descripción')
    agregar1 = gettext('AGREGAR AL CARRO')

    results8 = {'descripcion3':descripcion3,'detalles':detalles,'promo':promo,'nombre':nombre,'precio':precio,
                'descripcion2':descripcion2,'agregar1':agregar1}

    archivos = gettext('Archivos')

    results9 = {'archivos':archivos,'promociones':promociones}


    if 'conectado' in session:
        with connectionBD() as conn:
            cur = conn.cursor()

            cur.execute("SELECT idpro, nompro, descripcion, imagen, precio FROM productos WHERE  idpro > 100 ORDER BY idpro ASC")
            itemData1 = cur.fetchall()
            itemData1 = parse(itemData1)

        return render_template('archivos.html',  itemData1=itemData1, dataLogin = dataLoginSesion(),results5=results5,results8=results8,results9=results9)
    else:
        return abort(401)