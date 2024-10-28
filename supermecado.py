class Grafo:

    def __init__(self, grafo=None):
        if grafo is None:
            grafo = {}
        self.grafo = grafo

    def mostra_grafo(self):
        print(self.grafo)
        print(len(self.grafo))

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
    36:[37,40,63],
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

grafo = Grafo(meu_grafo)

grafo.mostra_grafo()