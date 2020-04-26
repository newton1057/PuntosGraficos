def potencia(base,exponente):
    resultado = 1
    if exponente == 0:
        resultado = 1
    else:
        for i in range(exponente):
            resultado = resultado * base
    return resultado

def raiz(valor):
    aux = 2.0
    cociente = valor/aux
    promedio = (aux + cociente)/2.0
    while abs(cociente - promedio) > 0.00000000001: 
        aux = promedio
        cociente = valor/aux
        promedio = (aux + cociente) / 2.0
    print(promedio)
    return promedio

numlados = int(input("Ingrese el numero de lados que tendra la figura: "))
if numlados>=3:
    auxladox=0
    auxladoy=0
    distancia=0
    for i in range(numlados):
        print(i)
        if i == 0:
            ladox = int(input("Ingrese el valor de punto X del origen: "))
            ladoy = int(input("Ingrese el valor de punto y del origen: "))

            origenx=ladox
            origeny=ladoy

            auxladox = ladox
            auxladoy = ladoy

        else:

            ladox = int(input("Ingrese el valor de punto X: "))
            ladoy = int(input("Ingrese el valor de punto y: "))

            restax = auxladox - ladox
            restay = auxladoy - ladoy

            print(restax)
            print(restay)

            respotenciax = potencia(restax,2)
            respotenciay = potencia(restay,2)

            print(respotenciax)
            print(respotenciay)

            auxraiz = respotenciax + respotenciay
            print(auxraiz)

            distancia = distancia + raiz(auxraiz)

            auxladox = ladox
            auxladoy = ladoy

            if i == numlados-1:

                restax = auxladox - origenx
                restay = auxladoy - origeny

                print(restax)
                print(restay)

                respotenciax = potencia(restax,2)
                respotenciay = potencia(restay,2)

                print(respotenciax)
                print(respotenciay)

                auxraiz = respotenciax + respotenciay
                print(auxraiz)

                distancia = distancia + raiz(auxraiz)

                auxladox = ladox
                auxladoy = ladoy

    print("La distancia es: ", distancia)   

else:
    input("Ingresar un numero mayor a 3")