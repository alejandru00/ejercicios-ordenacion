
""" 
He hecho los dos progranas pq no sabía si sorted se considera como estructura adicional
"""

caso_prueba = int(input())

for _ in range(caso_prueba):                        

    num_nombres = int(input())
    num_nombres_distintos = 0

    nombres = list(map(int, input().split()))
    nombres_ordenados = sorted(nombres)

    for i in range(num_nombres - 1):
        if nombres_ordenados[i] != nombres_ordenados[i + 1]:
            num_nombres_distintos += 1

    num_nombres_distintos += 1 

    print(num_nombres_distintos)