with open("agenda_julian.txt", "w") as archivo:
  for i in range(6):
      nombre=input("ingrese nombre del estudiante: ")
      direccion=input("ingrese direccion del estudiante: ")
      telefono=input("ingrese telefono del estudiante: ")
      archivo.write(nombre + "," + direccion + "," + telefono + "\n")
with open("agenda_julian.txt", "r") as ejemplo:
    print("la agenda registradas son: ")
    print(ejemplo.read())