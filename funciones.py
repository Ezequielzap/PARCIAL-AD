

productos = ["A","B","C"]

ventas = [
    [50,60,70],    #A
    [80,55,45],    #B
    [40,65,75]     #C
]


#1
def mostrar(lista1:list,lista2:list):
    """
    funcion que muestra la lista de productos , las ventas trimestrales y el total anual

    parametro1 = recibe una matriz que contiene las ventas trimestales
    parametro2 = recibe una lista que contiene los productos

    """
    print("Ventas trimestrales\nProducto | T1 | T2 | T3 | Total\n--------------------------------")
    for i in range(len(lista1)):
        total = lista1[i][0] + lista1[i][1] + lista1[i][2]
        print(f"    {lista2[i]}    | {lista1[i][0]} | {lista1[i][1]} | {lista1[i][2]} | {total}") 


#2
def ordenar_productos(lista1:list,lista2:list):
    """
    funcion que ordena productos de manera descendente segun las ventas anuales

    parametro1 = recibe una matriz que contiene las ventas trimestrales
    parametro2 = recibe una lista que contiene los productos

    """
    for i in range(len(lista1)- 1):
        for j in range(i + 1,len(lista1)):
            if (lista1[i][0] + lista1[i][1] + lista1[i][2])  < (lista1[j][0] + lista1[j][1] + lista1[j][2]):

                aux = lista1[i]
                lista1[i] = lista1[j]
                lista1[j] = aux

                aux2 = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux2

    print("Ventas trimestrales ordenadas (desc)\nProducto | T1 | T2 | T3 | Total\n--------------------------------")
    for i in range(len(lista1)):
        total = lista1[i][0] + lista1[i][1] + lista1[i][2]
        print(f"    {lista2[i]}    | {lista1[i][0]} | {lista1[i][1]} | {lista1[i][2]} | {total}") 



#3
def buscar_por_nombre(lista1:list,lista2:list):
    """
    funcion que busca y muestra las ventas trimestrales de un producto especifico
    
    parametro1 = recibe una matriz que contiene las ventas trimestrales
    parametro2 = recibe una lista que contiene los productos

    """
    producto = input("ingrese que  producto quiere mostrar (A-B-C): ")
    while producto != "A" and producto != "B" and producto != "C":
        producto = input("error, ingrese que producto quiere mostrar (A-B-C): ")

    if producto == "A":
        producto = 0
        total = lista1[producto][0] + lista1[producto][1] + lista1[producto][2]
        print("Ventas trimestrales\nProducto | T1 | T2 | T3 | Total\n--------------------------------")
        print(f"    {lista2[producto]}    | {lista1[producto][0]} | {lista1[producto][1]} | {lista1[producto][2]} | {total}") 
    elif producto == "B":
        producto = 1
        total = lista1[producto][0] + lista1[producto][1] + lista1[producto][2]
        print("Ventas trimestrales\nProducto | T1 | T2 | T3 | Total\n--------------------------------")
        print(f"    {lista2[producto]}    | {lista1[producto][0]} | {lista1[producto][1]} | {lista1[producto][2]} | {total}")
    else: 
        producto = 2
        total = lista1[producto][0] + lista1[producto][1] + lista1[producto][2]
        print("Ventas trimestrales\nProducto | T1 | T2 | T3 | Total\n--------------------------------")
        print(f"    {lista2[producto]}    | {lista1[producto][0]} | {lista1[producto][1]} | {lista1[producto][2]} | {total}")
     

#4
def buscar_valor_de_venta(lista1:list,lista2:list):
    """
    fucion que busca un valor especifico de venta y si lo encuentra ,muestra a que producto pertenece
    
    parametro1 = recibe una matriz que contiene las ventas trimestrales
    parametro2 = recibe una lista que contiene los productos
    """
    valor_de_venta = int(input("Que valor de venta quiere buscar: "))
    valor_encontrado = False
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            if lista1[i][j] == valor_de_venta:
                print(f"El valor buscado pertenece al producto {lista2[i]} en el trimestre {j + 1}")
                valor_encontrado = True
    if valor_encontrado == False:
        print(f"No se encontro el valor de venta buscado")
            

