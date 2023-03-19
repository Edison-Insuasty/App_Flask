from flask import Flask, render_template, request, redirect, url_for, session, flash
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from administrador import *
from werkzeug.utils import secure_filename 
from datetime import date, datetime, time
from babel import numbers, dates
import random
from . import carritoc
from index import *
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

#Agregar al carrito de compras un producto
@carritoc.route("/addToCart")
def addToCart():
    if 'conectado' in session:
        idpro = int(request.args.get('idpro'))
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (session['cedula'], ))
            cedula = cur.fetchone()[0]
            # Buscar si el producto ya está en el carrito del usuario
            cur.execute("SELECT cantidad FROM carrito WHERE cedula = %s AND id = %s  ", (cedula, idpro ))
            result = cur.fetchone()
            if result: 
                cantidad = result[0] + 1
                cur.execute("UPDATE carrito SET cantidad = %s WHERE cedula = %s AND id = %s", (cantidad, cedula, idpro ))
            else:           
                cur.execute("INSERT INTO carrito (cedula, id, cantidad) VALUES (%s, %s, %s)", (cedula, idpro, 1))                
                
            conn.commit()                
            
        conn.close()

        if idpro < 100:
            return redirect(url_for('menu.menu'))
        else:
            return redirect(url_for('ofertas.archivos'))
    else:
        return redirect(url_for('reg'))

#Ver el carrito de compras y los productos en el
@carritoc.route("/cart")
def cart():

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
    
    carrito = gettext('CARRITO')
    carrito1 = gettext('CARRITO DE COMPRAS')
    imagen = gettext('IMAGEN')
    cantidad1 = gettext('CANTIDAD')
    valor = gettext('VALOR UNITARIO')
    valor1 = gettext('VALOR TOTAL')
    descartar = gettext('Descartar')
    subtotal = gettext('Subtotal')
    pagar = gettext('PAGAR')
    vaciar = gettext('VACIAR CARRITO')
    seguir = gettext('SEGUIR COMPRANDO')

    results14 = {'carrito':carrito,'carrito1':carrito1,'imagen':imagen,'cantidad1':cantidad1,
                'valor':valor,'valor1':valor1,'descartar':descartar,'subtotal':subtotal,
                'pagar':pagar,'vaciar':vaciar,'seguir':seguir}

    if 'conectado' in session:
        cedula = session['cedula']
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (cedula, ))
            cedula = cur.fetchone()[0]
            cur.execute("SELECT productos.idpro, productos.nompro, productos.precio, productos.imagen, carrito.cantidad, productos.precio*carrito.cantidad AS valor FROM productos, carrito WHERE productos.idpro = carrito.id AND carrito.cedula = %s", (cedula, ))
            productos = cur.fetchall()        
            conn.commit()
        totalPrice = 0
        for row in productos:
            totalPrice += row[2] * row[4]        
        return render_template("cart.html", productos = productos, totalPrice=totalPrice, dataLogin = dataLoginSesion(),results5=results5,results14=results14)
    else:
        return redirect(url_for('reg'))
    
