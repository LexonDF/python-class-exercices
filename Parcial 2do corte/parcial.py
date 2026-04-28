pelicula = [(1, "Scary pelicula 6", 8500), (2, "Maldición", 7500), (3, "Bouelbard", 7000)]

def seleccion_pelicula(pelicula):
    for numero, nombre, precio in pelicula:
        print(f"{numero}. Pelicula: {nombre} | Precio: ${precio}")

    try:
        seleccion = int(input("Seleccione la pelicula (numero): "))
        
        pelicula_elegida = None
        for item in pelicula:
            if item[0] == seleccion:
                pelicula_elegida = item
                break 
        
        if pelicula_elegida:
            id_mov, nombre, precio = pelicula_elegida
            print(f"Has seleccionado: {nombre}")

            cantidad = int(input("¿Cuántas entradas desea comprar?: "))
            
            if cantidad > 0:
                total = cantidad * precio
                print("-" * 30)
                print(f"RESUMEN DE COMPRA:")
                print(f"Pelicula: {nombre}")
                print(f"Cantidad: {cantidad}")
                print(f"Total a pagar: ${total}")
                print("-" * 30)
            else:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Error: Ese número de película no existe en la lista.")

    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

seleccion_pelicula(pelicula)