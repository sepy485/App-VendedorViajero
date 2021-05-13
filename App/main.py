import numpy as np
N = 4
N = int(input("Ingrese el número de ciudades a recorrer: "))
print('Algoritmo del viajero! \n')
print('Ciudades: \n')
for i in range(N):
  print('C' + str(i+1))

print(' \n')
print('Distancia de ciudades')
matriz = np.random.randint(99, size=(N, N)) + 1
print(matriz)
print(' \n')
#Función que le asigna 0 a la distancia de una ciudad a sí misma (diagonal de ceros)
for x in range(N):
  for y in range(N):
    if(x == y):
      matriz[x][y] = 0

print(matriz)