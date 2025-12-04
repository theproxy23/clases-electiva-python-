archivo=open("nombre.txt", "w")
archivo.write("ni nombre es Julian dario galvez\n")
archivo.write("mi edad es 21\n")
archivo.write("mi ciudad es neiva\n")
archivo.close()

archivo=open("ejemplo.txt", "a")
contenido=archivo.write("nueva linea de cpdigo\n")
archivo.close()

archivo=open("ejemplo.txt", "r")
contenido=archivo.read()
print(contenido)
archivo.close()

#--- IGNORE ---
