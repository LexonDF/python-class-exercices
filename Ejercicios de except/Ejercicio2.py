# 2.Programa de inventario de zapatos que valide si una talla, color, tipo de zapatos está disponible.

inventario = {
    (38, "negro", "tenis"): 5,
    (39, "blanco", "formal"): 2,
    (40, "café", "bota"): 0,
    (41, "negro", "tenis"): 3,
    (42, "rojo", "sandalia"): 1,
}

print("=== Inventario de Zapatos ===")

try:
    talla = int(input("Ingrese la talla (número): "))
    color = input("Ingrese el color: ").lower().strip()
    tipo  = input("Ingrese el tipo de zapato: ").lower().strip()

    if not color or not tipo:
        raise ValueError("El color y el tipo no pueden estar vacíos.")

    clave = (talla, color, tipo)

    if clave in inventario:
        cantidad = inventario[clave]
        if cantidad > 0:
            print(f"\n✔ Disponible: {cantidad} par(es) — talla {talla}, {color}, {tipo}.")
        else:
            print(f"\n✘ Agotado: talla {talla}, {color}, {tipo} (sin stock).")
    else:
        print(f"\n✘ No existe en inventario: talla {talla}, {color}, {tipo}.")

except ValueError as e:
    print(f"\n⚠ Error de valor: {e}")
except KeyboardInterrupt:
    print("\n\nOperación cancelada por el usuario.")