
num_peliculas = int(input())

peliculas = []

for i in range(num_peliculas):
    inicio, fin = map(int, input().split())
    peliculas.append((inicio, fin))

peliculas_por_entrada = sorted(peliculas, key = lambda x:x[0])
peliculas_por_salida = sorted(peliculas, key = lambda x:x[1])

horario_actual = 0 
peliculas_vistas = 0

for i in peliculas:
    if peliculas_por_salida[i] > peliculas_por_entrada[i]:
        peliculas_por_entrada.remove(peliculas_por_entrada[i])

    else: 
        for i in peliculas:
            if (peliculas_por_entrada[i][0] - peliculas_por_entrada[0][1])  > (peliculas_por_entrada[i+1][0] - peliculas_por_entrada[0][i+1]):
                peliculas_vistas += 1
            else:
                peliculas_por_entrada.remove(peliculas_por_entrada[i])

print(peliculas_vistas)


"""
Ni idea como se hace, si pillas por hora de entrada podria ser que pillases la mas larga, 
si lo haces por hora de salida dps no puedes comparar que hora de entrada esta mas cerca; 
y si lo haces, no se como hacer para calcular cual tiene la menor diferencia de horas y encontrarla en la lista de entradas.
Osea, que diria que no vale con este codigo de chat gpt que se ve que tmb se lo ha dado a mas gente de:

            num_peliculas = int(input())

            peliculas = []

            for _ in range(num_peliculas):
                inicio, fin = map(int, input().split())
                peliculas.append((inicio, fin))

            # Ordena la lista de películas por la hora de finalización
            peliculas.sort(key=lambda x: x[1])

            horario_actual = 0  # Inicialmente, no has visto ninguna película
            peliculas_vistas = 0  # Inicialmente, no has visto ninguna película

            for pelicula in peliculas:
                if pelicula[0] >= horario_actual:
                    # Puedes ver esta película
                    horario_actual = pelicula[1]  # Actualiza el horario actual
                    peliculas_vistas += 1

            print(peliculas_vistas)

            

El mio, no he llegado a runearlo, igual, no me da tiempo.
"""