#Librerias usadas
import statistics
import grafo
import copy

#Lista de Generos posibles
Generos = [ 
  "Accion", 
  "Romance", 
  "Fantasia", 
  "Ciencia Ficcion", 
  "Aventura", 
  "Documental", 
  "Terror", 
  "Suspenso",
  "Comedia",
  "Infantil",
  "SuperHero"
]

#Inicializamos el grafo no dirigido y con pesos
G = grafo.GrafoPesos()

#Creamos nodos de tipo Géneros
for i in Generos:
  G.agregNodo(i)
print(G.vertices)

#Clase película
class Pelicula():

  #Inicializar la película
  def __init__(self, Nombre, Generos,fecha):
        self.valoraciones = []
        self.nombre = Nombre
        self.generos = Generos
        self.fecha = fecha
        self.valoracion = 0
  #Printear la información acerca de la película      
  def __str__(self):
      if len(self.valoraciones) == 0:
          return f"Nombre: {self.nombre}\nFecha: {self.fecha}\nGeneros: {self.generos}\n\nLa Pelicula no tiene Valoraciones"
      else:
          return f"Nombre: {self.nombre}\nFecha: {self.fecha}\nGenero: {self.genero}\nValoracione: {self.valoracion}"
  #Da una valoración a la película
  def agregarValoraciones(self, n):
      self.valoraciones.append(n)
      self.valoracion = statistics.mean(self.valoraciones)

  #Toma el nombre de una película
  def getNombre(self):
      return self.nombre

  #Toma la fecha
  def getFecha(self):
      return self.fecha

  #Toma la valoración
  def getValoracion(self):
      return self.getValoracion

  #Toma Todas las valoraciones
  def getValoraciones(self):
      return self.valoraciones

  #Toma un género
  def getGenero(self):
      return self.genero


#Estas serán nuestras películas base, ya agregadas en el sistema
p1 = Pelicula("ToyStory",{"Accion":3, 
  "Romance":0, 
  "Fantasia":5, 
  "Ciencia Ficcion":0, 
  "Aventura":6, 
  "Documental":0, 
  "Terror":0, 
  "Suspenso":0,
  "Comedia":8, 
  "Infantil":10,
  "SuperHero":0}, 2000)
p2 = Pelicula("Batman", {"Accion":9, 
  "Romance":3, 
  "Fantasia":1, 
  "Ciencia Ficcion":3, 
  "Aventura":2, 
  "Documental":0, 
  "Terror":0, 
  "Suspenso":5,
  "Comedia":0, 
  "Infantil":0,
  "SuperHero":10}, 2010)
p3 = Pelicula("JojoRabbit", {"Accion":3, 
  "Romance":6, 
  "Fantasia":3, 
  "Ciencia Ficcion":0, 
  "Aventura":6, 
  "Documental":3, 
  "Terror":0, 
  "Suspenso":5,
  "Comedia":8, 
  "Infantil":0,
  "SuperHero":1}, 2018)
p4 = Pelicula("Alien", {"Accion":7, 
  "Romance":0, 
  "Fantasia":6, 
  "Ciencia Ficcion":8, 
  "Aventura":4, 
  "Documental":0, 
  "Terror":10, 
  "Suspenso":9,
  "Comedia":0, 
  "Infantil":0,
  "SuperHero":0}, 2010)
p5 = Pelicula("Emoji", {"Accion":0, 
  "Romance":1, 
  "Fantasia":2, 
  "Ciencia Ficcion":0, 
  "Aventura":8, 
  "Documental":0, 
  "Terror":0, 
  "Suspenso":0,
  "Comedia":9, 
  "Infantil":10,
  "SuperHero":0}, 2015)
p6 = Pelicula("JhonWick2", {"Accion":10, 
  "Romance":0, 
  "Fantasia":0, 
  "Ciencia Ficcion":0, 
  "Aventura":5, 
  "Documental":0, 
  "Terror":0, 
  "Suspenso":6,
  "Comedia":1, 
  "Infantil":0,
  "SuperHero":0}, 2000)

#Lista con las peliculas
Peliculas = [p1,p2,p3,p4,p5,p6]
Matriz = []


#Genera la matriz con valores de género
def GenerarMatriz():
  M = []
  for p in Peliculas:
    n = []
    for g in Generos:
      peso = p.generos[g]
      n.append(peso)
    M.append(n)
  return M

