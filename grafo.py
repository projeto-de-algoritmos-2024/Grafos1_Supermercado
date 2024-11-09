from collections import deque


class Grafo:

    # inicializa grafo
    def __init__(self, grafo=None):
        # inicializa novo grafo vazio se não encontrar grafo existente
        if grafo is None:
            grafo = {}
        # grafo = dicionário já criado
        self.grafo = grafo

    def mostra_grafo(self):
        # printa o dicionário que contém as conexões entre cada vértice, como uma lista encadeada
        print(self.grafo)
        # printa qtd de vertices
        print(len(self.grafo))

    def busca_largura(self, inicio, fim):
        arvore_busca = []
        visitados = []
        fila = deque([inicio])
        fila.append(inicio)
        visitados.append(inicio)
        while (fila):
            vertice = fila.popleft()
            for vizinho in self.grafo.get(vertice, []):
                if vizinho == fim:
                    arvore_busca.append((vertice, vizinho))
                    visitados.append(vizinho)
                    return arvore_busca
                elif not (vizinho in visitados):
                    arvore_busca.append((vertice, vizinho))
                    visitados.append(vizinho)
                    fila.append(vizinho)

