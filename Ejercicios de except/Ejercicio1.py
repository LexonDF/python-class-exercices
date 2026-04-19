# 1.Programa que valide correo electrónico.
correo = "Figueredo1101@gmail.com"
ingreso_correo = input("Ingrese el correo: ")

try:
    if ingreso_correo == correo:
        print("El correo es correcto.")
    else:
        raise ValueError("Correo incorrecto")

except ValueError:
    print("El correo es incorrecto.")