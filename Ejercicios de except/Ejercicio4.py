# 4.Programa que haga el calculo de una nómina, reciba un sueldo y calcule el pago de 15 días trabajados, calculando también el auxilio de transporte.
SMMLV              = 1_750_905
AUXILIO_TRANSPORTE = 250_000

print("=== Cálculo de Nómina — 15 días ===")

try:
    sueldo_mensual = float(input("Ingrese el sueldo mensual ($): "))

    if sueldo_mensual <= 0:
        raise ValueError("El sueldo debe ser un valor positivo.")

    pago_15_dias = sueldo_mensual / 2

    if sueldo_mensual <= 2 * SMMLV:
        auxilio_15 = AUXILIO_TRANSPORTE / 2
    else:
        auxilio_15 = 0

    total = pago_15_dias + auxilio_15

    print("\n--- Liquidación ---")
    print(f"Sueldo mensual        : ${sueldo_mensual:>12,.0f}")
    print(f"Pago 15 días          : ${pago_15_dias:>12,.0f}")
    if auxilio_15 > 0:
        print(f"Auxilio transporte    : ${auxilio_15:>12,.0f}")
    else:
        print(f"Auxilio transporte    : No aplica (sueldo > 2 SMMLV)")
    print(f"{'─'*36}")
    print(f"TOTAL A PAGAR         : ${total:>12,.0f}")

except ValueError as e:
    print(f"\n⚠ Error de valor: {e}")
except KeyboardInterrupt:
    print("\n\nOperación cancelada por el usuario.")