import funciones

archivo="archivo_ejemplo_antonio.csv"

while True:
    print("menu")
    print("1. ver estuidantes")
    print("2. agregar estuidantes")
    print("3. salir")

    opcion=input("seleecione ina opcion:")
    if opcion=="1":
        estas= funciones.leer_estudiantes(archivo)
        for e in estas:
            print(f"{e["nombre"]} - {e["edad"]} años - {e["direccion"]}")

    elif  opcion ==2:
        nombre= input("nombre")
        edad=input("edad")
        direccion=input("direccion")
        if not  funciones.validar_nombre(nombre):
            print ("nombre invalido")
        if not  funciones.validar_edad(edad):
            print ("edad invalida")
        if not funciones.validar_direccion(direccion):
            print ("direccion invalida")
            continue
        funciones.agregar_estuidante(archivo, nombre, edad, direccion)
        print("estudiante agregado con exito")

    elif opcion=="3":
        break
    else:
        print("opcion no valida")     
    


