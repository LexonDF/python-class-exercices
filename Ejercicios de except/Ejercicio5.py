# 5.Programa que guarde en un archivo.txt diez palabras.
print("=== Guardar 10 palabras en archivo ===")

nombre_archivo = "palabras.txt"
palabras = []

try:
    for i in range(1, 11):
        palabra = input(f"Ingrese la palabra #{i}: ").strip()
        if not palabra:
            raise ValueError(f"La palabra #{i} no puede estar vacía.")
        palabras.append(palabra)

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for palabra in palabras:
            archivo.write(palabra + "\n")

    print(f"\n✔ Se guardaron {len(palabras)} palabras en '{nombre_archivo}'.")
    print("\nContenido guardado:")

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo, 1):
            print(f"  {i}. {linea.strip()}")

except ValueError as e:
    print(f"\n⚠ Error de valor: {e}")
except FileNotFoundError:
    print(f"\n⚠ Error: No se encontró la ruta para guardar '{nombre_archivo}'.")
except PermissionError:
    print(f"\n⚠ Error: Sin permisos para escribir en '{nombre_archivo}'.")
except OSError as e:
    print(f"\n⚠ Error del sistema al manejar el archivo: {e}")
except KeyboardInterrupt:
    print("\n\nOperación cancelada por el usuario.")