#Imprimir la factura de compra 
@carritoc.route("/checkout")
def checkout():

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
    
    pago = gettext('PAGO')
    factura = gettext('FACTURA DE COMPRA')
    cantidad = gettext('Cantidad')
    descripcion2 = gettext('Descripción')
    precio1 = gettext('Precio Unitario')
    importe = gettext('Importe')
    total = gettext('Total')
    condiciones = gettext('Condiciones y formas de pago')
    pago1 = gettext('El pago se debe realizar en el momento de entrega del producto')
    banco = gettext('Banco Davivienda')
    pago2 = gettext('Pago contraentrega')
    aceptar = gettext('ACEPTAR')

    results13 = {'pago':pago,'factura':factura,'parrilla1':parrilla1,'carrera':carrera,'barrio':barrio,
                'cantidad':cantidad,'descripcion2':descripcion2,'precio1':precio1,'importe':importe,
                'total':total,'condiciones':condiciones,'pago1':pago1,'banco':banco,'pago2':pago2,
                'aceptar':aceptar}

    b = dates.format_datetime(datetime.now(), locale=request.accept_languages.best_match(['en', 'es', 'de', 'fr']))
    result = {'us_date': b}
    cedula = session['cedula']
    with connectionBD() as conn:
        cur = conn.cursor()
        cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (cedula, ))
        cedula = cur.fetchone()[0]
        cur.execute("SELECT productos.idpro, productos.nompro, productos.precio, productos.imagen, carrito.cantidad, productos.precio*carrito.cantidad AS valor FROM productos, carrito WHERE productos.idpro = carrito.id AND carrito.cedula = %s", (cedula, ))
        productos = cur.fetchall()    
        conn.commit()
    numero_aleatorio = random.randint(100000, 500000)
   
    totalPrice = 0
    for row in productos:
        totalPrice += row[2] * row[4] 
    return render_template("checkout.html", productos = productos, numero_aleatorio=numero_aleatorio, totalPrice=totalPrice, result=result, dataLogin = dataLoginSesion(),results5=results5,results13=results13)
    
#eliminar un producto del carrito de compras
@carritoc.route("/removeFromCart")
def removeFromCart():

    if 'conectado' in session:
        cedula = session['cedula']
        productId = int(request.args.get('productId'))
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (cedula, ))
            cedula = cur.fetchone()[0]
            try:
                # Buscar si el producto ya está en el carrito del usuario
                cur.execute("SELECT cantidad FROM carrito WHERE cedula = %s AND id = %s AND cantidad > 0", (cedula, productId))
                result = cur.fetchone()
                if result:           
                    cur.execute("UPDATE carrito SET cantidad = cantidad - 1 WHERE cedula = %s AND id = %s AND cantidad > 0", (cedula, productId))
                    conn.commit()             
                else:
                    cur.execute("DELETE FROM carrito WHERE cedula = %s AND id = %s", (cedula, productId))
            except:
                conn.rollback()
                abort(400)
        conn.close()
        return redirect(url_for("carritoc.cart"))
    else:           
        return redirect(url_for("reg"))

#aumentar de uno en uno la cantidad de productos en el carrito
@carritoc.route("/aumentaFromCart")
def aumentaFromCart():

    if 'conectado' in session:
        cedula = session['cedula']
        productId = int(request.args.get('productId'))
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (cedula, ))
            userId = cur.fetchone()[0]
            try:
                # Buscar si el producto ya está en el carrito del usuario
                cur.execute("SELECT cantidad FROM carrito WHERE cedula = %s AND id = %s AND cantidad > 0", (cedula, productId))
                result = cur.fetchone()
                if result:                    
                    cur.execute("UPDATE carrito SET cantidad = cantidad + 1 WHERE cedula = %s AND id = %s AND cantidad > 0", (cedula, productId)) 
                    conn.commit()              
                else:
                    cur.execute("DELETE FROM carrito WHERE cedula = %s AND id = %s", (cedula, productId))
            except:
                conn.rollback()
                abort(400)
        conn.close()
        return redirect(url_for("carritoc.cart"))
    else:           
        return redirect(url_for("reg"))

#reducir de uno en uno la cantidad de productos en el carrito
@carritoc.route("/eliminaFromCart")
def eliminaFromCart():

    if 'conectado' in session:
        cedula = session['cedula']
        productId = int(request.args.get('productId'))
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (cedula, ))
            cedula = cur.fetchone()[0]
       
            cur.execute("DELETE FROM carrito WHERE cedula = %s AND id = %s", (cedula, productId))
            conn.commit()

        conn.close()
        return redirect(url_for("carritoc.cart"))
    else:           
        return redirect(url_for("reg"))

#Vaciar el carrito de compras
@carritoc.route("/elimina2")
def elimina2():

    cedula = session['cedula']
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)
    cur.execute("DELETE FROM carrito WHERE cedula = %s", (cedula, ))
    conexion_MySQLdb.commit()
    cur.close() 
    return redirect(url_for('carritoc.cart'))