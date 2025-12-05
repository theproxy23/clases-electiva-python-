#validacion de datos
def validar_nombre(nombre):
    return nombre.isalpha() and len(nombre)>=2
def validar_edad(edad):
    return edad.isdigit() and 15 <=(edad)<=120
def validar_direccion(direccion):
    return direccion(direccion)>=3
#LEER archivo csv
def leer_estudiantes(archivo):
    lista=[]
    with open (archivo,"r", encoding="utf-8")as f:
        next (f) #saltar el encabezado
        for linea in f:
            nombre, edad, direccion,=linea.strip().split(",")
            lista.append({"nombre": nombre, "edad":edad, "direccion":direccion}) 
#agregar estuidantes al csv 
def agregar_estuidante(archivo, nombre,edad,direccion):
    with open (archivo, "a", encoding="utf-8")as f:
        f.write(f"{nombre},{edad},{direccion}/n") 
