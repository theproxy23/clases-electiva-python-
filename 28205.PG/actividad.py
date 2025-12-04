contador=0
numero=int(input("Introduce un número (0 para terminar): "))
for i in range(5):
    if numero>0:
        contador += 1
    numero=int(input("Introduce un número (0 para terminar): "))
print(f"la cantidad de numeros es: {contador}")