class Arco:
  """
  Clase para representar un arco en un grafo.

  Atributos:
    id_nodo_inicio: Identificador del nodo inicial del arco.
    id_nodo_fin: Identificador del nodo final del arco.
    tipo_linea: Tipo de línea del arco (dirigido, no dirigido).
    color: Color del arco (utilizado para visualización).
    peso: Peso del arco (utilizado para algoritmos de grafos).

  Métodos:
    agregar(id_nodo_inicio, id_nodo_fin, tipo_linea, color, peso): Agrega un nuevo arco a la estructura.
    editar(tipo_linea_nuevo, color_nuevo, peso_nuevo): Edita el tipo de línea, color y peso del arco actual.
    eliminar(): Elimina el arco actual de la estructura.
  """

  def __init__(self,id_arco, id_nodo_inicio, id_nodo_fin, tipo_linea, color, peso):
    """
    Constructor de la clase Arco.

    Parámetros:
      id_nodo_inicio: Identificador del nodo inicial del arco.
      id_nodo_fin: Identificador del nodo final del arco.
      tipo_linea: Tipo de línea del arco (dirigido, no dirigido).
      color: Color del arco (utilizado para visualización).
      peso: Peso del arco (utilizado para algoritmos de grafos).
    """
    self.id_arco = id_arco
    self.id_nodo_inicio = id_nodo_inicio
    self.id_nodo_fin = id_nodo_fin
    self.tipo_linea = tipo_linea
    self.color = color
    self.peso = peso

  def editar_arco(self, tipo_linea_nuevo, color_nuevo, peso_nuevo):
    """
    Función para editar el tipo de línea, color y peso del arco actual.

    Parámetros:
      tipo_linea_nuevo: Nuevo tipo de línea del arco.
      color_nuevo: Nuevo color del arco.
      peso_nuevo: Nuevo peso del arco.
    """
    self.tipo_linea = tipo_linea_nuevo
    self.color = color_nuevo
    self.peso = peso_nuevo
