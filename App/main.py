import numpy as np
from Ciudad import Ciudad
from time import time

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
    #print("Tiempo transcurrido: " + str(time.process_time()) + " [sg]")
    return resultado
  #Si no ha terminado con la lista entonces continúa
  else:
    nodo2 = listaConectados[0]
    resultado = resultado + nodo1.getNombre() + " => " + str(calcularDistancia(nodo1.getNumero(),nodo2.getNumero(),matrizDistancias)) + " => "
    algoritmoDFS(listaConectados, matrizDistancias, N, resultado)
    return resultado

#Función que se encarga de ejecutar todo el proceso del programa
def funcionMain(N):
  new_n = N
  while new_n%2!=0 or new_n<4:
    new_n = int(input("Favor ingrese  un valor par mayor o igual a 4 y que sea PAR: "))
  start_time= time()
  print(start_time)
  listaCiudadesAux = []
  #Rellena una lista con las ciudades
  for i in range(new_n):
    nombre = 'C' + str(i+1)
    listaCiudadesAux.append(Ciudad(i,nombre))

  #Generamos una matriz de números aleatorios entre 1 y 100 para simular las distancias
  matriz = np.random.randint(99, size=(new_n, new_n)) + 1

  #Función que le asigna 0 a la distancia de una ciudad a sí misma (diagonal de ceros)
  for x in range(new_n):
    for y in range(new_n):
      if(x == y):
        matriz[x][y] = 0
  
  algoritmoDFS(listaCiudadesAux, matriz, new_n, '')
  elapsed_time = time()
  print(elapsed_time)
  dif = elapsed_time-start_time
  print(dif)

#Inicio y bienvenida formal del programa  
print('Bienvenido al algoritmo del viajero! \n')
N = int(input("Ingrese el número de ciudades a recorrer: "))
funcionMain(int(N))