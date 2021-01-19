import statistics as stats

nIntroducidos = 1
noPermitido = 0
numeros = []
print ("Introduzca 0 para mostrar el resultado y finalizar el programa")
a = input("Introduce un numero\n")


if (a.isnumeric()):

    numeros.append(int(a))

    while int(a) >0:

        a = input("Introduce otro numero\n")

        while not a.isnumeric():
            print("Valor no permitido")
            noPermitido = noPermitido + 1
            print(noPermitido)
            a = input("Introduce otro numero\n ")

        if int(a) >0 : #Para no sumar como número introducido el 0
            nIntroducidos = nIntroducidos +1
            numeros.append(int(a))

    print("Programa finalizado")
    print("Números introducidos:  " + str(nIntroducidos)) #Suma de todos los números introducidos
    print("Suma total de los numeros introducidos: " + str(sum(numeros))) #Para comprobar que el contenido de la lista sea correcto
    print("La media de los datos es: " + str(int(stats.mean(numeros)))) #Con el int de delante convertimos el float en int para que no salga con tantos decimales

else:
   print("Valor no permitido")
   noPermitido = noPermitido + 1
   print(noPermitido)

