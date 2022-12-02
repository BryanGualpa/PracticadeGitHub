print("\nALGORITMO SOBRE DE COLAS")
numeros=[]
for x in range(2):
    valor=str(input("Ingrese el nombre: "))
    valor2=str(input("Ingrese el numero de cedula: "))
    valor3=str(input("Desea guardar los datos ingresados(SI/NO)?: "))

    if(valor3=="SI"):
        numeros.append(valor)
        numeros.append(valor2)
    print("Los valores han sido guardados exitosamaente....")

print("\nLista")
print (numeros)
print ("\n")

resp=str(input("A alcanzado el limite para ingresar datos, desea eliminar los datos ingresados(SI/NO)?: "))

print("Esto es mio : ggggg)")
while True:
    if(resp=='SI'):
        eliminar = str(input("¿Que variable desea eliminar: "))
        for x in numeros:
            if(x==eliminar):
                numeros.remove(x)
        print("\nValores nuevos")
        print (numeros)
        resp=str(input("Desea eliminando datos(SI/NO): "))
        if(resp=='SI'):
            continue
        elif(resp=='NO'):
            break

print("El algoritmo de colas a finalizado.")

