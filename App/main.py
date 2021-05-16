import numpy as np
N = 0
ciudades = ["C1"]
ciudadesp = 'C1'
print('Bienvenido al algoritmo del viajero! \n')

while(N < 4 or N%2 != 0):
    N = int(input("Ingrese el número de ciudades a recorrer: "))
    if(N<4 or N%2 != 0):
        print("N debe ser mayor o igual a 4 y un número par!")
print('Ciudades: ')
for i in range(N-1):
  ciudadesp = (ciudades + ', C' + str(i+2))
print(ciudadesp)
print(' \n')
print('Distancia de ciudades')
matriz = np.random.randint(99, size=(N, N)) + 1

#Crear NODOS

#Crear árbol

#Función que le asigna 0 a la distancia de una ciudad a sí misma (diagonal de ceros)
for x in range(N):
  for y in range(N):
    if(x == y):
      matriz[x][y] = 0
print(matriz)
print(' \n')

def algoritmoDFS(listaCiudades, matrizDistancias):
  nodo1 = NodoCiudad()
algoritmoDFS()