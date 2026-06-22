import funciones as fun

paises = fun.cargar_paises()

while True:
    opcion = fun.menu_opciones()
    match opcion:
        case '1':
            fun.agregar_pais(paises)
        case '2':
            if paises.len() <= 0:
                ('Error, no hay paises cargados en el sistema.')
            else:
                fun.actualizar_datos(paises)
        case '3':
            if paises.len() <= 0:
                ('Error, no hay paises cargados en el sistema.')
            else:
                fun.buscar_paises(paises)
        case '4':
            if paises.len() <= 0:
                ('Error, no hay paises cargados en el sistema.')
            else:
                fun.filtrar_paises(paises)
        case '5':
            if paises.len() <= 0:
                ('Error, no hay paises cargados en el sistema.')
            else:
                fun.ordenar_paises(paises)
        case '6':
            if paises.len() <= 0:
                ('Error, no hay paises cargados en el sistema.')
            else:
                fun.mostrar_estadisticas(paises)
        case '7':
            print('\nGracias por utilizar nuestro sistema, hasta luego!')
            break
        case '8':
            print(paises)
        case _:
            print('\nError, ingrese una opcion valida.\n')