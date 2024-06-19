import Nodo
import Arco
class Grafo:
  """
  Clase para representar un grafo.

  Atributos:
    nodos: Diccionario que almacena los nodos del grafo, donde la clave es el ID del nodo y el valor es el objeto Nodo correspondiente.
    arcos: Lista que almacena los arcos del grafo.

  Métodos:
    agregar_nodo(self, id_nodo, peso, color, vecinos): Agrega un nuevo nodo al grafo.
    agregar_arco(self, id_nodo_inicio, id_nodo_fin, tipo_linea, color, peso): Agrega un nuevo arco al grafo.
    crear_grafo_personalizado(self, lista_nodos, lista_arcos): Crea un grafo personalizado a partir de listas de nodos y arcos.
    mostrar_grafo(self): Muestra una representación del grafo (formato a definir).
  """

  def __init__(self):
    self.nodos = []
    self.arcos = []
    self.adyacentes = {}

  def agregar_nodo(self, nodo_agregar):
    """
    Función para agregar un nuevo nodo a la estructura.

    Parámetros:


    El nuevo nodo agregado.
    """
    if nodo_agregar not in self.nodos:
      self.nodos.append(nodo_agregar)
      self.adyacentes[nodo_agregar.id_nodo] = []

  def eliminar_nodo_lista(lista_nodos, nodo_eliminar):
    """
    Función para eliminar un nodo de una lista de nodos.

    Parámetros:
      lista_nodos: La lista de nodos en la que se encuentra el nodo a eliminar.
      nodo_eliminar: El nodo a eliminar de la lista.
    """
    if nodo_eliminar in lista_nodos:
      lista_nodos.remove(nodo_eliminar)
    else:
      print(f"Error: El nodo {nodo_eliminar} no se encuentra en la lista.")

  def agregar_arco(self, arco_agregar):
    """
    Función para agregar un nuevo arco a la estructura.

    Parámetros:
    """
    if arco_agregar not in self.arcos:
      self.arcos.append(arco_agregar)
      self.adyacentes[arco_agregar.id_nodo_inicio].append(arco_agregar.id_nodo_fin)

  def eliminar_arco(self, arco_eliminar):
    """
    Función para eliminar el arco actual de la estructura.

    Parámetros:
      lista_nodos: La lista de nodos en la que se encuentra el nodo a eliminar.
      nodo_eliminar: El nodo a eliminar de la lista.
    """
    if arco_eliminar in self.arcos:
      self.lista_arcos.remove(arco_eliminar)
    else:
      print(f"Error: El arco {arco_eliminar} no se encuentra en la lista.")

  def adyacentes(self, id_nodo):
    if id_nodo in self.adyacentes:
      return self.adyacentes[id_nodo]
    else:
      return []

  def getAdyacentes(self):
    if len(self.adyacentes) > 0:
      return self.adyacentes
