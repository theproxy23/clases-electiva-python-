class persona:
    def __int__(self, nombre, edad):
       self.nombre=nombre
       self.edad=edad
    def saludar(self):
        print(f"hola soy{self.nombre} y tengo {self.edad}años")
persona1 = persona("laura",20)
persona2 = persona("andres",25)

persona1.saludar()
persona2.saludar()