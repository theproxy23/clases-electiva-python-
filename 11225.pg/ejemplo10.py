frutas={"manzana","banana","cereza"}
print(frutas)

vacio=set()

numeros={1,2,3,4,5}
print(numeros)

# Conjuntos no permiten elementos duplicados

colores={"rojo","verde","azul","rojo","amarillo"}
colores.add("naranja")
print(colores)

# Verificar si un elemento está en el conjunto

colores={"rojo","verde","azul","amarillo"}
colores.remove("verde")
print(colores)

colores={"rojo","verde","azul","amarillo"}
colores.discard("verde")
print(colores)

