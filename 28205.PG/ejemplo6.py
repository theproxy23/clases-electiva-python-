numero=6
print(f"tabla del {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Fin del programa
numero_secreto = 20  # Este es un número secreto
intento = int(input("Adivina el número secreto entre 1 al 40: "))
while intento != numero_secreto:
    print("Número incorrecto. Intenta de nuevo.")
    intento = int(input("Adivina el número secreto entre 1 al 40: "))
print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto}")

# Este programa muestra la tabla de multiplicar del 6 y un juego de adivinanza de números

contador=0
for i in range(100):
    contador += 1
print(f"El contador ha llegado a: {contador}")

# Contador simple que cuenta hasta 100

acumulador=0
for i in range(5):
 numero=int(input("Introduce un número para sumar (0 para terminar): "))
 acumulador += numero
 print(f"Suma acumulada: {acumulador}")