class Nodo:
  """
  Clase para representar un nodo en una estructura de datos.

  Atributos:
    dato: El dato almacenado en el nodo.
    siguiente: Referencia al siguiente nodo en la estructura.

  Métodos:
    agregar(dato): Agrega un nuevo nodo a la estructura.
    editar(dato_nuevo): Edita el dato del nodo actual.
    eliminar(): Elimina el nodo actual de la estructura.
  """

  def __init__(self, id_nodo, valor, color,etiqueta, x , y):
    """
    Constructor de la clase Nodo.

    Parámetros:
      id_nodo: Identificador único del nodo.
      peso: Peso del nodo.
      color: Color del nodo (utilizado para algoritmos de búsqueda).
      vecinos: Diccionario que almacena los nodos vecinos y el costo de llegar a ellos.
    """
    self.id_nodo = id_nodo
    self.valor = valor
    self.color = color
    self.etiqueta = etiqueta
    self.x = x
    self.y = y

  def editar_nodo(nodo, nuevo_color,nueva_etiqueta, nuevo_valor):
    """
    Función para editar el color y el peso de un nodo.

    Parámetros:
      nodo: El nodo a editar.
      nuevo_color: El nuevo color del nodo.
      nuevo_peso: El nuevo peso del nodo.
    """
    nodo.color = nuevo_color
    nodo.etiqueta = nueva_etiqueta
    nodo.valor = nuevo_valor