import numpy as np
N = 4
ciudades = 'C1'
print('Bienvenido al algoritmo del viajero! \n')
N = int(input("Ingrese el número de ciudades a recorrer: "))
print('Ciudades: ')
for i in range(N-1):
  ciudades = (ciudades + ', C' + str(i+1))
print(ciudades)
print(' \n')
print('Distancia de ciudades')
matriz = np.random.randint(99, size=(N, N)) + 1

#Función que le asigna 0 a la distancia de una ciudad a sí misma (diagonal de ceros)
for x in range(N):
  for y in range(N):
    if(x == y):
      matriz[x][y] = 0
print(matriz)
print(' \n')
