from flask import session
from conexionBD import * 

def dataLoginSesion():
    inforLogin = {
        "cedula"              :session['cedula'],
        "nombres"             :session['nombres'],
        "apellidos"           :session['apellidos'],
        "correo"              :session['correo'],
        "direccion"           :session['direccion'],
        "telefono"            :session['telefono'],
        "credencial"          :session['credencial']
    }
    return inforLogin

def dataPerfilUsuario():
    conexion_MySQLdb = connectionBD() 
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    cedula         = session['cedula']
    
    querySQL  = ("SELECT * FROM usuarios WHERE cedula='%s'" % (cedula,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return datosUsuario