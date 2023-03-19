from random import sample
from conexionBD import *  #Importando conexion BD

def parse(data):
    ans = []
    i = 0
    while i < len(data):
        curr = []
        for j in range(7):
            if i >= len(data):
                break
            curr.append(data[i])
            i += 1
        ans.append(curr)
    return ans
#Creando una funcion para obtener la lista de carros.
def listaProductos():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM productos LIMIT 0,10"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda

def  recibeActualizarProducto(nompro, descripcion, precio, nuevoNombreFile, idpro):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("UPDATE productos SET nompro = %s descripcion = %s  precio = %s imagen = %s WHERE idpro= %s", (nompro, descripcion, precio, nuevoNombreFile, idpro))
        conexion_MySQLdb.commit()
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update

def registrarProducto(idpro, nompro, descripcion, precio, nuevoNombreFile):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute("INSERT INTO productos (idpro, nompro, descripcion, precio , imagen) VALUES (%s, %s, %s, %s, %s)", (idpro, nompro, descripcion, precio, nuevoNombreFile))
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_insert = cursor.rowcount #retorna 1 o 0
        return resultado_insert

def detallesdelProducto(idpro):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE idpro ='%s'" % (idpro,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        return resultadoQuery

def updateProducto(idpro):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE idpro = %s LIMIT 1", [idpro])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio