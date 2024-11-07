import tkinter as tk
from tkinter import messagebox
import lista_de_produtos
#import matplotlib.pyplot as plt

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



def menor_caminho (arvore):
    inicio = arvore[0][0]
    fim = arvore[-1][-1]
    #print(inicio)
    #print(fim)
    nova_arvore = []
    arvore.reverse()
    #print(arvore)
    for no in arvore:
        if (no[0] == inicio and no[1] == fim):
            nova_arvore.append(no)
            return nova_arvore
        elif no[1] == fim:
            fim = no[0]
            nova_arvore.append(no)

meu_grafo = {
    1:[2,3],
    2:[1,3,14,37],
    3:[1,2,4],
    4:[3,5],
    5:[4,6],
    6:[5,7],
    7:[6,8],
    8:[7,9],
    9:[8,10],
    10:[9,11],
    11:[10,12],
    12:[11,13],
    13:[12, 25],
    14:[2,15,34,35],
    15:[14,16,33,34,35],
    16:[15,17,32,33,34],
    17:[16,18,31,32,33],
    18:[17,19,30,31,32],
    19:[18,20,29,30,31],
    20:[19,21,28,29,30],
    21:[20,22,27,28,29],
    22:[21,23,26,27,28],
    23:[22,24,26,27],
    24:[23,25,39],
    25:[13,24],
    26:[22,23,27,39],
    27:[21,22,23,26,28],
    28:[20,21,22,27,29],
    29:[19,20,21,28,30],
    30:[18,19,20,29,31],
    31:[17,18,19,30,32],
    32:[16,17,18,31,33],
    33:[15,16,17,32,34],
    34:[14,15,16,33,35],
    35:[14,15,34,37],
    36:[37,40,64],
    37:[2,35,36],
    38:[39,49,62],
    39:[24,26,38],
    40:[36,41,50,51],
    41:[40,42,50,51,52],
    42:[41,43,51,52,53],
    43:[42,44,52,53,54],
    44:[43,45,53,54,55],
    45:[44,46,54,55,56],
    46:[45,47,55,56,57],
    47:[46,48,56,57,58],
    48:[47,49,57,58,59],
    49:[38,48,58,59],
    50:[40,41,51,64],
    51:[40,41,42,50,52],
    52:[41,42,43,51,53],
    53:[42,43,44,52,54],
    54:[43,44,45,53,55],
    55:[44,45,46,54,56],
    56:[45,46,47,55,57],
    57:[46,47,48,56,58],
    58:[47,48,49,57,59],
    59:[48,49,58,62],
    60:[63,64],
    61:[62,65],
    62:[38,59,61],
    63:[60,64,74],
    64:[36,50,60,63],
    65:[61,66],
    66:[65,67],
    67:[66,68],
    68:[67,69],
    69:[68,70],
    70:[69,71],
    71:[70,72],
    72:[71,73],
    73:[72,74],
    74:[63,73]
}

coordenadas_grafo={
    1:(50,75),
    2:(100,100),
    3:(100,50),
    4:(150,50),
    5:(200,50),
    6:(250,50),
    7:(300,50),
    8:(350,50),
    9:(400,50),
    10:(450,50),
    11:(500,50),
    12:(550,50),
    13:(600,50),
    14: (150, 100),
    15: (200, 100),
    16: (250, 100),
    17: (300, 100),
    18: (350, 100),
    19: (400, 100),
    20: (450, 100),
    21: (500, 100),
    22: (550, 100),
    23: (600, 100),
    24:(650,100),
    25:(650,50),
    26: (600, 150),
    27: (550, 150),
    28: (500, 150),
    29: (450, 150),
    30: (400, 150),
    31: (350, 150),
    32: (300, 150),
    33: (250, 150),
    34: (200, 150),
    35: (150, 150),
    36:(100, 200),
    37:(100, 150),
    38:(650, 200),
    39:(650,150),
    40: (150, 200),
    41: (200, 200),
    42: (250, 200),
    43: (300, 200),
    44: (350, 200),
    45: (400, 200),
    46: (450, 200),
    47: (500, 200),
    48: (550, 200),
    49: (600, 200),
    50: (150, 250),
    51: (200, 250),
    52: (250, 250),
    53: (300, 250),
    54: (350, 250),
    55: (400, 250),
    56: (450, 250),
    57: (500, 250),
    58: (550, 250),
    59: (600, 250),
    60:(50,275),
    61:(650, 300),
    62:(650, 250),
    63:(100, 300),
    64:(100, 250),
    65: (600, 300),
    66: (550, 300),
    67: (500, 300),
    68: (450, 300),
    69: (400, 300),
    70: (350, 300),
    71: (300, 300),
    72: (250, 300),
    73: (200, 300),
    74: (150, 300)
}

