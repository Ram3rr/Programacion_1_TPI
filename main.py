import funciones as fun

paises = fun.cargar_paises()

while True:
    opcion = fun.menu_opciones()
    match opcion:
        case '1':
            fun.agregar_pais(paises)
        case '2':
            fun.actualizar_datos(paises)
        case '3':
            fun.buscar_paises(paises)
        case '4':
            fun.filtrar_paises(paises)
        case '5':
            pass
        case '6':
            pass
        case '7':
            print('\nGracias por utilizar nuestro sistema, hasta luego!')
            break
        case '8':
            print(paises)
        case _:
            print('\nError, ingrese una opcion valida.\n')