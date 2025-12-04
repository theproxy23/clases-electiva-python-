# numeros=[]
# for i in range(5):
#     numero=int(input("Ingrese un número: "))
#     numeros.append(numero)
# print(f"Lista final de numeros es: {numeros}")

personas={
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid"
}
print(f"Nombre: {personas['nombre']}")
print(f"Edad: {personas['edad']}") 


estudiantes={"nombre:" "María" "nota":4.2}
estudiantes["nota"]= 4.5
print(estudiantes)

estudiantes={"nombre":"María","edad":20, "nota":4.2}
del estudiantes["edad"]
print(estudiantes)

estudiantes={"nombre":"María","edad":20, "nota":4.2}
estudiantes.clear()
print(estudiantes)

estudiantes={"nombre":"María","edad":20, "nota":4.2}
for clave in estudiantes:
    print(clave)

estudiantes={"nombre":"María","edad":20, "nota":4.2}
for clave, valor in estudiantes.items():
    print(f"{clave}: {valor}") 

estudiantes={"nombre":"María","edad":20, "nota":4.2}
for valor in estudiantes.values():
    print(valor)    