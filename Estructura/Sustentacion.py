import numpy as np

def calcular_probabilidad_transicion(estado_actual, estado_siguiente):
  """
  Calcula la probabilidad de transición de un estado a otro.

  Args:
    estado_actual: El estado actual del sistema.
    estado_siguiente: El estado siguiente del sistema.

  Returns:
    La probabilidad de transición de estado_actual a estado_siguiente.
  """
  # Se carga la matriz de probabilidades del sistema.
  matriz_probabilidades = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.07, 0.02, 0.91, 0, 0, 0, 0],
    [0, 0.03, 0.97, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
  ])

  # Se obtiene la probabilidad de transición de la matriz.
  probabilidad_transicion = matriz_probabilidades[estado_actual, estado_siguiente]

  return probabilidad_transicion

def calcular_probabilidad_estado_siguiente(estado_actual):
  """
  Calcula la probabilidad de cada estado posible en el siguiente paso.

  Args:
    estado_actual: El estado actual del sistema.

  Returns:
    Un diccionario con las probabilidades de cada estado posible en el siguiente paso.
  """
  probabilidades_estado_siguiente = {}

  for estado_siguiente in range(8):
    probabilidad_transicion = calcular_probabilidad_transicion(estado_actual, estado_siguiente)
    probabilidades_estado_siguiente[estado_siguiente] = probabilidad_transicion

  return probabilidades_estado_siguiente

def calcular_perdida_sistema_candidato(estado_sistema_candidato, estado_sistema_general):
  """
  Calcula la pérdida del sistema candidato para un estado particular del sistema general.

  Args:
    estado_sistema_candidato: El estado del sistema candidato (A, B y C).
    estado_sistema_general: El estado del sistema general (ABCD, D, A, B, C, AB, AC, BC).

  Returns:
    La pérdida del sistema candidato.
  """
  estado_deseado = np.array([1, 1, 1])
  diferencia_estado = estado_deseado - estado_sistema_candidato
  perdida = np.sum(diferencia_estado)

  return perdida

def evaluar_minima_perdida(estado_sistema_candidato):
  """
  Evalúa la mínima pérdida del sistema candidato para todos los estados posibles del sistema general.

  Args:
    estado_sistema_candidato: El estado del sistema candidato (A, B y C).
  """
  perdidas_estado_general = {}

  for estado_sistema_general in range(16):
    perdida_sistema_candidato = calcular_perdida_sistema_candidato(estado_sistema_candidato, estado_sistema_general)
    perdidas_estado_general[estado_sistema_general] = perdida_sistema_candidato

  # Se identifica la mínima pérdida y los estados del sistema general que la producen.
  minima_perdida = min(perdidas_estado_general.values())
  estados_minima_perdida = [key for key, value in perdidas_estado_general.items() if value == minima_perdida]

  print(f"Mínima pérdida del sistema candidato: {minima_perdida}")
  print(f"Estados del sistema general que producen la mínima pérdida: {estados_minima_perdida}")

# Ejemplo de uso
estado_sistema_candidato = np.array([0, 1, 1])  # Estado actual del sistema candidato (A, B y C)

evaluar_minima_perdida(estado_sistema_candidato)

#punto 1
estado_actual = np.array([0, 1, 1])  # Estado actual del sistema (A, B y C)
probabilidades_estado_siguiente = calcular_probabilidad_estado_siguiente(estado_actual)
probabilidad_abc_siguiente = probabilidades_estado_siguiente[7]  # Índice 7 corresponde a ABC = 111
print(f"P(ABCt+1 | ABCt) = {probabilidad_abc_siguiente}")

#punto 2
#estado_actual = np.array([0, 1, 1])  # Estado actual del sistema (A, B y C)
#probabilidad_ab_actual = calcular_probabilidad_estado_siguiente(estado_actual)[1]  # Índice 1 corresponde a AB = 01
#probabilidad_ac_siguiente = calcular_probabilidad_transicion(estado_actual, [0, 1, 0])[6]
# Índice 6 representa AC = 110
#probabilidad_ab_y_ac_siguiente = probabilidad_ab_actual * probabilidad_ac_siguiente
#probabilidad_ac_dado_ab = probabilidad_ab_y_ac_siguiente / probabilidad_ab_actual
#print(f"P(ACt+1 | ABt) = {probabilidad_ac_dado_ab}")

#punto 3
#estado_actual = np.array([0, 1, 1])  # Estado actual del sistema (A, B y C)
# Se calculan las probabilidades de cada estado del conjunto y las probabilidades del evento condicional para cada evento.
# Este proceso requiere de la matriz de probabilidades del sistema condicionada a cada estado ABCt.
# Se realiza la suma de las probabilidades condicionales ponderadas por las probabilidades de cada estado del conjunto.
#probabilidad_ac_dado_abc = ...  # Resultado de la suma
#print(f"P(ACt+1 | ABCt) = {probabilidad_ac_dado_abc}")
