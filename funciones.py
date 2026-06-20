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
            poblacion = int(paises[2])
            superficie = int(paises[3])
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
        print('''----------------
Ingrese 1 para actualizar la poblacion del pais.
Ingrese 2 para actualizar la superficie de un pais.
Ingrese 3 para volver al menu.
----------------''')
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


def filtrar_paises(paises):

    while True:
        print('''----------------
Ingrese 1 para filtrar por continente.
Ingrese 2 para filtrar por rango poblacional.
Ingrese 3 para filtrar por rango de superficie.
Ingrese 4 para volver al menu.
----------------''')
        
        opcion = input('Ingrese la opcion elegida: ')
        match opcion:

            case '1':

                paises_filtrados = []
                encontrado = False
                filtrar_continente = input('Ingrese que continente desea filtrar: ').strip().title()
                if filtrar_continente in ['America', 'Asia', 'Europa', 'Africa', 'Oceania']:
                    for pais, datos in paises.items():
                        if datos['Continente'] == filtrar_continente:
                            paises_filtrados.append(pais)
                            encontrado = True
                    print(f'Los paises ubicados en {filtrar_continente} son {paises_filtrados}')
                    if not encontrado:
                        print('No existen paises dentro de ese continente.')
                        break
                else:
                    print('El continente ingresado no existe')

            case '2':

                paises_filtrados = []
                opcion_filtrado = input('\nElija X para filtrar paises con mayor poblacion que la seleccionada.\nSeleccione Y para filtrar paises con menor poblacion que la seleccionada: ').strip().title()
                match opcion_filtrado:
                    case 'X':
                        
                        while True:
                            try:

                                encontrado = False
                                filtrar_poblacion = int(input('Ingrese por el rango poblacional que desee filtrar: '))
                                if filtrar_poblacion < 0:
                                    raise ErrorNumeroInvalido ('Error, la poblacion no puede ser menor a 0')
                                for pais, datos in paises.items():
                                    if datos['Poblacion'] > filtrar_poblacion:
                                        paises_filtrados.append(pais)
                                        encontrado = True
                                if encontrado:
                                    print(f'Los paises con una poblacion mayor a {filtrar_poblacion} son {paises_filtrados}')
                                if not encontrado:
                                    print('No existen paises dentro de ese rango poblacional.')
                                break

                            except ValueError:
                                print('Error, ingrese un numero valido.')
                            except ErrorNumeroInvalido as e:
                                print (e)

                    case 'Y':

                        while True:
                            try:

                                encontrado = False
                                filtrar_poblacion = int(input('Ingrese por el rango poblacional que desee filtrar: '))
                                if filtrar_poblacion < 0:
                                    raise ErrorNumeroInvalido ('Error, la poblacion no puede ser menor a 0')
                                for pais, datos in paises.items():
                                    if datos['Poblacion'] < filtrar_poblacion:
                                        paises_filtrados.append(pais)
                                        encontrado = True
                                print(f'Los paises con una poblacion menor a {filtrar_poblacion} son {paises_filtrados}')
                                if not encontrado:
                                    print('No existen paises dentro de ese rango poblacional.')
                                break

                            except ValueError:
                                print('Error, ingrese un numero valido.')
                            except ErrorNumeroInvalido as e:
                                print (e)
                        
                    case _:
                        print('Ingrese una opcion valida')

            case '3':

                paises_filtrados = []
                opcion_filtrado = input('\nElija X para filtrar paises con mayor superficie que la seleccionada.\nSeleccione Y para filtrar paises con menor superficie que la seleccionada: ').strip().title()
                match opcion_filtrado:
                    case 'X':

                        while True:
                            try:

                                encontrado = False
                                filtrar_poblacion = int(input('Ingrese por el rango de superficie que desee filtrar: '))
                                if filtrar_poblacion <= 0:
                                    raise ErrorNumeroInvalido ('Error, la superficie no puede ser menor/igual a 0')
                                for pais, datos in paises.items():
                                    if datos['Superficie'] > filtrar_poblacion:
                                        paises_filtrados.append(pais)
                                        encontrado = True
                                print(f'Los paises con una superficie mayor a {filtrar_poblacion} son {paises_filtrados}')
                                if not encontrado:
                                    print('No existen paises dentro de ese rango de superficie.')
                                break

                            except ValueError:
                                print('Error, ingrese un numero valido.')
                            except ErrorNumeroInvalido as e:
                                print (e)

                    case 'Y':

                        while True:
                            try:

                                encontrado = False
                                filtrar_poblacion = int(input('Ingrese por el rango de superficie que desee filtrar: '))
                                if filtrar_poblacion <= 0:
                                    raise ErrorNumeroInvalido ('Error, la superficie no puede ser menor/igual a 0')
                                for pais, datos in paises.items():
                                    if datos['Superficie'] < filtrar_poblacion:
                                        paises_filtrados.append(pais)
                                        encontrado = True
                                print(f'Los paises con una superficie menor a {filtrar_poblacion} son {paises_filtrados}')
                                if not encontrado:
                                    print('No existen paises dentro de ese rango de superficie.')
                                break

                            except ValueError:
                                print('Error, ingrese un numero valido.')
                            except ErrorNumeroInvalido as e:
                                print (e)
                        
                    case _:
                        print('\nIngrese una opcion valida')
                            
            case '4':
                print('\nSera regresado al menu principal.\n')
                return
            

