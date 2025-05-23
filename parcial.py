from funciones import *


seguir = "s"
while seguir == "s":
    print("")
    print("--- MENU DE OPCIONES ---")
    print("1-Mostrar productos y ventas\n2-Ordenar productos por Ventas anuales (desc)\n3-Buscar producto por nombre\n4-Buscar monto de venta en la matriz\n5-Salir")
    opcion = int(input("seleciones una opcion (1-5): "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("error, selecione opcion (1-5): "))

    if opcion == 1:
        mostrar(ventas,productos)
    elif opcion == 2:
        ordenar_productos(ventas,productos)
    elif opcion == 3:
        buscar_por_nombre(ventas,productos)
    elif opcion == 4:
        buscar_valor_de_venta(ventas,productos)
    else:
        seguir = "n"