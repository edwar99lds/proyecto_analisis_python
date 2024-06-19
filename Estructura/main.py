from Estructura.Grafo import Grafo
from Estructura.Nodo import Nodo
from Estructura.Arco import Arco
from Estructura.Bipartito import Bipartito
from Estructura.EstrategiaDos import EstrategiaDos
from tkinter import *

class main:
  def __init__(self):
    """Función principal del programa."""

    self.app = Tk()
    self.app.title('Proyecto análisis')
    self.app.state('zoomed')
    self.frame = Frame(self.app)
    self.frame.pack(fill="both")
    self.frame.config(width=1360, height=760, bg='brown4')
    self.map = Canvas(self.frame, width=1360, height=760, bg='dim gray')
    self.map.place(x=250, y=0)

    # boton y campos de texto para crear nodo
    self.boton_nodo = Button(button=Button(self.frame, text="Agregar nodo",
                                       command=self.agregar_nodo).place(x=60, y=10))
    self.entrada1_id_nodo = StringVar()
    self.etiqueta_nodo = Label(self.frame, text="id_nodo").place(x=5, y=40)
    self.texto_nodo_id = Entry(self.frame, textvariable=self.entrada1_id_nodo).place(x=60, y=40)
    self.entrada2_valor = StringVar()
    self.etiqueta_nodo = Label(self.frame, text="valor").place(x=5, y=70)
    self.texto_nodo_valor = Entry(self.frame, textvariable=self.entrada2_valor).place(x=60, y=70)
    self.entrada3_color = StringVar()
    self.etiqueta_nodo = Label(self.frame, text="color").place(x=5, y=100)
    self.texto_nodo_color = Entry(self.frame, textvariable=self.entrada3_color).place(x=60, y=100)
    self.entrada4_etiqueta = StringVar()
    self.etiqueta_nodo = Label(self.frame, text="etiqueta").place(x=5, y=130)
    self.texto_nodo_etiqueta = Entry(self.frame, textvariable=self.entrada4_etiqueta).place(x=60, y=130)
    self.entrada5_x = StringVar()
    self.etiqueta_nodo = Label(self.frame, text="x").place(x=5, y=160)
    self.texto_nodo_x = Entry(self.frame, textvariable=self.entrada5_x).place(x=60, y=160)
    self.entrada6_y = StringVar()
    self.etiqueta_nodo = Label(self.frame, text="y").place(x=5, y=190)
    self.texto_nodo_y = Entry(self.frame, textvariable=self.entrada6_y).place(x=60, y=190)

    # boton y campos de texto para eliminar nodo
    self.boton_eliminar_nodo = Button(button=Button(self.frame, text="Eliminar nodo",
                                       command=self.eliminar_nodo).place(x=10, y=220))
    self.entrada_eliminar_nodo = StringVar()
    self.texto_arco_inicio = Entry(self.frame, textvariable=self.entrada_eliminar_nodo).place(x=110, y=220)

    # boton y campos de texto para crear arco
    self.boton2_arco = Button(button=Button(self.frame, text="Agregar arco",
                                       command=self.agregar_arco).place(x=60, y=250))
    self.entrada7_id_arco = StringVar()
    self.etiqueta_arco_id = Label(self.frame, text="id_arco").place(x=5, y=280)
    self.texto_arco_id = Entry(self.frame, textvariable=self.entrada7_id_arco).place(x=60, y=280)
    self.entrada8_id_nodo_inicio = StringVar()
    self.etiqueta_arco_inicio = Label(self.frame, text="id_inicio").place(x=5, y=310)
    self.texto_arco_inicio = Entry(self.frame, textvariable=self.entrada8_id_nodo_inicio).place(x=60, y=310)
    self.entrada9_id_nodo_fin = StringVar()
    self.etiqueta_arco_fin = Label(self.frame, text="id_fin").place(x=5, y=340)
    self.texto_arco_fin = Entry(self.frame, textvariable=self.entrada9_id_nodo_fin).place(x=60, y=340)
    self.entrada10_arco_tipo = StringVar()
    self.etiqueta_arco_tipo = Label(self.frame, text="tipo").place(x=5, y=370)
    self.texto_arco_tipo = Entry(self.frame, textvariable=self.entrada10_arco_tipo).place(x=60, y=370)
    self.entrada11_arco_color = StringVar()
    self.etiqueta_arco_color = Label(self.frame, text="color").place(x=5, y=400)
    self.texto_arco_color = Entry(self.frame, textvariable=self.entrada11_arco_color).place(x=60, y=400)
    self.entrada12_arco_peso = StringVar()
    self.etiqueta_arco_peso = Label(self.frame, text="peso").place(x=5, y=430)
    self.texto_arco_peso = Entry(self.frame, textvariable=self.entrada12_arco_peso).place(x=60, y=430)

    # boton y campos de texto para eliminar arco
    self.boton_eliminar_arco = Button(button=Button(self.frame, text="Eliminar arco",
                                       command=self.eliminar_arco).place(x=10, y=470))
    self.entrada_eliminar_arco= StringVar()
    self.texto_eliminar_arco = Entry(self.frame, textvariable=self.entrada_eliminar_arco).place(x=110, y=475)

    # boton grafo aleatorio
    self.boton_aleatorio = Button(button=Button(self.frame, text="Grafo aleatorio",
                                       command=self.pintar_nodos).place(x=60, y=520))

    # boton y campos de texto para elegir nodo origen
    self.boton_origen = Button(button=Button(self.frame, text="Nodo origen",
                                                    command=self.pintar_origen).place(x=10, y=550))
    self.entrada_origen = StringVar()
    self.texto_origen = Entry(self.frame, textvariable=self.entrada_origen).place(x=110, y=550)

    # botones para procesos
    self.boton_proceso1 = Button(button=Button(self.frame, text="Proceso Bipartito",
                                       command=self.grafo_bipartito).place(x=60, y=600))

    self.boton_proceso2 = Button(button=Button(self.frame, text="Proceso 2",
                                               command=self.pintar_tablero).place(x=60, y=630))

    self.boton_proceso3 = Button(button=Button(self.frame, text="Proceso 3",
                                               command=self.pintar_tablero).place(x=60, y=660))


    self.grafo1 = Grafo()

    # Procesar o utilizar la lista de nodos como se requiera
    # Puedes iterar sobre la lista, acceder a sus atributos, etc.

    # Crear un nodo
    self.nodo1 = Nodo(1, 10, "azure","A",200,80)
    self.nodo2 = Nodo(2, 50, "cyan","B",680,50)
    self.nodo3 = Nodo(3, 35, "pink", "C",200,350)
    self.nodo4 = Nodo(4, 80, "red", "D",650,370)
    self.nodo5 = Nodo(5, 68, "blue2", "E",400,550)

    # Agregar nodos a la lista
    self.grafo1.agregar_nodo(self.nodo1)
    self.grafo1.agregar_nodo(self.nodo2)
    self.grafo1.agregar_nodo(self.nodo3)
    self.grafo1.agregar_nodo(self.nodo4)
    self.grafo1.agregar_nodo(self.nodo5)

    # Crear un arco
    self.arco1 = Arco(1,1, 2, "normal", "gold", 3)
    self.arco2 = Arco(2,1, 3, "normal", "cyan", 4)
    self.arco3 = Arco(3,1, 4, "normal", "khaki1", 2)
    self.arco4 = Arco(4,1, 5, "normal", "yellow2", 7)
    self.arco5 = Arco(5,2, 3, "normal", "turquoise", 4)
    self.arco6 = Arco(6,2, 4, "normal", "lavender", 6)
    self.arco7 = Arco(7,2, 5, "normal", "bisque", 3)
    self.arco8 = Arco(8,3, 4, "normal", "blue", 5)
    self.arco9 = Arco(9,3, 5, "normal", "pink2", 8)
    self.arco10 = Arco(10,4, 5, "normal", "purple1", 6)

    # Agregar arcos a la lista
    self.grafo1.agregar_arco(self.arco1)
    self.grafo1.agregar_arco(self.arco2)
    self.grafo1.agregar_arco(self.arco3)
    self.grafo1.agregar_arco(self.arco4)
    self.grafo1.agregar_arco(self.arco5)
    self.grafo1.agregar_arco(self.arco6)
    self.grafo1.agregar_arco(self.arco7)
    self.grafo1.agregar_arco(self.arco8)
    self.grafo1.agregar_arco(self.arco9)
    self.grafo1.agregar_arco(self.arco10)

    self.estrategiaDos = EstrategiaDos()

    self.lista_arcos_extraidos = []
    self.total_perdida = 0

    for e in self.grafo1.nodos:
      print(f"Nodo {e.id_nodo}")
    for i in self.grafo1.arcos:
      print(f"Arco, inicio: {i.id_nodo_inicio} fin: {i.id_nodo_fin} con peso: {i.peso}")

    self.app.mainloop()

  def pintar_tablero(self):
    self.map.delete('all')
    self.map.update()

  def pintar_nodos(self):
    for e in self.grafo1.arcos:
      for i in self.grafo1.nodos:
        if e.id_nodo_inicio is i.id_nodo:
          for j in self.grafo1.nodos:
            if e.id_nodo_fin is j.id_nodo:
              self.map.create_line(i.x +30, i.y+30, j.x+30, j.y+30, width=8, fill=e.color)
              lx = (i.x - j.x) / 2
              ly = (i.y - j.y) / 2
              self.map.create_text(i.x - lx - 10,i.y - ly + 10,
                                   fill="navy", font="Times 15", text=str(e.peso))
              self.map.create_text(i.x - lx + 20,i.y - ly + 10,
                                   fill="navy", font="Times 15", text="id: "+str(e.id_arco))
    for e in self.grafo1.nodos:
      self.map.create_text(e.x + 5, e.y - 10, fill="navy", font="Times 15", text=str(e.etiqueta))
      self.map.create_text(e.x + 60, e.y - 10, fill="navy", font="Times 15", text=str(e.id_nodo))
      self.map.create_rectangle(e.x, e.y, e.x + 70, e.y + 70, fill=e.color)

  def pintar_origen(self):
    self.map.delete('all')
    self.map.update()
    id_nodo_origen = int(self.entrada_origen.get())
    for e in self.grafo1.nodos:
      if id_nodo_origen is e.id_nodo:
        self.map.create_rectangle(e.x - 30, e.y - 30, e.x -10, e.y-10, fill="red")
    self.pintar_nodos()

  def agregar_nodo(self):
    self.map.delete('all')
    self.map.update()
    id_nodo = int(self.entrada1_id_nodo.get())
    valor = self.entrada2_valor.get()
    color = self.entrada3_color.get()
    etiqueta = self.entrada4_etiqueta.get()
    x = int(self.entrada5_x.get())
    y = int(self.entrada6_y.get())
    nodo_nuevo = Nodo(id_nodo,valor,color,etiqueta,x,y)
    self.grafo1.agregar_nodo(nodo_nuevo)
    self.pintar_nodos()

  def eliminar_nodo(self):
    self.map.delete('all')
    id_nodo = int(self.entrada_eliminar_nodo.get())
    for e in self.grafo1.nodos:
      if id_nodo is e.id_nodo:
        self.grafo1.nodos.remove(e)
    for i in self.grafo1.arcos:
      if id_nodo is i.id_nodo_inicio:
        self.grafo1.arcos.remove(i)
      if id_nodo is i.id_nodo_fin:
        self.grafo1.arcos.remove(i)
    self.pintar_nodos()

  def agregar_arco(self):
    self.map.delete('all')
    self.map.update()
    id_arco = int(self.entrada7_id_arco.get())
    id_nodo_inicio = int(self.entrada8_id_nodo_inicio.get())
    id_nodo_fin = int(self.entrada9_id_nodo_fin.get())
    tipo = self.entrada10_arco_tipo.get()
    color = self.entrada11_arco_color.get()
    peso = int(self.entrada12_arco_peso.get())
    arco_nuevo = Arco(id_arco,id_nodo_inicio,id_nodo_fin,tipo,color,peso)
    self.grafo1.agregar_arco(arco_nuevo)
    self.pintar_nodos()

  def eliminar_arco(self):
    self.map.delete('all')
    id_arco = int(self.entrada_eliminar_arco.get())
    print("Adyacentes: ",self.grafo1.getAdyacentes())
    for i in self.grafo1.arcos:
      if id_arco is i.id_arco:
        arcos_extraidos, perdida = self.estrategiaDos.particion_minima(self.grafo1,id_arco)
        self.lista_arcos_extraidos.append(arcos_extraidos)
        self.total_perdida += perdida
        self.map.create_rectangle(800, 10, 1000, 200, fill="white")
        self.map.create_text(900, 50, fill="black", font="Times 15", text="Arcos extraidos: ")
        self.map.create_text(900, 80, fill="black", font="Times 15", text=self.lista_arcos_extraidos)
        self.map.create_text(900, 120, fill="black", font="Times 15", text="Perdida: ")
        self.map.create_text(900, 150, fill="black", font="Times 15", text=self.total_perdida)
        self.map.create_text(900, 180, fill="black", font="Times 15", text="Perdida significativa")
        self.grafo1.arcos.remove(i)
    self.pintar_nodos()

  def grafo_bipartito(self):
    self.map.create_rectangle(5, 550, 270, 700, fill="white")
    es_bipartito = Bipartito(self.grafo1)
    if (es_bipartito.es_bipartito_bfs()):
      print("Si es bipartito en anchura")
      self.map.create_text(120, 600, fill="black", font="Times 15", text="Si es bipartito en anchura")
    else:
      print("No es bipartito en anchura")
      self.map.create_text(130, 630, fill="black", font="Times 15", text="No es bipartito en anchura")
    if (es_bipartito.es_bipartito_dfs()):
      print("Si es bipartito en profundidad")
      self.map.create_text(120, 630, fill="black", font="Times 15", text="Si es bipartito en profundidad")
    else:
      print("No es bipartito en profundidad")
      self.map.create_text(130, 660, fill="black", font="Times 15", text="No es bipartito en profundidad")


main()