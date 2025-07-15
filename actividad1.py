print("Hola primer Git")
nombre = input("Ingresa tu nombre: ")
edad = int(input("ingresa tu edad por favor: "))
print("Bienvenido")
print(f"tu nombre es {nombre}")
if edad > 18:
    print("Eres mayor de edad")
elif edad > 0:
    print("Eres menor de edad")
else:
    print("Edad ingresada incorrectamente.")