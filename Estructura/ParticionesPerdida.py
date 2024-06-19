import networkx as nx

def particiones_con_perdida(grafo, nodos_presentes, nodos_futuros):
  """
  Encuentra todas las posibles particiones del grafo con sus valores de pérdida.

  Args:
    grafo: Un objeto NetworkX que representa el grafo.
    nodos_presentes: Una lista de nodos que pertenecen a la partición presente.
    nodos_futuros: Una lista de nodos que pertenecen a la partición futuro.

  Returns:
    Un diccionario que mapea cada partición a su valor de pérdida.
  """
  particiones = []
  perdida_particiones = {}

  # Crear subgrafos para cada partición
  subgrafo_presente = grafo.subgraph(nodos_presentes)
  subgrafo_futuro = grafo.subgraph(nodos_futuros)

  # Calcular la pérdida para cada partición
  for arista in grafo.edges:
    nodo_inicio, nodo_fin = arista
    if nodo_inicio in nodos_presentes and nodo_fin in nodos_futuros:
      peso_arista = grafo[nodo_inicio][nodo_fin]["weight"]
      perdida_particiones[particion] += peso_arista

  # Agregar la partición y su valor de pérdida al diccionario
  particiones.append((nodos_presentes, nodos_futuros))
  perdida_particiones[particion] = perdida

  # Generar todas las particiones posibles mediante backtracking
  for nodo in nodos_futuros:
    nuevos_nodos_presentes = nodos_presentes + [nodo]
    nuevos_nodos_futuros = [n for n in nodos_futuros if n != nodo]
    sub_particiones = particiones_con_perdida(grafo, nuevos_nodos_presentes, nuevos_nodos_futuros)
    particiones.extend(sub_particiones.keys())
    perdida_particiones.update(sub_particiones)

  return perdida_particiones

# Ejemplo de uso
grafo = nx.Graph()
grafo.add_nodes(["A", "B", "C"])
#grafo.add_edges(["A", "B", weight=1], ["A", "C", weight=2], ["B", "C", weight=3])

nodos_presentes = ["A"]
nodos_futuros = ["B", "C"]

particiones_y_perdida = particiones_con_perdida(grafo, nodos_presentes, nodos_futuros)

print(particiones_y_perdida)
