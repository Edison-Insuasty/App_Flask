from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from administrador import *
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from . import adminblu
from index import *
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

#listando los productos con paginacion
@adminblu.route('/admin', methods=['GET','POST'])
def inicio():
  
    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    descripcion1 = gettext('DESCRIPCIÓN')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    descartar = gettext('Descartar')
    no1 = gettext('NO HAY MAS ELEMENTOS')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    if 'conectado' in session:
        return render_template('public/layout.html', miData = listaProductos(), dataLogin = dataLoginSesion(),results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
    else:
        return abort(401)

@adminblu.route("/page/<number_page>")
def page(number_page):
  
    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    descripcion1 = gettext('DESCRIPCIÓN')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    descartar = gettext('Descartar')
    no1 = gettext('NO HAY MAS ELEMENTOS')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)
    if number_page == '1':
        cursor.execute("SELECT * FROM productos LIMIT 0,10")
    if number_page == '2':
        cursor.execute("SELECT * FROM productos LIMIT 10,10")
    if number_page == '3':
        cursor.execute("SELECT * FROM productos LIMIT 20,10")
    if number_page == '4':
        cursor.execute("SELECT * FROM productos LIMIT 30,10")
    if number_page == '5':
        cursor.execute("SELECT * FROM productos LIMIT 40,10")
    if number_page == '6':
        cursor.execute("SELECT * FROM productos LIMIT 50,10")
    if number_page == '7':
        cursor.execute("SELECT * FROM productos LIMIT 60,10")
    if number_page == '8':
        cursor.execute("SELECT * FROM productos LIMIT 70,10")
    if number_page == '9':
        cursor.execute("SELECT * FROM productos LIMIT 80,10")
    if number_page == '10':
        cursor.execute("SELECT * FROM productos LIMIT 90,10")
    
    miData = cursor.fetchall()
    conn.commit()
    return render_template('public/layout.html', miData=miData,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)

#ver la descripcion de los productos sea de menu o promociones
@adminblu.route("/productDescription")
def productDescription():

    menu1 = gettext('MENU')
    detalles = gettext('DETALLES')
    promo = gettext('Promo')
    agregar1 = gettext('AGREGAR AL CARRO')
    ir = gettext('IR A MENU')
    ir1 = gettext('IR A PROMOCIÓNES')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')

    results6 = {'menu1':menu1,'detalles':detalles,'promo':promo,'nombre':nombre,'precio':precio,
                'descripcion2':descripcion2,'agregar1':agregar1,'ir': ir,'ir1':ir1}

    inicio = gettext('INICIO')
    menu1 = gettext('MENU')
    descripcion1 = gettext('DESCRIPCIÓN')
    promociones = gettext('PROMOCIONES')
    contacto1 = gettext('CONTACTO')
    direccion1 = gettext('Dirección')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')
    salir = gettext('SALIR')

    results5 = {'inicio':inicio,'menu1':menu1,'descripcion1':descripcion1,'promociones':promociones,
                'contacto1':contacto1,'salir':salir, 'direccion1':direccion1,'carrera':carrera,
                'barrio':barrio,'redes':redes,'parrilla1':parrilla1,'tenemos':tenemos}

    idpro = request.args.get('idpro')
    with connectionBD() as conn:
        cur = conn.cursor()      
        cur.execute("SELECT idpro, nompro, descripcion, imagen, precio FROM productos WHERE idpro =%s", (idpro,))
        productData = cur.fetchone()
    conn.close()  
    return render_template("productDescription.html", data=productData, dataLogin = dataLoginSesion(),results6=results6,results5=results5)
            
