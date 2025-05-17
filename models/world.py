'''
    DECLARACAO DE OBJETOS (mapas e seus itens)

    Mapa simples (para jogador Snake): em desenvolvimento

'''
from models.player import SnakePart

class WorldItem_SNAKE:
    #Itens do tipo "estrutura" presentes no mundo (8x8)
    TIJOLO = (0, 3)
    TIJOLO_FOGO = (4, 3)
    TIJOLO_AREIA = (6, 3)
    TIJOLO_GELO = (8, 3)
    CAIXA = (1, 3)
    METAL = (5, 3)
    CUBO = (2, 3)
    FOGO = (3, 3)
    AREIA = (7, 3)
    GELO = (9, 3)
    VAZIO = (1, 2)
    VAZIO_DESERTO = (1, 10)
    #Itens do tipo "consumiveis" no mundo (8x8)
    COMIDA = (0, 2) #coordenadas de acordo com o arquivo do tilemap!!!
    MOEDA = (2, 2)
    CRISTAL = (3, 2)
    CRISTAL2 = (5, 2)
    VIDA = (4, 2)
    #Itens do tipo "POWER-UP" no mundo (8x8)
    ORB_FOGO = (11, 2) #garante imunidade ao fogo porem x2 dano de gelo
    ORB_AREIA = (11, 3) #garante imunidade a areia porem x2 dano ao bater em algo
    ORB_GELO = (10, 3) #garante imunidade ao gelo porem x2 dano de fogo
    #Itens do tipo "fase" no mundo
    PORTAL_RIGHT = (7, 2)
    PORTAL_DOWN = (8, 2)
    PORTAL_UP = (9, 2)
    PORTAL_LEFT = (10, 2)
    #itens do tipo "jogador" no mundo (8x8)
    JOGADOR = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1),
               (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4),
               (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5),
               (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6),
               (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7),
               (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8),
               (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9)
               ] #coordenadas de acordo com o arquivo do tilemap!!!

