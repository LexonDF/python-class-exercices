# 3.Programa que reciba una fecha de nacimiento y arroje la edad de la persona.
from datetime import date

print("=== Cálculo de Edad ===")

try:
    año = int(input("Año de nacimiento  (ej. 1995): "))
    mes = int(input("Mes de nacimiento  (1-12): "))
    dia = int(input("Día de nacimiento  (1-31): "))

    nacimiento = date(año, mes, dia)
    hoy        = date.today()

    if nacimiento > hoy:
        raise ValueError("La fecha de nacimiento no puede ser en el futuro.")

    edad = hoy.year - nacimiento.year
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1

    print(f"\nFecha de nacimiento : {nacimiento.strftime('%d/%m/%Y')}")
    print(f"Fecha actual        : {hoy.strftime('%d/%m/%Y')}")
    print(f"Edad                : {edad} años")

except ValueError as e:
    print(f"\n⚠ Error de valor: {e}")
except OverflowError:
    print("\n⚠ Error: el año ingresado está fuera del rango permitido.")
except KeyboardInterrupt:
    print("\n\nOperación cancelada por el usuario.")