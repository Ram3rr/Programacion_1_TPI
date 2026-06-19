#Se crean errores personalizados para mensajes mas claros y evitar errores
class ErrorNombreInvalido(Exception):
    pass
class ErrorNumeroInvalido(Exception):
    pass



def menu_opciones():
    
    print('''----- Menu -----
1. Agregar un pais
2. Actualizar datos (Poblacion y superficie)
3. Buscar un pais por nombre
4. Filtrar paises (Continente, rango de poblacion y rango de superficie)
5. Ordenar paises (Nombre, poblacion y superficie)
6. Mostrar estadisticas
7. Salir.
''')
    opcion = input('Elija su opcion: ')

    return opcion

#Se carga la informacion del archivo csv a un diccionario
def cargar_paises():

    paisesAgregados = {}
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        next (archivo) 
        for i in archivo:
            paises = i.strip().split(',')
            nombre = paises[0]
            continente = paises[1]
            poblacion = paises[2]
            superficie = paises[3]
            #Se crea el diccionario paisesAgregados con un diccionario como valor de cada uno
            paisesAgregados[nombre] = {'Continente': continente, 'Poblacion': poblacion, 'Superficie': superficie}

        return paisesAgregados
    

def agregar_pais(paises):

#Se divide cada ingreso de informacion en 4 'while' y 'try' para poder agregar los datos del pais al diccionario 
    while True:
        try:

            nombre = input('Ingrese el nombre de su pais: ').strip().title()
            if not nombre.replace(' ','').isalpha():
                raise ErrorNombreInvalido ('Error, ingrese un nombre valido.')
            
            if nombre in paises:
                raise ErrorNombreInvalido ('Error, ese pais ya se encuentra cargado.')
            break
        except ErrorNombreInvalido as e:
            print(e)

    while True:
        try:

            continente = input('Ingrese el continente de su pais: ').strip().title()
            if not continente.replace(' ','').isalpha():
                raise ErrorNombreInvalido ('Error, ingrese un nombre valido.')
            if continente not in ['America', 'Asia', 'Europa', 'Africa', 'Oceania']:
                raise ErrorNombreInvalido ('Error, ingrese un continente existente.')
            break

        except ErrorNombreInvalido as e:
            print(e)

    while True:
        try:

            poblacion = int(input('Ingrese la poblacion de su país: '))
            if poblacion < 0:
                raise ErrorNumeroInvalido ('Error, la poblacion no puede ser menor a 0.')
            break

        except ValueError:
            print('Error, ingresar un numero valido.')
        except ErrorNumeroInvalido as e:
            print(e)
            
    while True:
        try:

            superficie = int(input('ingrese la superficie de su país: '))
            if superficie <= 0:
                raise ErrorNumeroInvalido ('Error, la superficie no puede ser menor/igual a 0.')
            break

        except ValueError:
            print('Ingrese un numero valido.')
        except ErrorNumeroInvalido as e:
            print(e)

#Se agrega el
    paises[nombre] = {'Continente': continente, 'Poblacion': poblacion, 'Superficie': superficie}