def ordenar_paises(paises):
    while True:       
        opcion = input('''1. Nombre
2. Poblacion
3. Superficie
4. Salir

Ingrese como desea ordenar los países: ''')
        match opcion:
            case '1':
#Se crea una nueva variable a partir del sorted del diccionario 'paises' para tenerlo ordenado alfabeticamente por los nombres de los paises
                paises_ordenados = sorted(paises)
                print("\n-----Paises ordenados por Nombre-----\n")
                for pais in paises_ordenados:
                    print(pais)
                print("")                                     
                break

            case '2':
                orden = input('1. Ascendente \n2. Descendente\n\nIngrese el orden deseado: ')
#Se crea una nueva lista para tener primero el número de la poblacion y poder usar un sorted para ordenarlo
                lista_poblacion = []
                for pais, datos in paises.items():
#Se agrega el número de la poblacion y el nombre del pais para la futura impresion
                    lista_poblacion.append((int(datos["Poblacion"]), pais))
                match orden:
                    case '1':
                        lista_poblacion = sorted(lista_poblacion)
                    case '2':
#Usando reverse= True se puede dar vuelta la lista para que quede en orden descendiente
                        lista_poblacion = sorted(lista_poblacion, reverse=True)
                    case _:
                        print("Error, ingrese un número valido")
                        break

                print("\n-----Paises ordenados por Poblacion-----\n")
                for pais in lista_poblacion:
                    print(pais)
                print("")
                break 

            case '3':
#Se usa usa la misma lógica que el (case '2')
                orden = input('1. Ascendente \n2. Descendente\n\nIngrese el orden deseado: ')
                lista_superficie = []
                for pais, datos in paises.items():
                    lista_superficie.append((int(datos["Superficie"]), pais))
                match orden:
                    case '1':
                        lista_superficie = sorted(lista_superficie)
                    case '2':
                        lista_superficie = sorted(lista_superficie, reverse=True)
                    case _:
                        print("Error, ingrese un número valido")
                        break

                print("\n-----Paises ordenados por Superficie-----\n")
                for pais in lista_superficie:
                    print(pais)
                print("")
                break 
                
            case '4':
                print('Volviendo al menú')
                break
            case _:
                print("Error, ingrese un número valido")


def mostrar_estadisticas(paises):

#Se crean 2 variables para anotar el número con menor y mayor cantidad de poblacion
    mayor_pais = ""
    menor_pais = ""
    for pais, datos in paises.items():
#Se actualiza la variable al primer pais para luego comparar
        if mayor_pais == '':
            mayor_pais = pais
            menor_pais = pais
#Se compara para actualizar la variable para menor y mayor superficie
        if int(datos['Poblacion']) > int(paises[mayor_pais]['Poblacion']):
            mayor_pais = pais
        if int(datos['Poblacion']) < int(paises[menor_pais]['Poblacion']):
            menor_pais = pais
    print("\n------ Paises Mayor y Menor Poblacion ------\n")
    print(f'''Mayor poblacion:
Pais: {mayor_pais}  Poblacion: {paises[mayor_pais]['Poblacion']}''')
    print("")
    print(f'''Menor poblacion:
Pais: {menor_pais}  Poblacion: {paises[menor_pais]['Poblacion']}''')

#Se crea la variable de la suma total de la poblacion
    suma_poblacion = 0
    for pais, datos in paises.items():
        suma_poblacion += int(datos['Poblacion'])
#Se suma la poblacion de cada pais y se saca el promedio
        promedio_poblacion = suma_poblacion / len(paises)

    print("\n------ Promedio de Poblacion ------\n")
    print(promedio_poblacion)


#Misma lógica que el promedio de la población
    suma_superficie = 0
    for datos in paises.values():
        suma_superficie += int(datos['Superficie'])

    promedio_superficie = suma_superficie / len(paises)

    print("\n------ Promedio de Superficie ------\n")
    print(promedio_superficie)

    
#Se crea un diccionario con los continentes
    print("\n------ Cantidad de paises por continente ------\n")
    continentes = {'America': 0, 'Europa': 0, 'Asia': 0, 'Africa': 0, 'Oceania': 0}

    for datos in paises.values():

        continente = datos['Continente']
        if continente in continentes:
            continentes[continente] += 1
#Se compara para agregar un pais al contador segun el continente al que pertenezca.

    for continente, cantidad in continentes.items():
        print(f'{continente}: {cantidad}')
    print("")
