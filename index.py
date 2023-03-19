from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, abort
from catalogo import menu
from contacto import contacto
from descripcion import descripcion
from ofertas import ofertas
from carrito import carritoc
from adminblu import adminblu
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from werkzeug.security import generate_password_hash, check_password_hash
from administrador import *
from werkzeug.utils import secure_filename 
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

app = Flask(__name__)
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

sentry_sdk.init(
    dsn="https://47b422c23c014fec8d53ccc9dc0e3e61@o4504709798952960.ingest.sentry.io/4504709801443328",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)

app.config['BABEL_DEFAULT_LOCALE'] = 'es'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'fr'])

babel = Babel(app, locale_selector=get_locale)

app.register_blueprint(menu)
app.register_blueprint(contacto)
app.register_blueprint(descripcion)
app.register_blueprint(ofertas)
app.register_blueprint(carritoc)
app.register_blueprint(adminblu)

error_codes = [
    400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
    416, 417, 418, 422, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505
]
for code in error_codes:
    @app.errorhandler(code)
    def client_error(error):

        error2 = gettext('Error')
        solicitud = gettext('Solicitud incorrecta')
        regresar = gettext('REGRESAR')

        results = {'error2':error2,'solicitud': solicitud,'regresar': regresar}

        return render_template('error1.html', error=error, results=results), error.code

#inicio de sesion
@app.route('/sesion', methods=['GET', 'POST'])
def loginUser():
    conexion_MySQLdb = connectionBD()

    inicio = gettext('INICIO')
    quienes = gettext('QUIENES SOMOS')
    parrilla = gettext('PARRILLA IPIALEÑA: Somos una empresa comprometidos con garantizar satisfacción a nuestros clientes, nuestros productos se caracterizan por contar con alta calidad y eficiencia en la prestación del servicio')
    cocinero = gettext('COCINERO')
    cocinero1 = gettext('Un cocinero no puede, él sólo, gobernar su reino. Está necesitado de colaboradores que entiendan lo que se propone, cuál es su visión del mundo. Es con todos ellos, con su energía, saber hacer y esmero, como el proyecto deja de serlo para concentrarse en la realidad')
    da = gettext('DA LO MEJOR DE TI')
    cocinero2 = gettext('El cocinero no es una persona aislada, que vive y trabaja sólo para dar de comer a sus huéspedes. Un cocinero se convierte en artista cuando tiene cosas que decir a través de sus platos, como un pintor en un cuadro')

    results1 = {'inicio':inicio,'quienes': quienes,'parrilla': parrilla,'cocinero': cocinero,
                'cocinero1': cocinero1,'da': da,'cocinero2': cocinero2}
    
    salir = gettext('SALIR')
    gestion = gettext('GESTION DE PRODUCTOS')
    agregar = gettext('AGREGAR NUEVO PRODUCTO A LA PARRILLA')

    results2 = {'salir': salir,'gestion':gestion,'agregar':agregar}
    
    direccion1 = gettext('Dirección')
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
    
    felicitaciones = gettext('Felicitaciones')
    excelente = gettext('EXCELENTE')

    results15 = {'felicitaciones':felicitaciones,'excelente':excelente}

    registrar1 = gettext('Registrar Carro')
    detalles1 = gettext('DETALLES DEL PRODUCTO')
    detalles2 = gettext('DE LA PARRILLA IPIALEÑA')
    nombre1 = gettext('NOMBRE')
    foto = gettext('FOTO')
    precio2 = gettext('PRECIO')
    no = gettext('No existe el carrito')

    results16 = {'registrar1':registrar1,'detalles1':detalles1,'detalles2':detalles2,'nombre1':nombre1,
                'descripcion1':descripcion1,'foto':foto,'precio2':precio2,'no':no}

    actualizar = gettext('Actualizar Información del Carro')
    cambiar = gettext('Cambiar Foto del producto')
    guardar = gettext('Guardar Actualización')
    noo = gettext('No existe el Coche')
    nombre = gettext('Nombre')
    precio = gettext('Precio')
    descripcion2 = gettext('Descripción')

    results17 = {'registrar1':registrar1,'actualizar':actualizar,'nombre':nombre,
                'descripcion2':descripcion2,'precio':precio,'cambiar':cambiar,'guardar':guardar,'noo':noo}

    foto1 = gettext('Foto')
    acciones = gettext('ACCIONES')
    ver = gettext('Ver')
    actualizar1 = gettext('Actualizar')
    no1 = gettext('NO HAY MAS ELEMENTOS')
    descartar = gettext('Descartar')

    results18 = {'nombre':nombre,'descripcion2':descripcion2,'foto1':foto1,'precio':precio,
                'acciones':acciones,'ver':ver,'actualizar1':actualizar1,'descartar':descartar,'no1':no1}

    registrar2 = gettext('Registrar Nuevo Producto')
    foto2 = gettext('Foto del Producto')
    guardar1 = gettext('Guardar Registro')

    results19 = {'registrar1':registrar1,'registrar2':registrar2,'nombre':nombre,'descripcion2':descripcion2,
                'precio2':precio2,'foto2':foto2,'guardar1':guardar1}

    if 'conectado' in session:
        if(session['credencial'] == '___' ):
            return render_template('inicio.html', dataLogin = dataLoginSesion(),results1=results1,results5=results5)
        elif(session['credencial'] == '123' ):
            return render_template('public/layout.html',  miData = listaProductos(), dataLogin = dataLoginSesion(),results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)  
                       
    else:
        if request.method == 'POST' and 'cedula' in request.form and 'password' in request.form:
            cedula   = str(request.form['cedula'])
            password   = str(request.form['password'])

            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE cedula = %s", [cedula])
            account = cursor.fetchone()

            if account:
                if check_password_hash(account['password'],password):
                    # Crear datos de sesión, para poder acceder a estos datos en otras rutas 
                    session['conectado']        = True
                    session['cedula']           = account['cedula']
                    session['nombres']          = account['nombres']
                    session['apellidos']        = account['apellidos']
                    session['correo']           = account['correo']
                    session['direccion']        = account['direccion']
                    session['telefono']         = account['telefono']
                    session['credencial']       = account['credencial']

                    if(session['credencial'] == '___' ):
                        return render_template('inicio.html',typeAlert=1, dataLogin = dataLoginSesion(),results1=results1,results5=results5)
                    elif(session['credencial'] == '123' ):
                        return render_template('public/layout.html',  miData = listaProductos(), dataLogin = dataLoginSesion(),results2=results2,results15=results15,results16=results16,results17=results17,results18=results18,results19=results19)        
                else:
                    abort(401)
            else:
                return abort(401)
        return abort(400)

