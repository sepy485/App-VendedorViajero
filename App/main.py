import numpy as np
import time
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
  ciudadesp = (ciudadesp + ', C' + str(i+2))
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

#Función que retorna la distancia entre 2 ciudades
def calcularDistancia(ciudad1, ciudad2, matriz):
  distancia = (matriz[ciudad1][ciudad2])
  return distancia
      
print(str(calcularDistancia(0,3,matriz)))

print("Tiempo transcurrido: " + str(time.process_time()) + " [sg]")



def algoritmoDFS(listaCiudades, matrizDistancias, N, resultado):
  nodo1 = listaCiudades[0] #toma cualquier ciudad para iniciar, en este caso la primera
  nodo1.setVisitado(True)
  listaConectados = nodo1.getConectados() #toma las ciudades conectadas
  i = 0
  while((listaConectados[i].getVisitado) and (i < len(listaConectados))):
    i = i+1
  #Si se llegó al final de la lista finaliza  
  if(i == N):
    resultado = resultado + " Fin."
    print("El resultado es: " + str(resultado))
    print("Tiempo transcurrido: " + str(time.process_time()) + " [sg]")
  #Si no ha terminado con la lista
  else:
    nodo2 = listaConectados[i]
    resultado = nodo1.getNombre() + " => " + str(calcularDistancia(nodo1,nodo2,matriz)) + " => " + algoritmoDFS(listaConectados, matrizDistancias, N, resultado)
  return resultado

