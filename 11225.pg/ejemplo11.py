a={"ROJO","VERDE","AZUL"}
b={"AMARILLO","negro","NARANJA"}
union=a | b
print(union)

a={"ROJO","VERDE","AZUL"}
b={"AMARILLO","VERDE","NARANJA"}
inter=a & b
print(inter)

A={"ROJO","VERDE","AZUL"}
B={"AMARILLO","VERDE","NARANJA"}
INTER=  A.intersection(B)
print(INTER)

A={"ROJO","VERDE","AZUL"}
B={"AMARILLO","VERDE","NARANJA"}
DIF= A.difference(B)
print(DIF)

A={"ROJO","VERDE","AZUL"}
B={"AMARILLO","VERDE","NARANJA"} 
DIF_SIM= A.symmetric_difference(B)
print(DIF_SIM)
