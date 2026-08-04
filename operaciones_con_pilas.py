class Pila:
    def __init__(self, capacidad_maxima=5):
        """Crear pila con una capacidad máxima definida."""
        self.capacidad = capacidad_maxima
        self.items = []

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def is_full(self):
        """Verifica si la pila alcanzó su capacidad máxima."""
        return len(self.items) == self.capacidad

    def push(self, elemento):
        """Agrega un elemento a la cima de la pila."""
        if self.is_full():
            print("\n❌ Error: La pila está llena (Overflow). No se puede agregar el elemento.")
        else:
            self.items.append(elemento)
            print(f"\n✅ Elemento '{elemento}' agregado correctamente a la pila.")

    def pop(self):
        """Elimina y retorna el elemento de la cima de la pila."""
        if self.is_empty():
            print("\n❌ Error: La pila está vacía (Underflow). No hay elementos para eliminar.")
            return None
        else:
            elemento = self.items.pop()
            print(f"\n✅ Elemento '{elemento}' eliminado de la cima de la pila.")
            return elemento

    def peek(self):
        """Muestra el elemento en la cima sin eliminarlo."""
        if self.is_empty():
            print("\n⚠️ La pila está vacía. No hay elemento en la cima.")
            return None
        else:
            print(f"\n👁️ Elemento en la cima (peek): {self.items[-1]}")
            return self.items[-1]

    def imprimir_pila(self):
        """Muestra el contenido visual de la pila."""
        if self.is_empty():
            print("\n📦 La pila está actualmente VACÍA.")
        else:
            print("\n--- Estado de la Pila (Arriba -> Abajo) ---")
            for i in range(len(self.items) - 1, -1, -1):
                if i == len(self.items) - 1:
                    print(f"| {self.items[i]} | <- CIMA")
                else:
                    print(f"| {self.items[i]} |")
            print("└-----┘")

    def cantidad_elementos(self):
        """Retorna el total de elementos presentes."""
        cantidad = len(self.items)
        print(f"\n📊 Cantidad de elementos en la pila: {cantidad} de {self.capacidad}")
        return cantidad


def mostrar_menu():
    print("\n" + "="*35)
    print("      MENÚ DE OPERACIONES CON PILA")
    print("="*35)
    print("1. Crear / Reiniciar Pila")
    print("2. Agregar elemento (Push)")
    print("3. Eliminar elemento (Pop)")
    print("4. Ver elemento en la cima (Peek)")
    print("5. Imprimir pila completa")
    print("6. Ver cantidad de elementos")
    print("7. Verificar si está vacía (isEmpty)")
    print("8. Verificar si está llena (isFull)")
    print("9. Salir")
    print("="*35)


def main():
    pila = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            try:
                cap = int(input("\nIngrese el tamaño máximo de la pila: "))
                if cap <= 0:
                    print("❌ El tamaño debe ser un entero positivo.")
                else:
                    pila = Pila(cap)
                    print(f"✅ Pila creada exitosamente con capacidad de {cap} elementos.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número entero.")

        elif opcion in ["2", "3", "4", "5", "6", "7", "8"]:
            if pila is None:
                print("\n⚠️ Primero debe crear una pila seleccionando la Opción 1.")
                continue

            if opcion == "2":
                dato = input("\nIngrese el valor o elemento a agregar: ").strip()
                if dato:
                    pila.push(dato)
                else:
                    print("❌ No se puede agregar un valor vacío.")

            elif opcion == "3":
                pila.pop()

            elif opcion == "4":
                pila.peek()

            elif opcion == "5":
                pila.imprimir_pila()

            elif opcion == "6":
                pila.cantidad_elementos()

            elif opcion == "7":
                if pila.is_empty():
                    print("\n🔴 La pila SÍ está vacía (isEmpty = True).")
                else:
                    print("\n🟢 La pila NO está vacía (isEmpty = False).")

            elif opcion == "8":
                if pila.is_full():
                    print("\n🔴 La pila SÍ está llena (isFull = True).")
                else:
                    print("\n🟢 La pila NO está llena (isFull = False).")

        elif opcion == "9":
            print("\n👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, elija un número entre 1 y 9.")


if __name__ == "__main__":
    main()