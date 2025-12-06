class Estudiante:
#clase principal de funcion
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas =notas
    def calcular_promedio (self):
        promedio= sum(self.notas)/len(self.notas)
        return promedio
    def mostrar_info(self):
        promedio=self.calcular_promedio()
        if promedio>=3.0:
            estado="aprovado"
        else:
            estado="reprovado"
        print(f"\n el promedio de las notas de {self.nombre} es: {promedio: .2f}, por esto el estudiante esta ({estado})")
#se sale de la clase  Sigo altgr+?
lista_estudiantes=[]   
cantidad= int(input("ingrese cantidad de estudiantes a registrar,:"))
for i in range(cantidad):
    print(f"\n ingrese el  estudiante numero, {i+1}")
    nombre=input("ingrese el nombre del estudiante: ")
    notas=[]

    for j in range(3):
        nota=float(input(f"ingrese la nota numero {j+i}:"))
        notas.append(nota)

    estudiante = Estudiante (nombre,notas)
    lista_estudiantes.append(estudiante)
#se sale de la clase
aprovados=0
for est in lista_estudiantes:
    est.mostrar_info()
    if est.calcular_promedio()>=3.0:
         aprovados +=1
    print(f"\n entonces los {cantidad} estudiantes")
    print(f"\n {aprovados} aprovaron el curso")
    print(f"\ {aprovados} reprobaron")