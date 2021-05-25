import numpy as np
from Ciudad import Ciudad
import time

#Variables
N = 0 #Cantidad de ciudades INPUT
listaCiudades = []


#Inicio del programa
print('Bienvenido al algoritmo del viajero! \n')
while(N < 4 or N%2 != 0):
    N = int(input("Ingrese el número de ciudades a recorrer: "))
    if(N<4 or N%2 != 0):
        print("N debe ser mayor o igual a 4 y un número par!")
        
#Rellena una lista con las ciudades
for i in range(N):
  nombre = 'C' + str(i)
  listaCiudades.append(Ciudad(i,nombre))

print(' \n')

#Generamos una matriz de números aleatorios entre 1 y 100 para simular las distancias
matriz = np.random.randint(99, size=(N, N)) + 1

#Función que le asigna 0 a la distancia de una ciudad a sí misma (diagonal de ceros)
for x in range(N):
  for y in range(N):
    if(x == y):
      matriz[x][y] = 0
      
#Muestra la matriz de distancias entre ciudades
print('Distancia de ciudades')
print(matriz)
print(' \n')

#Función que retorna la distancia entre 2 ciudades
def calcularDistancia(ciudad1, ciudad2, matriz):
  distancia = (matriz[ciudad1][ciudad2])
  return distancia
      
#AlgoritmoDFS (recursivo) que calcula el camino que toma el viajero
def algoritmoDFS(listaCiudades, matrizDistancias, N, resultado):
  nodo1 = listaCiudades[0] #toma cualquier ciudad para iniciar, en este caso la primera de la lista
  nodo1.setVisitado(True) #Marca la ciudad como visitada
  listaConectados = listaCiudades #toma las ciudades conectadas
  listaConectados.pop(0) #Quitamos de la lista la ciudad visitada
  i = len(listaConectados)
 
  #Si se llegó al final de la lista finaliza  
  if(i <= 0):
    resultado = resultado + " Fin."
    print("El resultado es: " + str(resultado))
    print("Tiempo transcurrido: " + str(time.process_time()) + " [sg]")
    return resultado
  #Si no ha terminado con la lista entonces continúa
  else:
    nodo2 = listaConectados[0]
    resultado = resultado + nodo1.getNombre() + " => " + str(calcularDistancia(nodo1.getNumero(),nodo2.getNumero(),matriz)) + " => "
    algoritmoDFS(listaConectados, matrizDistancias, N, resultado)
    return resultado

#Se ejecuta el algoritmo
algoritmoDFS(listaCiudades, matriz, N, '')
