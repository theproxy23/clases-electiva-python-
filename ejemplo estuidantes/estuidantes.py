class estudiante:
    def _int_(self, nombre, notas):
        self.nombre = nombre
        self.notas =notas
    def calcular_promedio (self):
        promedio= sum(self.nombre)/(self.notas)
        return promedio
    def mostrar_info(self):
        promedio=self.calcular_promedio()
        if promedio>=3.0:
            estado="aprovado"
        else:
            estado= "reprovado"
        print(f "/n el promedio de las notas de" {self.nombre} "es:" {promedio:.2f}, "por esto el estudiante esta" ({estado}))
        lsita_estudiantes=[]
    
        cantidad= int(input("ingrese cantidad de estudiantes a registrar"))
    for i in range(cantidad):
        print(f"/n estudiante numero{i+1}")
              nombre=input("nombre:")
              notas=[]
            for j in range(3):
            nota=float(input(f"ingrese la nota numero {j+i} de {nombre}:"))
            notas.append(nota)
        estudiante=estudiante(nombre, notas)
        lista_estudiantes.append(estudiante)

    aprovados=0
    for est in lista_estudiantes:
    est.mostrar_info()
    if est.calcular_promedio()>=3.0:
    aprovados +=1
    print(f"/n entonces los {cantidad} estudiantes")
    print(f"/n {aprovados} aprovaron el curso")
    print(f"{len(lista_estudiantes)-aprovados} reprobaron")