#Registrando una cuenta de Usuario
@app.route('/registro', methods=['GET', 'POST'])
def registerUser():
    conexion_MySQLdb = connectionBD()

    cedula1 = gettext('Cedula')
    contraseña = gettext('Contraseña')
    iniciar = gettext('Iniciar Sesión')
    registrar = gettext('Registrar')
    direccion1 = gettext('Dirección')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')

    results3 = {'cedula1':cedula1,'contraseña':contraseña,'iniciar':iniciar,'registrar':registrar}

    results7 = {'direccion1':direccion1,'carrera':carrera,'barrio':barrio,'redes':redes,
            'parrilla1':parrilla1,'tenemos':tenemos}

    if request.method == 'POST':
        cedula          = request.form['cedula']
        nombres         = request.form['nombres']
        apellidos       = request.form['apellidos']
        correo          = request.form['correo']
        direccion       = request.form['direccion']
        telefono        = request.form['telefono']
        password        = request.form['password']
        repite_password = request.form['repite_password']
        credencial      = request.form['credencial']

        # Comprobando si ya existe la cuenta de Usuario con respecto al email
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE cedula = %s', (cedula,))
        account = cursor.fetchone()
        cursor.close() #cerrrando conexion SQL
          
        if account:
            #'Ya existe un usuario con esta cedula!'
            abort(400)
        elif password != repite_password:
            #'Disculpa, las clave no coinciden!'
            abort(401)
        elif not cedula or not password or not password or not repite_password:
            #'El formulario no debe estar vacio!'
            abort(400)
        elif (credencial != '123' and credencial != '___'):
            #'credenciales incorrectas!'
            abort(401)
        else:
            # La cuenta no existe y los datos del formulario son válidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion_MySQLdb = connectionBD()
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute('INSERT INTO usuarios (cedula,nombres,apellidos,correo,direccion,telefono,credencial,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (cedula, nombres, apellidos, correo, direccion, telefono, credencial, password_encriptada))
            conexion_MySQLdb.commit()
            cursor.close()

        return render_template('login.html', typeAlert=1, results3=results3,results7=results7)
    
    return render_template('login.html', dataLogin = dataLoginSesion(), typeAlert=0, results3=results3,results7=results7)

@app.route('/')
def principal():

    cedula1 = gettext('Cedula')
    contraseña = gettext('Contraseña')
    iniciar = gettext('Iniciar Sesión')
    registrar = gettext('Registrar')
    direccion1 = gettext('Dirección')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')

    results3 = {'cedula1':cedula1,'contraseña':contraseña,'iniciar':iniciar,'registrar':registrar}

    results7 = {'direccion1':direccion1,'carrera':carrera,'barrio':barrio,'redes':redes,
            'parrilla1':parrilla1,'tenemos':tenemos}
    
    return render_template('login.html',results3=results3,results7=results7)

@app.route('/reg')
def reg():

    registro = gettext('Registro')
    nombres = gettext('Nombres')
    apellidos = gettext('Apellidos')
    correo = gettext('Correo')
    direccion1 = gettext('Dirección')
    telefono = gettext('Teléfono')
    contraseña1 = gettext('Confirme Contraseña')
    credencial = gettext('Credencial')
    volver = gettext('Volver')
    cedula1 = gettext('Cedula')
    contraseña = gettext('Contraseña')
    registrar = gettext('Registrar')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')


    results4 = {'registro':registro,'cedula1':cedula1,'nombres':nombres,'apellidos':apellidos,
                'correo':correo,'direccion1':direccion1,'telefono':telefono,'contraseña':contraseña,
                'contraseña1': contraseña1,'credencial':credencial,'registrar':registrar,'volver':volver}
    
    results7 = {'direccion1':direccion1,'carrera':carrera,'barrio':barrio,'redes':redes,
            'parrilla1':parrilla1,'tenemos':tenemos}

    return render_template('registro.html',results4=results4,results7=results7)

#Iniciando sesion
@app.route('/login')
def login():

    inicio = gettext('INICIO')
    quienes = gettext('QUIENES SOMOS')
    parrilla = gettext('PARRILLA IPIALEÑA: Somos una empresa comprometidos con garantizar satisfacción a nuestros clientes, nuestros productos se caracterizan por contar con alta calidad y eficiencia en la prestación del servicio')
    cocinero = gettext('COCINERO')
    cocinero1 = gettext('Un cocinero no puede, él sólo, gobernar su reino. Está necesitado de colaboradores que entiendan lo que se propone, cuál es su visión del mundo. Es con todos ellos, con su energía, saber hacer y esmero, como el proyecto deja de serlo para concentrarse en la realidad')
    da = gettext('DA LO MEJOR DE TI')
    cocinero2 = gettext('El cocinero no es una persona aislada, que vive y trabaja sólo para dar de comer a sus huéspedes. Un cocinero se convierte en artista cuando tiene cosas que decir a través de sus platos, como un pintor en un cuadro')

    results1 = {'inicio':inicio,'quienes': quienes,'parrilla': parrilla,'cocinero': cocinero,
                'cocinero1': cocinero1,'da': da,'cocinero2': cocinero2}
    
    menu1 = gettext('MENU')
    descripcion1 = gettext('DESCRIPCIÓN')
    promociones = gettext('PROMOCIONES')
    contacto1 = gettext('CONTACTO')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')
    salir = gettext('SALIR')
    direccion1 = gettext('Dirección')

    results5 = {'inicio':inicio,'menu1':menu1,'descripcion1':descripcion1,'promociones':promociones,
                'contacto1':contacto1,'salir':salir, 'direccion1':direccion1,'carrera':carrera,
                'barrio':barrio,'redes':redes,'parrilla1':parrilla1,'tenemos':tenemos}
    
    cedula1 = gettext('Cedula')
    contraseña = gettext('Contraseña')
    iniciar = gettext('Iniciar Sesión')
    registrar = gettext('Registrar')

    results3 = {'cedula1':cedula1,'contraseña':contraseña,'iniciar':iniciar,'registrar':registrar}

    results7 = {'direccion1':direccion1,'carrera':carrera,'barrio':barrio,'redes':redes,
            'parrilla1':parrilla1,'tenemos':tenemos}

    if 'conectado' in session:
        cedula = session['cedula']
        with connectionBD() as conn:
            cur = conn.cursor()
            cur.execute("SELECT cedula FROM usuarios WHERE cedula = %s", (cedula, ))
            userId = cur.fetchone()[0]
            cur.execute("SELECT productos.idpro, productos.nompro, productos.precio, productos.imagen, carrito.cantidad FROM productos, carrito WHERE productos.idpro = carrito.id AND carrito.cedula = %s", (cedula, ))
            productos = cur.fetchall()
        return render_template('inicio.html', dataLogin = dataLoginSesion(),productos=productos,results1=results1,results5=results5)
    else:
        return render_template('login.html',results3=results3,results7=results7)

#Cerrar sesion y vaciar carro
@app.route('/logout')
def logout():

    cedula1 = gettext('Cedula')
    contraseña = gettext('Contraseña')
    iniciar = gettext('Iniciar Sesión')
    registrar = gettext('Registrar')
    direccion1 = gettext('Dirección')
    carrera = gettext('CARRERA')
    barrio = gettext('BARRIO SANTIAGO - IPIALES')
    redes = gettext('Nuestras Redes')
    parrilla1 = gettext('PARRILA IPIALEÑA')
    tenemos = gettext('Tenemos mas de 10 años de experciencia en la elaboración de nuestros productos, danos el gusto de atenderte')

    results3 = {'cedula1':cedula1,'contraseña':contraseña,'iniciar':iniciar,'registrar':registrar}

    results7 = {'direccion1':direccion1,'carrera':carrera,'barrio':barrio,'redes':redes,
            'parrilla1':parrilla1,'tenemos':tenemos}
    
    if 'conectado' in session:
        cedula = session['cedula']
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("DELETE FROM carrito WHERE cedula = %s", (cedula, ))
 
        conexion_MySQLdb.commit()
        cur.close()
        # Eliminar datos de sesión, esto cerrará la sesión del usuario
        session.pop('conectado', None)
        session.pop('cedula', None)
        session.pop('nombres', None)
        session.pop('apellidos', None)
        session.pop('correo', None)
        session.pop('direccion', None)
        session.pop('telefono', None)
        session.pop('credencial', None)
    
        return render_template('login.html',results3=results3,results7=results7)
    else:
        return render_template('login.html',results3=results3,results7=results7)
    
if __name__ == '__main__':
    app.run(debug=True, port=5018)