#Genera el grafo con los nodos a partir de las películas
def generarGrafo():
  for i in range(len(Matriz)):
    for j in range(len(Matriz[i])):
      G.agregPesos(Peliculas[i].getNombre(), Generos[j], Matriz[i][j])



listaVisitados={}

#Filtra las peliculas en el grafo, para no ver los géneros
def filtrarPeliculas(lista):
  resultado= []
  for i in lista:
    if i not in Generos and i not in resultado:
      resultado.append(i)
  return resultado

#Organiza la lista y coloca el nodo a iniciar de preferencia de primero en la lista
def organizarLista(lista, v):
  listafinal=[v]
  for i in lista:
    if i != v:
      listafinal.append(i)
  return listafinal

#Función para encontrar el peso menor en el grafo
def encontrarPesoMenor(G, s):
  pesos=[]
  for v in G.vecinos(s):
    pesos.append(G.peso(s, v))
  if len(pesos) == 0:
    return 0
  else:
    return min(pesos)

#Auxiliar de nuestra función basada en DFS
def JPS_aux(G, x, lista):
  lista.append(x)
  listaVisitados[x]=True
  vecinos=G.vecinos(x)
  minimo=encontrarPesoMenor(G, x)
  for e in vecinos:
    if len(G.lados) != 0:
      if G.peso(x,e) == minimo:
        G.eliminarLado(x,e)
        JPS_aux(G, e, lista)
        
#Función de búsqueda para recorrer el nodo con el camino de menor peso
def JPS(G1, s):
  resultado=[]
  G = copy.copy(G1)
  nodos = organizarLista(G.vertices, s)
  for v in nodos:
    listaVisitados[v]=False
  for x in nodos:
    if not listaVisitados[x]:
      JPS_aux(G, x, resultado)
  return resultado
activo = True

#Menú
while(activo):
    print("1. Agregar Pelicula")
    print("2. Listar Pelicula")
    print("3. Eliminar Pelicula")
    print("4. Agregar Valoracion")
    print("5. Generar Matriz")
    print("6. Generar Grafo")
    print("7. Recomendacion")
    print("0. Salir")
    
    opcion = int(input("Seleccione opcion : "))

    #Salir
    if opcion == 0:
        activo = False
    
    #Agrega una película al sistema    
    if opcion == 1:
        nombre = str(input("Digite el Nombre de la Pelicula : "))
        fecha = int(input("Digite la fecha de la Pelicula : "))
        print("Acontinuación digite un valor del 0 al 10 sobre el tipo de género de la película escogida: \n")
        dictValoracion={}
        for i in Generos:
          valor = int(input(i+" : "))
          dictValoracion[i] = valor
        p = Pelicula(nombre, dictValoracion, fecha)
        Peliculas.append(p)

    #Lista las películas
    if opcion == 2:
        print("\n")
        if len(Peliculas) != 0:
            for p in Peliculas:
                print(p)
                print("\n")
        else:
            print("No hay peliculas")
    
    #Elimina una película        
    if opcion == 3:
        indice = int(input("Digite el indice de la pelicula : "))
        Peliculas.pop(indice - 1)

    #Agrega una valoración
    if opcion == 4:
        print("Película que vas a valorar: \n")
        for i in range(len(Peliculas)):
          print(str(i + 1) + " : " + Peliculas[i].getNombre())
        indice = int(input("Digite el indice de la pelicula : "))
        valoracion = int(input("Digite la valoracion : "))
        Peliculas[indice - 1].agregarValoraciones(valoracion)

    #Genera la matriz para ver la recomendación
    if opcion == 5:
        Matriz = GenerarMatriz()
        print(Matriz)

    #Genera el grafo
    if opcion == 6:
        generarGrafo()
        print(G)

    #Busca una recomendación
    if opcion == 7:
        print("lista de películas que puedes escoger: ")
        for i in range(len(Peliculas)):
          print(str(i + 1) + " : " + Peliculas[i].getNombre())
        index = int(input("Escoge una película: "))
        print("Recomendaciones de menor a mayor para: " + Peliculas[index-1].getNombre() + "/n")
        print(filtrarPeliculas(JPS(G, Peliculas[index-1].getNombre())))
        print("================================================")
        print("La Película mejor recomendada para ti es: " + filtrarPeliculas(JPS(G, Peliculas[index-1].getNombre()))[1])
        print("Si te gustó: " + Peliculas[index-1].getNombre()+ " " + "Talvez te guste: " + filtrarPeliculas(JPS(G, Peliculas[index-1].getNombre()))[2])
