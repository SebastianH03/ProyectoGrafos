#Libreria a utilizar
import numpy as np

#Clase grafo
class Grafo:

  #Inicializamos el grafo con una lista de vertices y de lados vacíos
  def __init__(self, vertices = [], lados = []):
    self.vertices = vertices
    self.lados = lados

  #Printear el grafo
  def __str__(self):
    return f"El grafo tiene los vertices = {self.vertices} y de lados = {self.lados}"

  #Añade un nodo al grafo
  def agregNodo(self, vertice):
    self.vertices.append(vertice)

  #Agrega un lado al grafo
  def agregLado(self, *lado):
    self.lados.append(lado)
    for i in lado:
      self.agregNodo(i)

  #Eliminar un lado
  def eliminarLado(self, e, v):
    if len(self.lados) != 0:
      i = 0
      for l in self.lados:
        if l[0] == e and l[1] == v:
          self.lados.pop(i)
          break
        i += 1

  #Guarda los vecinos de un nodo dado
  def vecinos(self, vertice):
    vecinos = set()
    for i in self.lados:
      if vertice == i[0]:
        vecinos.add(i[1])
      elif vertice == i[1]:
        vecinos.add(i[0])
    return vecinos


#Subclase de pesos para nuestro grafo no dirigido
class GrafoPesos(Grafo):
  
    #Inicializar el subgrafo
    def __init__(self, vertices = [], lados = []):
      super().__init__(vertices, lados)
      self.pesos = dict.fromkeys(self.lados, np.inf)

    #Agregar pesos
    def agregPesos(self, verticeE, verticeS, peso):
      self.pesos[(verticeE, verticeS)] = peso
      self.pesos[(verticeS, verticeE)] = peso
      self.agregLado(verticeE, verticeS)

    #Muestra los pesos entre dos vértices conectados
    def peso(self, verticeE, verticeS):
      return self.pesos[(verticeE, verticeS)]