class World_SNAKE:
    
    def __init__(self, tilemap, largura, altura, baseX=0, baseY=0, tamanho=8, SNAKE=[], bioma="neutro"):
        #constantes das dimensoes do mapa do arquivo tilemap
        self.LARGURA = largura
        self.ALTURA = altura
        self.baseX = baseX #compensador no eixo X para realizar busca nos tilemaps de outras fases no arquivo
        self.baseY = baseY #compensador no eixo Y para realizar busca nos tilemaps de outras fases no arquivo
        self.TAMANHO = tamanho #dimensoes em pixels dos itens no tilemap
        self.SNAKE = SNAKE #adicionando informacoes do jogador ao mundo
        self.bioma = bioma #usado para saber qual sprite de fundo desenhar no tilemap
        self.obstaculos = ["tijolo", "caixa", "metal", "corpo", "cubo", "invalido"] #lista de obstaculos do mapa
        self.tilemap = tilemap
        self.world_map = [] #matriz que ira conter toda a info sobre posicao de estruturas, itens e jogador 
        #iterando sobre arquivo do tilemap repassado para gerar o mundo e povoando com os valores dos itens
        for y in range(self.ALTURA):
            self.world_map.append([]) # gerando linhas
            for x in range(self.LARGURA):
                #povoando colunas com itens de acordo com o arquivo do tilemap repassado
                if ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.TIJOLO):
                    self.world_map[y].append(WorldItem_SNAKE.TIJOLO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.TIJOLO_FOGO):
                    self.world_map[y].append(WorldItem_SNAKE.TIJOLO_FOGO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.TIJOLO_AREIA):
                    self.world_map[y].append(WorldItem_SNAKE.TIJOLO_AREIA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.TIJOLO_GELO):
                    self.world_map[y].append(WorldItem_SNAKE.TIJOLO_GELO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.CAIXA):
                    self.world_map[y].append(WorldItem_SNAKE.CAIXA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.CUBO):
                    self.world_map[y].append(WorldItem_SNAKE.CUBO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.FOGO):
                    self.world_map[y].append(WorldItem_SNAKE.FOGO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.AREIA):
                    self.world_map[y].append(WorldItem_SNAKE.AREIA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.GELO):
                    self.world_map[y].append(WorldItem_SNAKE.GELO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.COMIDA):
                    self.world_map[y].append(WorldItem_SNAKE.COMIDA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.MOEDA):
                    self.world_map[y].append(WorldItem_SNAKE.MOEDA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.CRISTAL):
                    self.world_map[y].append(WorldItem_SNAKE.CRISTAL)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.CRISTAL2):
                    self.world_map[y].append(WorldItem_SNAKE.CRISTAL2)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.VIDA):
                    self.world_map[y].append(WorldItem_SNAKE.VIDA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.METAL):
                    self.world_map[y].append(WorldItem_SNAKE.METAL)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.ORB_FOGO):
                    self.world_map[y].append(WorldItem_SNAKE.ORB_FOGO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.ORB_AREIA):
                    self.world_map[y].append(WorldItem_SNAKE.ORB_AREIA)
                elif ( self.tilemap.pget(x+baseX, y+baseY) == WorldItem_SNAKE.ORB_GELO):
                    self.world_map[y].append(WorldItem_SNAKE.ORB_GELO)
                elif ( self.tilemap.pget(x+baseX, y+baseY) in WorldItem_SNAKE.JOGADOR):
                    #print("GUARDANDO")
                    self.world_map[y].append(self.tilemap.pget(x+baseX, y+baseY)) #guardando sprite especifica do segmento do corpo do jogador
                else:
                    #desenhando fundo de acordo com bioma do mundo
                    if (self.bioma == "deserto"):
                        self.world_map[y].append(WorldItem_SNAKE.VAZIO_DESERTO) #falta de valor igual espaco vazio
                    else:
                        self.world_map[y].append(WorldItem_SNAKE.VAZIO) #falta de valor igual espaco vazio
    
    def printSnake(self):
        print("Segmentos ativos: ", end="")
        for parte in self.SNAKE.corpo:
            print("[ ({}, {}) | direcao = {} | tipo = {} | frente = {} | costa = {}] ".format(
                parte.posX, parte.posY, parte.direcao, parte.tipo, parte.frente, parte.costa
            ), end="")

    def printWorld(self):
        print("Valores atuais no tilemap:")
        for y in range(self.ALTURA):
            for x in range(self.LARGURA):
                print(self.world_map[y][x], end="")
            print(" {}".format(y))

    #funcao responsavel por desenhar os itens do mapa utilizando o banco de pixels correto
    def draw_worldItens(self, pyxel, posX, posY, sprite_bank, worldItem):
        pyxel.blt( 
        posX * self.TAMANHO, #posicao X onde sera desenhado o item
        posY * self.TAMANHO, #posicao Y onde sera desenhado o item
        sprite_bank, #especificando qual banco de sprites sera usado de referencia para desenhar
        worldItem[0] * self.TAMANHO, #posicao X do sprite no tilemap
        worldItem[1] * self.TAMANHO, #posicao Y do sprite no tilemap
        self.TAMANHO, #dimensao X do item
        self.TAMANHO #dimensao Y do item
        )

    #funcao responsavel por alterar o valor de algum item no mapa para outro (nao importa valor anterior)
    def change_worldItens(self, posItemX, posItemY, worldItem):
        self.world_map[posItemY][posItemX] = worldItem #alterando valor no tilemap do mundo

    #funcao responsavel por atualizar a localizacao do player no tilemap
    def loadSnakeOnTilemap(self):
        #percorrendo valores no tilemap e comparando com os valores dos segmentos da cobra (conversao necessaria)
        for y in range(self.ALTURA):
            for x in range(self.LARGURA):
                #no caso de existir um valor do tipo "corpo" nessa posicao do tilemap...
                if (self.world_map[y][x] in WorldItem_SNAKE.JOGADOR):
                    #verificar se existe um segmento no corpo com essas coordenadas...
                    existe = False
                    for parte in self.SNAKE.corpo:
                        #se coordenada (x,y) no tilemap tambem existir como coordenada de uma parte do corpo...
                        if ( (x*self.TAMANHO) == parte.posX and (y*self.TAMANHO) == parte.posY):
                            existe = True
                            break #avisando que SIM existe uma parte do corpo com essas coordenadas e quebrando loop for
                    #checando a flag para verificar se existe mesmo um segmento do corpo ou o local esta vazio
                    if (not existe):
                        if (self.bioma == "deserto"):
                            self.world_map[y][x] = WorldItem_SNAKE.VAZIO_DESERTO #falta de valor igual espaco vazio
                        else:
                            self.world_map[y][x] = WorldItem_SNAKE.VAZIO #falta de valor igual espaco vazio
                        existe = False
                else:
                    #no caso de nao existir, verificar se no vetor de segmentos ha uma parte que deve ser carregada no tilemap
                    if (self.world_map[y][x] not in WorldItem_SNAKE.JOGADOR):
                        for parte in self.SNAKE.corpo:
                            #se coordenada (x,y) no tilemap tambem existir como coordenada de uma parte do corpo...
                            if ( (x*self.TAMANHO) == parte.posX and (y*self.TAMANHO) == parte.posY):
                                    #preencher tilemap com valor tipo "corpo" especifico do segmento
                                    if (parte.tipo == "head"):
                                        #print("CARREGANDO PARTE TIPO HEAD")
                                        if (parte.direcao == 'w'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (1, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (1, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (1, 8)
                                            else:
                                                self.world_map[y][x] = (1, 0)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'a'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (0, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (0, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (0, 8)
                                            else:
                                                self.world_map[y][x] = (0, 0)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 's'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (2, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (2, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (2, 8)
                                            else:
                                                self.world_map[y][x] = (2, 0)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (3, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (3, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (3, 8)
                                            else:
                                                self.world_map[y][x] = (3, 0)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO
                                    elif (parte.tipo == "body"):
                                        #print("CARREGANDO PARTE TIPO BODY")
                                        if (parte.direcao == 'w'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (1, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (1, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (1, 9)
                                            else:
                                                self.world_map[y][x] = (1, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'wa'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (4, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (4, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (4, 9)
                                            else:
                                                self.world_map[y][x] = (4, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'wd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (7, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (7, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (7, 9)
                                            else:
                                                self.world_map[y][x] = (7, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'a'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (0, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (0, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (0, 9)
                                            else:
                                                self.world_map[y][x] = (0, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'as'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (7, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (7, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (7, 9)
                                            else:
                                                self.world_map[y][x] = (7, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'sa'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (6, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (6, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (6, 9)
                                            else:
                                                self.world_map[y][x] = (6, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 's'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (2, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (2, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (2, 9)
                                            else:
                                                self.world_map[y][x] = (2, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'sd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (5, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (5, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (5, 9)
                                            else:
                                                self.world_map[y][x] = (5, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'ds'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (4, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (4, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (4, 9)
                                            else:
                                                self.world_map[y][x] = (4, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (3, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (3, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (3, 9)
                                            else:
                                                self.world_map[y][x] = (3, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'dw'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (6, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (6, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (6, 9)
                                            else:
                                                self.world_map[y][x] = (6, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO
                                        elif (parte.direcao == 'aw'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (5, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (5, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (5, 9)
                                            else:
                                                self.world_map[y][x] = (5, 1)
                                            #evitando miragem
                                            if (self.bioma == "deserto"):
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO_DESERTO
                                            else:
                                                self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO
                                    elif (parte.tipo == "tail"):
                                        #print("CARREGANDO PARTE TIPO TAIL")
                                        if (parte.direcao == 'w'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (8, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (8, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (8, 9)
                                            else:
                                                self.world_map[y][x] = (8, 1)
                                        elif (parte.direcao == 'wa'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (10, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (10, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (10, 8)
                                            else:
                                                self.world_map[y][x] = (10, 0)
                                        elif (parte.direcao == 'aw'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (7, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (7, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (7, 8)
                                            else:
                                                self.world_map[y][x] = (7, 0)
                                        elif (parte.direcao == 'a'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (9, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (9, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (9, 8)
                                            else:
                                                self.world_map[y][x] = (9, 0)
                                        elif (parte.direcao == 'as'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (5, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (5, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (5, 8)
                                            else:
                                                self.world_map[y][x] = (5, 0)
                                        elif (parte.direcao == 'sa'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (11, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (11, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (11, 8)
                                            else:
                                                self.world_map[y][x] = (11, 0)
                                        elif (parte.direcao == 's'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (4, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (4, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (4, 8)
                                            else:
                                                self.world_map[y][x] = (4, 0)
                                        elif (parte.direcao == 'sd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (11, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (11, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (11, 9)
                                            else:
                                                self.world_map[y][x] = (11, 1)
                                        elif (parte.direcao == 'ds'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (6, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (6, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (6, 8)
                                            else:
                                                self.world_map[y][x] = (6, 0)
                                        elif (parte.direcao == 'd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (9, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (9, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (9, 9)
                                            else:
                                                self.world_map[y][x] = (9, 1)
                                        elif (parte.direcao == 'dw'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (8, 4)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (8, 6)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (8, 8)
                                            else:
                                                self.world_map[y][x] = (8, 0)
                                        elif (parte.direcao == 'wd'):
                                            #desenhando o sprite de acordo com o tipo da cobra (la ele)
                                            if (self.SNAKE.tipo == "fogo"):
                                                self.world_map[y][x] = (10, 5)
                                            elif (self.SNAKE.tipo == "areia"):
                                                self.world_map[y][x] = (10, 7)
                                            elif (self.SNAKE.tipo == "gelo"):
                                                self.world_map[y][x] = (10, 9)
                                            else:
                                                self.world_map[y][x] = (10, 1)
    
    '''
        Funcao responsavel por checar colisoes do jogador com os itens no mundo...
        OBS: SEMPRE REALIZAR CONVERSAO DE COORDENADAS DO JOGADOR E DO TILEMAP ( (8, 24) == (1, 3) com T=8)

        Funcao ira devolver valores de acordo com o elemento que foi colidido, onde:
        - return "tijolo/caixa/metal/cubo" -> significa que o jogador nao podera avancar para esse lugar (-1 de vida)
        - return "vazio" -> significa que o jogador podera avancar ao local sem problemas
        - return "moeda" -> significa que o jogador podera avancar ao local e adquirir pontuacao +500
        - return "cristal" -> significa que o jogador podera avancar ao local e adquirir pontuacao +2000
        - return "cristal" -> significa que o jogador podera avancar ao local e adquirir pontuacao +4000
        - return "comida" -> significa que o jogador podera avancar e crescer seu tamanho em 1 (caso ultrapasse o
        local valido para mover durante esse processo o jogador ira consumir a comida mas nao ira crescer)
        - return "corpo" -> significa que o jogador colidiu com uma parte de seu corpo (-1 de vida)
        - return "fogo" -> significa que o jogador colidiu com um local em chamas e por isso ira avancar ao local
        (-1 de vida)
        - return "orbFogo" -> significa que o jogador coletou o POWER-UP de fogo e agora tem imunidade ao dano 
        por fogo porem recebe x2 dano de gelo!
        - return "orbAreia" -> significa que o jogador coletou o POWER-UP de areia e agora tem imunidade ao dano 
        por areia POREM RECEBE X2 dano ao colidir com estruturas!
        - return "orbGelo" -> significa que o jogador coletou o POWER-UP de gelo e agora tem imunidade ao dano 
        por gelo porem recebe x2 dano de fogo!
    '''
    def checkCollision(self, direcao):
        #verificando local futuro onde o jogador estara ao se mover...convertido para tilemap
        posSnakeX = int((self.SNAKE.corpo[0].posX/self.TAMANHO))
        posSnakeY = int((self.SNAKE.corpo[0].posY/self.TAMANHO))
        #print("Posicao do jogador (tilemap): [ {}, {}]".format(posSnakeX, posSnakeY))
        #eliminando movimentos invalidos logo de cara (como cobra andando sobre si mesma em direcao oposta)
        if (direcao == 'w' and self.SNAKE.corpo[0].direcao == 's'):
            return "invalido"
        elif (direcao == 's' and self.SNAKE.corpo[0].direcao == 'w'):
            return "invalido"
        elif (direcao == 'a' and self.SNAKE.corpo[0].direcao == 'd'):
            return "invalido"
        elif (direcao == 'd' and self.SNAKE.corpo[0].direcao == 'a'):
            return "invalido"
        #simulando alteracao da posicao do jogador para futuras comparacoes
        if ( direcao == 'w'):
            posItemX = posSnakeX
            posItemY = posSnakeY-1
        elif ( direcao == 'a'):
            posItemX = posSnakeX-1
            posItemY = posSnakeY
        elif ( direcao == 's'):
            posItemX = posSnakeX
            posItemY = posSnakeY+1
        elif ( direcao == 'd'):
            posItemX = posSnakeX+1
            posItemY = posSnakeY
        else:
            return "invalido"
        #verificando valor no tilemap equivalente ao local do futuro deslocamento
        #print("Posicao futura ao se mover: [ {}, {}]".format(posItemX, posItemY))
        if ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.TIJOLO or
            self.world_map[posItemY][posItemX] == WorldItem_SNAKE.TIJOLO_FOGO or
            self.world_map[posItemY][posItemX] == WorldItem_SNAKE.TIJOLO_AREIA or
            self.world_map[posItemY][posItemX] == WorldItem_SNAKE.TIJOLO_GELO):
            #print("Tem uma parede de tijolos na minha frente...nao posso passar!")
            return "tijolo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.CAIXA):
            #print("Tem uma caixa na minha frente...nao posso passar!")
            return "caixa"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.METAL):
            #print("Tem uma placa de metal na minha frente...nao posso passar!")
            return "metal"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.CUBO):
            #print("Uhhh, que frio...nao posso passar!")
            return "cubo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.FOGO):
            #print("OUCH! Me queimei...")
            return "fogo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.AREIA):
            #print("OUCH! Me arranhei...")
            return "areia"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.GELO):
            #print("OUCH! Me queimei de frio...")
            return "gelo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.MOEDA):
            #print("Mais uma moeda para a colecao!")
            return "moeda"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.CRISTAL):
            #print("Que cristal bonito...")
            return "cristal"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.CRISTAL2):
            #print("Que cristal lindo...")
            return "cristal2"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.COMIDA):
            #print("comida")
            return "comida"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.VAZIO or 
              self.world_map[posItemY][posItemX] == WorldItem_SNAKE.VAZIO_DESERTO):
            #print("Caminho livre...em frente!")
            return "vazio"
        elif ( self.world_map[posItemY][posItemX] in WorldItem_SNAKE.JOGADOR):
            #print("OUCH! Bati em mim mesmo...")
            return "corpo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.VIDA):
            #print("Oba! Me sinto bem melhor...")
            return "vida"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.ORB_FOGO):
            #print("Quanto poder!! Sinto que sou invencivel ao fogo...")
            return "orbFogo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.ORB_AREIA):
            #print("Quanto poder!! Sinto que sou invencivel as areias do deserto...")
            return "orbAreia"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.ORB_GELO):
            #print("Quanto poder!! Sinto que sou invencivel ao gelo...")
            return "orbGelo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.PORTAL_RIGHT or
              self.world_map[posItemY][posItemX] == WorldItem_SNAKE.PORTAL_LEFT or
              self.world_map[posItemY][posItemX] == WorldItem_SNAKE.PORTAL_UP or
              self.world_map[posItemY][posItemX] == WorldItem_SNAKE.PORTAL_DOWN):
            #print("O que seria isso? Vou explorar...")
            return "portal"
        else:
            print("Nao sei o que esta na minha frente...")
            return "invalido"
        
    # FINALIZADO (talvez contenha bugs de timing no momento do consumo de comidas)
    def grow(self):
        '''
            Acrescentando 1 segmento do tipo "body" para o vetor corpo da cobra, onde:
            PASSO 1: "remover" cabeca temporariamente (criar copia)
            PASSO 2: criar novo segmento do tipo "body" com base na antiga posicao da cabeca
            PASSO 3: adicionar novo segmento ao vetor corpo da cobra (frente=0, costa=2)
            PASSO 4: adicionar cabeca ao segmento corpo com nova posicao de acordo a direcao do 
            novo segmento corpo e com seu atributo costa igual ao indice do segmento corpo (1)
        '''
        if (self.checkCollision(self.SNAKE.corpo[0].direcao) not in self.obstaculos):
            cabeca = self.SNAKE.corpo.pop(0)
            parteNova = SnakePart(cabeca.posX, cabeca.posY, "body", cabeca.direcao, 0, 2)
            self.SNAKE.corpo.insert(0, parteNova) #adicionando novo segmento de corpo no antigo lugar da cabeca
            #nova posicao da cabeca seguira o movimento anterior ao crescimento
            if (cabeca.direcao == 'w'):
                cabeca.posY -= 8
            elif (cabeca.direcao == 'a'):
                cabeca.posX -= 8
            elif (cabeca.direcao == 's'):
                cabeca.posY += 8
            elif (cabeca.direcao == 'd'):
                cabeca.posX += 8
            self.SNAKE.corpo.insert(0, cabeca) #reposicionando cabeca de volta ao corpo com atributos atualizados
            #atualizando atributos frente e costa dos antigos segmentos (resto do corpo e cauda)
            for i in range(2, len(self.SNAKE.corpo)):
                #tratando cauda de maneira diferente
                if (i == (len(self.SNAKE.corpo)-1) ):
                    self.SNAKE.corpo[i].frente += 1 #atualizar somente frente, costa segue vzia
                else:
                    self.SNAKE.corpo[i].frente += 1
                    self.SNAKE.corpo[i].costa += 1
            print("C-R-E-S-C-E-N-D-O")

    #funcao que adiciona um item do tipo "codigoItem" ao tilemap do mundo (local deve estar vazio)
    def addItem(self, posX, posY, codigoItem):
        #convertendo coordenadas na tela para coordenadas aceitas pelo tilemap
        posItemX = int(posX/self.TAMANHO)
        posItemY = int(posY/self.TAMANHO)
        #verificando se coordenada no tilemap ja esta ocupada por algum valor
        if (self.world_map[posItemX][posItemY] != WorldItem_SNAKE.VAZIO):
            return False #erro ao adicionar item, local invalido
        else:
            self.world_map[posItemX][posItemY] = codigoItem
            return True #sucesso ao adicionar item do tipo "codigoItem"

