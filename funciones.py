#Se crean errores personalizados para mensajes mas claros y evitar el uso excesivo de solamente ValueError
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

    paises_agregados = {}
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        next (archivo) 
        for i in archivo:
            paises = i.strip().split(',')
            nombre = paises[0]
            continente = paises[1]
            poblacion = paises[2]
            superficie = paises[3]
            #Se crea el diccionario paises_agregados con un diccionario como valor de cada uno
            paises_agregados[nombre] = {'Continente': continente, 'Poblacion': poblacion, 'Superficie': superficie}

        return paises_agregados
    

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

#Se agregan los datos del pais a el diccionario de paises ya validado.
    paises[nombre] = {'Continente': continente, 'Poblacion': poblacion, 'Superficie': superficie}


def actualizar_datos(paises):
    while True:
        try:
            actualizar_pais = input('Ingrese que pais desea editar: ').strip().title()
            if actualizar_pais not in paises:
                raise ErrorNombreInvalido ('Error, ese pais no se encuentra cargado.')
            break
        except ErrorNombreInvalido as e:
            print(e)

    while True:        
        print('''Ingrese 1 para actualizar la poblacion del pais.
Ingrese 2 para actualizar la superficie de un pais.
Ingrese 3 para volver al menu.
              ''')
        opcion = input('Ingrese su opcion: ')
        match opcion:
            case '1':
                while True:    
                    try:    
                        poblacion_actualizada = int(input('Ingrese la poblacion actualizada: '))
                        if poblacion_actualizada < 0:
                            raise ErrorNumeroInvalido ('Error, la poblacion no puede ser menor a cero.')
                        paises[actualizar_pais]['Poblacion'] = poblacion_actualizada
                        print(f'La poblacion de {actualizar_pais} fue correctamente actualizada.')
                        break
                    except ValueError:
                        print('Error, ingrese un numero valido')
                    except ErrorNumeroInvalido as e:
                        print(e)
                
            case '2':
                while True:    
                    try:
                        superficie_actualizada = int(input('Ingrese la superficie actualizada: '))
                        if superficie_actualizada <= 0:
                            raise ErrorNumeroInvalido ('Error, la superficie no puede ser menor/igual a 0.')
                        paises[actualizar_pais]['Superficie'] = superficie_actualizada
                        print(f'La superficie de {actualizar_pais} fue correctamente actualizada.')
                        break
                    except ValueError:
                        print('Error, ingrese un numero valido')
                    except ErrorNumeroInvalido as e:
                        print(e)

            case '3':
                print('Sera regresado al menu principal\n')
                break
            case _:
                print('Error, ingrese una opcion valida')


def buscar_paises(paises):
    while True:
        encontrado = False
        busqueda = input("Ingrese el país buscado: ")
        for pais,datos in paises.items():
            if busqueda.title() in pais:
                print(f'''Pais encontrado correctamente.
Pais: {pais}
Continente: {datos['Continente']}
Poblacion: {datos['Poblacion']}
Superficie: {datos['Superficie']}''')
                encontrado = True
        if not encontrado:
            print('Error, el pais buscado no se encuentra en la lista.')
        else: break