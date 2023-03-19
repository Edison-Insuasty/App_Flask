from . import descripcion
from flask import render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from index import *
from flask_babel import Babel, format_decimal, format_date, gettext, ngettext, lazy_gettext

@descripcion.route('/productos')
def mostrarProductos():

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

    productos = gettext('Producto')
    descripcion4 = gettext('DESCRIPCIÓN DE NUESTROS PRODUCTOS')
    nombre = gettext('Nombre')
    producto1 = gettext('POLLO BROASTER:  El pollo estilo broaster, es un pollo frito muy sabroso y crujiente que últimamente se viene sirviendo en muchos restaurantes de comida rápida (Tipo KFC) e incluso algunas versiones gourmet en restaurantes importantes. La mayoría de estos, se especializan en preparar este estilo de pollo rebozado con sabores tradicionales')
    producto2 = gettext('HAMBURGUESA: Sándwich hecho a base de carne molida o de origen vegetal, aglutinada en forma de filete cocinado a la parrilla o a la plancha, aunque también puede freírse u hornearse')
    producto3 = gettext('PAPA MIXTA: Deliciosa papa asada acompañada de pastor, arrachera, crema, mantequilla, queso blanco y queso amarillo. Le puedes añadir unos deliciosos nachos')
    producto4 = gettext('PERRO CALIENTE: El perrito caliente, también llamado completo, pancho, jocho, shuco o pan con perro, es un alimento en forma de bocadillo que se genera con la combinación de una salchicha')
    producto5 = gettext('PIZZA: La pizza es una preparación culinaria que consiste en un pan plano, habitualmente de forma circular, elaborado con harina de trigo, levadura, agua y sal (a veces aceite de oliva) que tradicionalmente se cubre con salsa de tomate y mozzarella y se hornea a alta temperatura en un horno de leña')
    producto6 = gettext('SANDWICH CUBANO: También llamado “Cuban Pressed Sandwich”, es un sanguchito que en su formato original lleva: jamón tipo lacón cocido, carne de cerdo, queso laminado, pepinillos en salmuera (que le dan el toque crunchy y fresquito), mayonesa y también le suelen añadir mostaza picante')
    producto7 = gettext('CARNE: Carne es todo alimento que sale de las partes blandas que se comen de un animal. En nuestro medio se suele comer carne de vacuno (vaca, ternera y añojo o ternera de un año), cerdo, cordero, cordero lechal, cabrito, conejo, aves de corral (pollo, pavo), etc, tiene diversas formas de preparación')
    producto8 = gettext('FILETE DE POLLO: El filete es una presa muy versatil, viene sin piel y sin hueso, porcionado, listo para adobar y preparar. Es un producto naturalmente alto en proteína, ideal para una dieta balanceada')
    producto9 = gettext('PAPA RELLENA: La papa rellena es una fritura típica de varios países latinoamericanos como Chile, Colombia, Cuba, Perú y Puerto Rico. Consiste en una masa frita de papa cocida, rellena de carne de vacuno, pollo, queso, cebollas, aceitunas, huevos duros, entre otros ingredientes picados')

    results10 = {'productos':productos,'descripcion4':descripcion4,'nombre':nombre,'producto1':producto1,
                'producto2':producto2,'producto3':producto3,'producto4':producto4,'producto5':producto5,
                'producto6':producto6,'producto7':producto7,'producto8':producto8,'producto9':producto9}

    if 'conectado' in session:
        return render_template('productos.html', dataLogin = dataLoginSesion(),results5=results5, results10=results10)
    else:
        return abort(401)