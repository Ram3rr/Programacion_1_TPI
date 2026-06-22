import funciones as fun

paises = fun.cargar_paises()

while True:
    opcion = fun.menu_opciones()
    match opcion:
        case '1':
            fun.agregar_pais(paises)
            fun.guardar_paises(paises)
        case '2':
            fun.actualizar_datos(paises)
            fun.guardar_paises(paises)
        case '3':
            fun.buscar_paises(paises)
        case '4':
            fun.filtrar_paises(paises)
        case '5':
            fun.ordenar_paises(paises)
        case '6':
            fun.mostrar_estadisticas(paises)
        case '7':
            print('\nGracias por utilizar nuestro sistema, hasta luego!')
            break
        case _:
            print('\nError, ingrese una opcion valida.\n')