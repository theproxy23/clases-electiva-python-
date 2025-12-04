def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido/a. a la clase de Python."

mensaje=saludar("JULIAN")
print(mensaje)

# Ejemplo de uso de la función saludar
# Funciones matemáticas básicas
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."
def calculadora():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Ingrese la opción (1/2/3/4):")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("resultado:", sumar(a, b))
    elif opcion == '2':
        print("resultado:", restar(a, b))
    elif opcion == '3':
        print("resultado:", multiplicar(a, b))

    elif opcion == '4':
        print("resultado:", dividir(a, b))
    else:
        print("Opción inválida.")
calculadora()

# Ejemplo de función para calcular el factorial de un número

