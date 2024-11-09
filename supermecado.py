import tkinter as tk
from tkinter import messagebox
import meu_grafo, coordenadas_grafo, grafo, lista_de_produtos
from collections import deque

grafo = grafo.Grafo(meu_grafo.meu_grafo)

def menor_caminho (arvore):
    # funcao para tirar nos indesejados da arvore final de menor caminho
    inicio = arvore[0][0]
    fim = arvore[-1][-1]
    nova_arvore = []
    arvore.reverse()
    for no in arvore:
        if (no[0] == inicio and no[1] == fim):
            nova_arvore.append(no)
            return nova_arvore
        elif no[1] == fim:
            fim = no[0]
            nova_arvore.append(no)

def manipula_lista_compras(lista_produtos):
    
    lista_de_compras_grafo = []
    # separa por virgula
    lista_compras = [p.strip() for p in lista_produtos.split(",")]
    print("Produtos digitados:", lista_compras)
    legenda = ["1 - entrada"]
    # transforma a lista de compras em numeros que o grafo entende como seus nos, faz a legenda 
    for produto in lista_compras:
        for meu_produto in lista_de_produtos.meus_produtos:
            if lista_de_produtos.meus_produtos[meu_produto] == produto:
                lista_de_compras_grafo.append(meu_produto)
                aux = str(meu_produto) + " - " + produto
                legenda.append(aux)
    
    legenda.append("60 - caixa")
    coordenadas_caminho.config(text = legenda)
    print(lista_de_compras_grafo)
    return lista_de_compras_grafo

def desenha_caminho(caminho, produtos):
    #pinta os nos que estão no caminho de vermelho e os que não estão de cinza
    for node, (x, y) in coordenadas_grafo.coordenadas_grafo.items():
        if node in produtos:
            color = "green"
        elif node in caminho:
            color = "red"
        else: 
            color = "grey"
        canvas.create_oval(x-10, y-10, x+10, y+10, fill=color)
        canvas.create_text(x, y, text=str(node), fill="white")
    # cria arestas de forma visual
    for node, neighbors in meu_grafo.meu_grafo.items():
        x1, y1 = coordenadas_grafo.coordenadas_grafo[node]
        for neighbor in neighbors:
            x2, y2 = coordenadas_grafo.coordenadas_grafo[neighbor]
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
    
    desenha_caminho(caminho_final, lista_grafo)

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

coordenadas_caminho = tk.Label(rota, text="")
coordenadas_caminho.pack(pady=10)

canvas = tk.Canvas(rota, width=700, height=400, bg="white")
canvas.pack()

rota.mainloop()