#Actualizar un producto dentro de la tabla productos
@adminblu.route('/form-update/<string:idpro>', methods=['GET','POST'])
def formViewUpdate(idpro):

    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    descripcion1 = gettext('DESCRIPCIÓN')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    descartar = gettext('Descartar')
    no1 = gettext('NO HAY MAS ELEMENTOS')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    if request.method == 'GET':
        resultData = updateProducto(idpro)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData,results2=results2,results15=results15,results17=results17)
        else:
            return render_template('public/layout.html', miData = listaProductos(), msg='No existe el producto', tipo= 1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
    else:
        return render_template('public/layout.html', miData = listaProductos(), msg = 'Metodo HTTP incorrecto', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)         
   
#Ver los detalles de un producto dentro de la tabla productos
@adminblu.route('/ver-detalles/<int:idpro>', methods=['GET', 'POST'])
def viewDetalleCarro(idpro):

    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    descripcion1 = gettext('DESCRIPCIÓN')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    descartar = gettext('Descartar')
    no1 = gettext('NO HAY MAS ELEMENTOS')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    if request.method == 'GET':
        resultData = detallesdelProducto(idpro) #Funcion que almacena los detalles del producto
        if resultData:
            return render_template('public/acciones/view.html', infoCarro = resultData, msg='Detalles del Producto', tipo=1,results2=results2,results15=results15,results16=results16)
        else:
            return render_template('public/acciones/layout.html', msg='No existe el Producto', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
    return redirect(url_for('adminblu.inicio'))
    
#actualzar un producto
@adminblu.route('/actualizar/idpro>', methods=['POST'])
def  formActualizarCarro(idpro):

    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    descripcion1 = gettext('DESCRIPCIÓN')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    descartar = gettext('Descartar')
    no1 = gettext('NO HAY MAS ELEMENTOS')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    if request.method == 'POST':
        idpro = request.form['idpro']
        nompro           = request.form['nompro']
        descripcion          = request.form['descripcion']
        precio            = request.form['precio']

        #Script para recibir el archivo (foto)
        if(request.files['imagen']):
            file     = request.files['imagen']
            fotoForm = recibeFoto(file)
            resultData = recibeActualizarProducto(nompro, descripcion, precio, fotoForm, idpro)
        else:
            fotoproducto  ='error.jpg'
            resultData = recibeActualizarProducto(nompro, descripcion, precio, fotoproducto, idpro)

        if(resultData ==1):
            return render_template('public/layout.html', miData = listaProductos(), msg='Datos del producto actualizados', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
        else:
            return render_template('public/layout.html', miData = listaProductos(), msg='No se pudo actualizar', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
        
#Link para registrar un nueco producto
@adminblu.route('/registrar-producto', methods=['GET','POST'])
def addCarro():

    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')
    registrar1 = gettext('Registrar Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio2 = gettext('PRECIO')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    return render_template('public/acciones/add.html',results2=results2,results15=results15,results19=results19)

#Registrando nuevo producto
@adminblu.route('/carro', methods=['POST'])
def formAddCarro():

    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}

    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    descripcion1 = gettext('DESCRIPCIÓN')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    nombre = gettext('Nombre')
    descripcion2 = gettext('Descripción')
    precio = gettext('Precio')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    descartar = gettext('Descartar')
    no1 = gettext('NO HAY MAS ELEMENTOS')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}
    
    if request.method == 'POST':
        idpro               = request.form['idpro']
        nompro              = request.form['nompro']
        descripcion         = request.form['descripcion']
        precio              = request.form['precio']       
        if(request.files['imagen'] !=''):
            file     = request.files['imagen'] #recibiendo el archivo
            nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
            resultData = registrarProducto(idpro, nompro, descripcion, precio, nuevoNombreFile)
            if(resultData ==1):
                return render_template('public/layout.html', miData = listaProductos(), msg='El Registro fue un éxito', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
            else:
                return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)   
        else:
            return render_template('public/layout.html', msg = 'Debe cargar una foto', tipo=1,results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)
           
#Elimina un producto de la tabla productos
@adminblu.route("/elimina")
def elimina():

        productId = int(request.args.get('idpro'))
        with connectionBD() as conn:
            cur = conn.cursor()

            cur.execute("DELETE FROM productos WHERE idpro = %s", (productId, ))
            conn.commit()

        conn.close()
        
        return redirect(url_for('adminblu.inicio'))

#procesar una foto
def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
    upload_path = os.path.join (basepath, '../static/img', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile