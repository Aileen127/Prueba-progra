print("Hola primer Git")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad por favor: "))
Facultad = input("Ingresa la facultad a la que perteneces ").lower()
print("Bienvenido")
print(f"tu nombre es {nombre}")
if edad  >= 18:
    print("Eres mayor de edad")
elif edad > 0:
    print("Eres menor de edad")
else:
    print("Edad ingresada incorrectamente.")

if Facultad == "ingenieria":
    print("Bienvenido a la facultad de ingenieria")
elif Facultad != "ingenieria":
    print("Usted es de una facultad distinta")
