#ciclo para pedir datos de contacto al usuario
def pedir_datos_contacto():
    contactos = [6]
    while True:
        nombre = input("Ingrese el nombre del contacto (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        telefono = input("Ingrese el número de teléfono del contacto: ")
        direccion = input("Ingrese la dirección del contacto: ")
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'direccion': direccion
        }
        contactos.append(contacto)
    return contactos
#fin ciclo para pedir datos de contacto al usuario
#funcion para mostrar los contactos ingresados
def mostrar_contactos(contactos):
    for contacto in contactos[1:]:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Dirección: {contacto['direccion']}")
#fin funcion para mostrar los contactos ingresados
#FUNCION para guardar contactos en un archivo
def guardar_contactos_en_archivo(contactos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for contacto in contactos[1:]:
            archivo.write(f"{contacto['nombre']},{contacto['telefono']},{contacto['direccion']}\n")
#fin FUNCION para guardar contactos en un archivo
#funcion principal
def main():
    contactos = pedir_datos_contacto()
    mostrar_contactos(contactos)
    guardar_contactos_en_archivo(contactos, 'contactos.txt')
#fin funcion principal
if __name__ == "__main__":
    main()
#funcion para abrir el archivo y leer los contactos guardados
def leer_contactos_desde_archivo(nombre_archivo):
    contactos = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            nombre, telefono, direccion = linea.strip().split(',')
            contacto = {
                'nombre': nombre,
                'telefono': telefono,
                'direccion': direccion
            }
            contactos.append(contacto)
    return contactos
#fin funcion para abrir el archivo y leer los contactos guardados
