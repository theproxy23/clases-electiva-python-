estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes.append("Sofía")
print(estudiantes)


estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes.insert(4, "Sofía")
print(estudiantes)

estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes[1]="Sofía"
print(estudiantes)

estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes[1:4]=["Sofía"]
print(estudiantes)

estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes.remove("Ana")
print(estudiantes)  

estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes.pop(2)
print(estudiantes)

estudiantes=["JULIAN", "Ana", "Luis", "Marta", "Carlos"]
estudiantes.sort(reverse=True)
print(estudiantes)