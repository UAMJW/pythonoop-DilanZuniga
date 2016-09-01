from data.propiedad import Propiedad
propiedades = []
def mainSwitch(option):
    return {
        'nueva':crear_propiedad,
        'mostrar':listar_propiedades,
        'salir':endFunction
    }.get(option,default)

def endFunction():
    print ''
    print 'Hasta luego!'
    print ''

def default():
    print 'Caracter no valido'
    

def crear_propiedad():
    costo = raw_input('Ingrese el costo del propiedad: ')
    direccion   = raw_input('Ingrese la direccion del propiedad: ')
    numero = raw_input('Ingrese el numero del propietario de la propiedad: ')

    propiedadNuevo = Propiedad(costo,direccion,numero)
    propiedades.append(propiedadNuevo)
    print ''

def listar_propiedades():
    for propiedad in propiedades:
        print propiedad.toString()
    print ''
    raw_input('Desea continuar?') 


def printMenu():
    print ''
    print '-------------------REALTY-----------------------'
    print 'Escriba (nueva) para ingresar una Propiedad'
    print '  '
    print 'Escriba (mostrar) para mostrar la lista de estudiantes'
    print '    '
    print 'Escriba(salir)para finalar la edicion  '
    print ''


var = ''
while (var!='salir'):
    printMenu()
    var = raw_input(' A continuacion escriba las opciones correspondientes: ')
    mainSwitch(var)()

