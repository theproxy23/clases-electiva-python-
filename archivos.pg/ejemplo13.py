with open("ejemplo2.txt", "w") as archivo:
  for i in range(3):
      nombre=input("ingrese nombre del estudiante: ")
      archivo.write(nombre + "\n")
with open("ejemplo2.txt", "r") as ejemplo:
    print("los estudiantes ingresados son: ")
    print(ejemplo.read())