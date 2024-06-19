from Estructura.Grafo import Grafo
from Estructura.Nodo import Nodo
from Estructura.Arco import Arco
import collections
class Bipartito:
  """
  Esta clase determina si un grafo dirigido o no dirigido es bipartito.

  Atributos:
    grafo: Objeto de la clase `Grafo` que contiene el grafo a analizar.

  Métodos:
    es_bipartito_bfs(): Determina si el grafo es bipartito usando búsqueda en anchura (BFS).
    es_bipartito_dfs(): Determina si el grafo es bipartito usando búsqueda en profundidad (DFS).
  """

  def __init__(self, grafo):
    """
    Inicializa la clase con el grafo a analizar.

    Args:
      grafo: Objeto de la clase `Grafo` que contiene el grafo a analizar.
    """
    self.grafo = grafo

  def es_bipartito_bfs(self):
    """
    Determina si el grafo es bipartito usando búsqueda en anchura (BFS).

    Devuelve:
      True si el grafo es bipartito, False en caso contrario.
    """
    visitados = set()  # Conjunto de nodos visitados
    colores = {}  # Diccionario para almacenar el color asignado a cada nodo

    for nodo in self.grafo.nodos:
      if nodo.id_nodo not in visitados:
        if self._bfs(nodo.id_nodo, colores, visitados):
          return False  # Se encontró un ciclo impar, el grafo no es bipartito

    return True  # No se encontraron ciclos impares, el grafo es bipartito

  def _bfs(self, nodo_inicial, colores, visitados):
    """
    Auxiliar para la función `es_bipartito_bfs`. Realiza la búsqueda en anchura.

    Args:
      nodo_inicial: Nodo inicial para la búsqueda.
      colores: Diccionario para almacenar el color asignado a cada nodo.
      visitados: Conjunto de nodos visitados.

    Devuelve:
      True si se encuentra un ciclo impar, False en caso contrario.
    """
    cola = collections.deque([nodo_inicial])
    color_actual = 1  # Color inicial para asignar

    while cola:
      nodo_actual = cola.popleft()
      if nodo_actual in colores:
        # Se encontró un nodo con un color diferente al esperado, hay un ciclo impar
        return True

      colores[nodo_actual] = color_actual

      for vecino in self.grafo.adyacentes[nodo_actual]:
        if vecino not in visitados:
          visitados.add(vecino)
          cola.append(vecino)
          color_actual = (color_actual + 1) % 2  # Alternar color para el siguiente nodo

    return False

  def es_bipartito_dfs(self):
    """
    Determina si el grafo es bipartito usando búsqueda en profundidad (DFS).

    Devuelve:
      True si el grafo es bipartito, False en caso contrario.
    """
    visitados = set()  # Conjunto de nodos visitados
    colores = {}  # Diccionario para almacenar el color asignado a cada nodo

    for nodo in self.grafo.nodos:
      if nodo.id_nodo not in visitados:
        if self._dfs(nodo.id_nodo, colores, visitados):
          return False  # Se encontró un ciclo impar, el grafo no es bipartito

    return True  # No se encontraron ciclos impares, el grafo es bipartito

  def _dfs(self, nodo_inicial, colores, visitados):
    """
    Auxiliar para la función `es_bipartito_dfs`. Realiza la búsqueda en profundidad.

    Args:
      nodo_inicial: Nodo inicial para la búsqueda.
      colores: Diccionario para almacenar el color asignado a cada nodo.
      visitados: Conjunto de nodos visitados.

    Devuelve:
      True si se encuentra un ciclo impar, False en caso contrario.
    """
    visitados.add(nodo_inicial)

    for vecino in self.grafo.adyacentes[nodo_inicial]:
      if vecino in visitados:
        # Se encontró un ciclo impar
        return True

      if vecino not in colores:
        # Asignar color opuesto al padre (si existe)
        color_padre = colores.get(nodo_inicial)
        color_actual = 1 if color_padre is None else color_padre ^ 1
        if self._dfs(vecino, colores, visitados):
          return True

    return False