grafo = Grafo(meu_grafo)

def manipula_lista_compras(lista_produtos):
    
    lista_de_compras_grafo = []
    # separa por virgula
    lista_compras = [p.strip() for p in lista_produtos.split(",")]

    print("Produtos digitados:", lista_compras)

    for produto in lista_compras:
        for meu_produto in lista_de_produtos.meus_produtos:
            if lista_de_produtos.meus_produtos[meu_produto] == produto:
                lista_de_compras_grafo.append(meu_produto)
   
            #print(meu_produto) # chave
            #print(lista_de_produtos.meus_produtos[meu_produto]) # valor
    #print(lista_de_compras_grafo)
    return lista_de_compras_grafo

def desenha_caminho(caminho):
    #pinta os nos que estão no caminho de vermelho e os que não estão de cinza
    for node, (x, y) in coordenadas_grafo.items():
        color = "red" if node in caminho else "gray"
        canvas.create_oval(x-10, y-10, x+10, y+10, fill=color)
        canvas.create_text(x, y, text=str(node), fill="white")
    for node, neighbors in meu_grafo.items():
        x1, y1 = coordenadas_grafo[node]
        for neighbor in neighbors:
            x2, y2 = coordenadas_grafo[neighbor]
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

def gerenciador():
    # Pega os produtos digitados
    produtos_da_lista = entrada.get()  
    
    lista_grafo = manipula_lista_compras(produtos_da_lista)
    lista_grafo.append(60)
    caminho = []

    comeco = 1
    for produto in lista_grafo:
        x = grafo.busca_largura(comeco, produto)
        comeco = produto
        y = menor_caminho(x)
        y.reverse()
        caminho.append(y)

    # Transformando a lista de listas de tuplas em uma lista única de elementos
    lista_unica = [elemento for sub_caminho in caminho for tupla in sub_caminho for elemento in tupla]

    # Removendo duplicados consecutivos
    caminho_final = [lista_unica[0]]
    for item in lista_unica[1:]:
        if item != caminho_final[-1]:
            caminho_final.append(item)

    print(caminho_final)
    desenha_caminho(caminho_final)

#grafo.mostra_grafo()

# arvore_resposta = grafo.busca_largura(1,60)

# x=menor_caminho(arvore_resposta)

# print(x)

#print(lista_de_produtos.meus_produtos)

rota = tk.Tk()
rota.title("Mapa do supermercado")

produtos_aceitos = tk.Label(
    rota,
    text="Bem-vindo ao supermercado Boa Compra! Vendemos os seguintes produtos:\n\n - ades - coca-cola - guarana - fanta - pepsi - leite - redbull - monster - tnt - kuat - guarana jesus - suco de uva integral - arroz - feijao - \nmacarrao - farinha - acucar - sal - miojo - cafe - biscoito - salgadinho - chocolate - bombom - alface - tomate - abobora - batata - pimenta - pepino - chuchu - jilo - cebola -\n alho - maca - banana - morango - uva - abacaxi - goiaba - pera - melancia - mamao - melao - limao - brocolis - cenoura - abobrinha - nugget - \npizza - hamburguer - frango - porco - picanha - costela - contra-file - queijo - iogurte - escova de dentes - pasta de dente - detergente - agua sanitaria - \nfio dental - sabonete - shampoo - condicionador - esponja - sabao em po - amaciante - desinfetante - papel higienico - lenco umedecido"
)

produtos_aceitos.pack(pady=10)

titulo = tk.Label(rota, text="Liste os produtos que você deseja comprar, separados por vírgula e sem espaços.")
titulo.pack(pady=10)

entrada = tk.Entry(rota, width=50)
entrada.pack(pady=5)


botao = tk.Button(rota, text="Enviar", command=gerenciador)
botao.pack(pady=10)

canvas = tk.Canvas(rota, width=700, height=700, bg="white")
canvas.pack()

rota.mainloop()

