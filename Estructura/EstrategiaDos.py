import networkx as nx

class EstrategiaDos:

    def particion_minima(self, grafo, arco_eliminar):
        """
            Encuentra la partición mínima del sistema representado por el grafo dirigido.
            Args:
                grafo: El grafo dirigido que representa el sistema.
                arco_eliminar (float): El id del arco que vamos a eliminar.
            Returns:
                list: Una lista de subconjuntos disjuntos que representan la partición del sistema,
                o None si no se encuentra una partición.
        """
        # Inicializar variables
        tolerancia = 50
        arcos_extraidos = set()
        perdida_acumulada = 0

        # Iterar sobre los arcos del grafo
        for arco in grafo.arcos:
            # Eliminar el arco y evaluar la pérdida de información
            if arco_eliminar is arco.id_arco:
                copia_grafo = grafo
                if self.eliminar_arco_y_evaluar(copia_grafo, arco, tolerancia):
                    # Marcar el arco como removible
                    arcos_extraidos.add(arco.id_arco)

                    # Actualizar la pérdida de información acumulada
                    perdida_acumulada += self.perdida_informacion(copia_grafo,arco)

                    # Verificar si se ha generado una partición
                    if self.es_particion(grafo):
                        # Partir el grafo en subconjuntos disjuntos
                        subgrafo = self.particion_grafo(grafo)

                        # Eliminar los arcos removibles del grafo original
                        for arcos in arcos_extraidos:
                            grafo.eliminar_arco(arcos)

                        # Devolver la partición del sistema
                        return subgrafo
                    return arcos_extraidos, perdida_acumulada
        # Si no se encuentra una partición, devolver None
        return None

    def eliminar_arco_y_evaluar(self, grafo, arco, tolerancia):
        """
            Elimina un arco del grafo y evalúa la pérdida de información causada por la eliminación.
            Args:
                grafo: El grafo dirigido que representa el sistema.
                arco_eliminar: representa el arco a eliminar .
                tolerancia (float): El umbral de tolerancia para la pérdida de información.

            Returns:
                bool: True si la pérdida de información es menor o igual al umbral de tolerancia,
                False en caso contrario.
        """
        # Eliminar el arco del grafo
        grafo.eliminar_arco(arco.id_arco)

        # Calcular la pérdida de información
        perdida = self.perdida_informacion(grafo,arco)

        # Evaluar la pérdida de información
        if perdida <= tolerancia:
            return True
        else:
            return False

    # Definir la función de pérdida de información
    def perdida_informacion(self, grafo, arco):
        """
        Calcula la pérdida de información causada por la eliminación de un arco en un grafo personalizado.

        Args:
            grafo: El grafo dirigido que representa el sistema.
            arco (tuple): La tupla que representa el arco a eliminar.

        Returns:
            float: La pérdida de información, representada por la suma de los grados de los nodos del arco eliminado.
        """

        # Obtener los nodos del arco
        id_nodo_inicio = arco.id_nodo_inicio
        id_nodo_fin = arco.id_nodo_fin
        nodo_inicio = None
        nodo_fin = None
        for nodo in grafo.nodos:
            if id_nodo_inicio is nodo.id_nodo:
                nodo_inicio = nodo
            if id_nodo_fin is nodo.id_nodo:
                nodo_fin = nodo

        # Calcular la pérdida de información (grado personalizado)
        grado_personalizado_inicio = self.contar_conexiones(nodo_inicio, grafo.adyacentes)
        grado_personalizado_fin = self.contar_conexiones(nodo_fin, grafo.adyacentes)
        perdida = grado_personalizado_inicio + grado_personalizado_fin

        # Devolver la pérdida de información
        print("Perdida de información: ",perdida)
        return perdida

    def contar_conexiones(self, nodo, adyacentes):
        """
        Cuenta el número de conexiones de un nodo en un grafo personalizado.

        Args:
            nodo (str): El nodo para el que se desea contar las conexiones.
            adyacentes (list): La lista de adyacentes del grafo (nodos inicio y fin).

        Returns:
            int: El número de conexiones del nodo.
        """

        conexiones = 0
        for adyacente in adyacentes.keys():
            if adyacente is nodo.id_nodo:
                conexiones += 1
            for a in adyacentes[adyacente]:
                if a is nodo.id_nodo:
                    conexiones += 1
        return conexiones

    def es_particion(self, grafo):
        """
        Verifica si un grafo dirigido es acíclico utilizando el algoritmo de Tarjan.

        Args:
            grafo (dict): Un diccionario que representa el grafo,
            donde las claves son los nodos y los valores son listas de adyacentes.

        Returns:
            bool: True si el grafo es acíclico, False en caso contrario.
        """

        apilado = []
        bajo_agua = set()
        discovery_time = {}  # Almacena el tiempo de descubrimiento para cada nodo
        low_time = {}  # Almacena el tiempo de bajo nivel para cada nodo

        def dfs(nodo, tiempo_global):
            if nodo in discovery_time:
                return  # Ya se ha visitado el nodo

            discovery_time[nodo] = low_time[nodo] = tiempo_global
            tiempo_global += 1

            apilado.append(nodo)
            bajo_agua.add(nodo)

            for adyacente in grafo.adyacentes[nodo.id_nodo]:
                for nodos in grafo.nodos:
                    if nodos.id_nodo is adyacente:
                        if nodos not in discovery_time:
                            dfs(nodos, tiempo_global)
                        elif nodos in bajo_agua:  # Se encontró una arista de retorno
                            low_time[nodo] = min(low_time[nodo], low_time[nodos])
                        else:  # Arista hacia un nodo ya visitado
                            pass

            if low_time[nodo] == discovery_time[nodo]:  # Se encontró un ciclo
                ciclo = []
                while True:
                    nodo_actual = apilado.pop()
                    bajo_agua.remove(nodo_actual)
                    ciclo.append(nodo_actual)

                    if nodo_actual == nodo:
                        break
                print("ciclo: ",ciclo)
                return ciclo

        tiempo_global = 0
        for nodo in grafo.nodos:
            if nodo not in discovery_time:
                ciclo = dfs(nodo, tiempo_global)
                print("Tiempo global: ",tiempo_global)
                if ciclo:
                    return False

        return True

    def particion_grafo(self, grafo):
        """
            Parte un grafo dirigido en subconjuntos disjuntos.
            Args:
                grafo (nx.DiGraph): El grafo dirigido que representa el sistema.
            Returns:
                list: Una lista de subconjuntos disjuntos que representan la partición del sistema.
        """
        subgraphs = []
        for subgraph in nx.connected_components(grafo):
            subgraphs.append(list(subgraph))
        return subgraphs

