
A = input().split()
numero_niños = int(A[0])
peso_max = int(A[1])

pesos = list(map(int, input().split()))
pesos_ordenados = sorted(pesos)

gondolas = 0

izquierda = 0
derecha = numero_niños - 1

while izquierda <= derecha:
    if pesos_ordenados[izquierda] + pesos_ordenados[derecha] <= peso_max:
        izquierda += 1  
        derecha -= 1  
    else:
        derecha -= 1  

    gondolas += 1 

print(gondolas)