
caso_prueba = int(input()) 

for _ in range(caso_prueba):
    num_nombres = int(input())
    nombres = list(map(int, input().split()))

    contador = {}

    for nombre in nombres:
        if nombre in contador:
            contador[nombre] += 1
        else:
            contador[nombre] = 1

    num_nombres_distintos = len(contador)

    print(num_nombres_distintos)




