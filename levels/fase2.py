'''

    LEVEL 2 - arquivo que carrega a primeira fase do jogo 

'''

from models.world import *
from models.player import *
from models import utilities
from levels import State
import pyxel
import random

#declarando constantes
LARGURA_JANELA = 128
ALTURA_JANELA = 137 #onde 128 pixels sao dedicados ao jogo e 9 pixels as informacoes do jogador (vida e pontos)
TAMANHO = 8 #referencia das dimensoes em pixels dos sprites no tilemap

#CODIGO PRINCIPAL
class Fase2(State):

    def onEnter(self, game):
        pyxel.mouse(True)
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/SNAKE_2.0/Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/SNAKE_2.0/Assets/Fonts/VictoriaBold-8.bdf")

        #carregando componentes do jogo (mundo e jogador)
        self.dados = utilities.readInfoPlayer() #lendo atributos do jogador obtidos na fase 1
        self.player = Snake(posX=16, posY=64, dir='d', Dx=8, vidas=self.dados[0], pontos=self.dados[1], tipo="planta")
        self.world = World_SNAKE(pyxel.tilemaps[0], largura=16, altura=16, baseX=16, baseY=0, tamanho=8, SNAKE=self.player)
        self.INPUT = self.player.dirAtual #flag de controle para a direcao passiva da cobra (movimento inicial)
        self.GAME_OVER = False 
        self.time = 20 #tempo base para o ritmo da gameplay
        #guardando dados do jogador para mostrar na janela GAME OVER
        utilities.writeInfoPlayer(self.player) #guardando dados

        #tocando musica de fundo em um loop infinito
        pyxel.playm(4, loop=True)

    def update(self, game):
        #checando se jogador ja utilizou todas as vidas ao jogar
        if (self.player.vidas <= 0):
            self.GAME_OVER = True
        if (not self.GAME_OVER):
            #checando tamanho do jogador, se atingir 40 entao gerar portais para avancar de fase
            if ( len(self.player.corpo) == 5):
                self.world.change_worldItens(15, 7, WorldItem_SNAKE.PORTAL_RIGHT)
                self.world.change_worldItens(15, 8, WorldItem_SNAKE.PORTAL_RIGHT)
            #checando constantemente input do usuario, caso jogo nao tenha finalizado
            if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)):
                self.INPUT = 'w'
            elif (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)):
                self.INPUT = 'a'
            elif (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)):
                self.INPUT = 's'
            elif (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)):
                self.INPUT = 'd'
            #checando movimentos invalidos e nao deixando valor ser repassado na atualizacao
            if ( self.world.checkCollision(self.INPUT) == "invalido"):
                self.INPUT = self.world.SNAKE.corpo[0].direcao #restaurando direcao valida
            #atualizando o jogo de acordo com a variavel TIME
            if (pyxel.frame_count%self.time == 0):
                if ( self.world.checkCollision(self.INPUT) == "comida"):
                    pyxel.play(0, 0) #reproduzindo sound[0] no channel[0] (efeito COMIDA)
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                    self.player.pontos += 200
                    if (self.world.checkCollision(self.INPUT) not in self.world.obstaculos):
                        self.world.grow()
                    utilities.writeInfoPlayer(self.player) #guardando dados 
                elif ( self.world.checkCollision(self.INPUT) == "fogo"):
                    if (self.player.tipo != "fogo"):
                        pyxel.play(0, 3) #reproduzindo sound[3] no channel[0] (efeito FOGO)
                        self.player.vidas -= 1
                        if (self.player.tipo == "gelo"):
                            self.player.vidas -= 1 #dano extra por fraqueza ao fogo
                        utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "areia"):
                    if (self.player.tipo != "areia"):
                        pyxel.play(0, 21) #reproduzindo sound[3] no channel[0] (efeito AREIA)
                        self.player.vidas -= 1
                        utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "gelo"):
                    if (self.player.tipo != "gelo"):
                        pyxel.play(0, 22) #reproduzindo sound[3] no channel[0] (efeito GELO)
                        self.player.vidas -= 1
                        if (self.player.tipo == "fogo"):
                            self.player.vidas -= 1 #dano extra por fraqueza ao gelo
                        utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "vida"):
                    pyxel.play(0, 4) #reproduzindo sound[4] no channel[0] (efeito VIDA)
                    self.player.vidas += 1
                    utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "moeda"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    self.player.pontos += 500
                    utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "cristal"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    self.player.pontos += 2000
                    utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "cristal2"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    self.player.pontos += 4000
                    utilities.writeInfoPlayer(self.player) #guardando dados 
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "orbFogo"):
                    pyxel.play(0, 13) #reproduzindo sound[13] no channel[0] (efeito POWER UP FOGO)
                    self.player.tipo = "fogo"
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "orbAreia"):
                    pyxel.play(0, 14) #reproduzindo sound[14] no channel[0] (efeito POWER UP AREIA)
                    self.player.tipo = "areia"
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "orbGelo"):
                    pyxel.play(0, 15) #reproduzindo sound[15] no channel[0] (efeito POWER UP GELO)
                    self.player.tipo = "gelo"
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "portal"):
                    utilities.writeInfoPlayer(self.player) #salvando dados do jogador em um arquivo a parte
                    #encerrando musica da fase2 e iniciando musica da fase3
                    pyxel.playm(3, loop=True)
                    return "fase3"
                elif ( self.world.checkCollision(self.INPUT) == "relogioUP"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    #evitando tempo negativo
                    if (self.time <= 8):
                        self.time = 1 #acelerando ritmo do jogo (maximo possivel)
                    else:
                        self.time -= 8 #acelerando ritmo do jogo
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "relogioDOWN"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    self.time += 8 #reduzindo ritmo do jogo
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) not in self.world.obstaculos):
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) in self.world.obstaculos):
                    self.player.vidas -= 1
                    pyxel.play(0, 2) #reproduzindo sound[1] no channel[0] (efeito OBSTACULO)
                    #checando caso especial: jogador com orb de fogo no obstaculo: cubo de gelo
                    if (self.world.checkCollision(self.INPUT) == "cubo" and self.player.tipo == "fogo"):
                        self.player.vidas -= 1 #dano dobrado por fraqueza
                    #checando caso especial: jogador com orb de areia colidindo com obstaculo: estruturas
                    elif (self.player.tipo == "areia"):
                        self.player.vidas -= 1 #dano dobrado por fraqueza
                    utilities.writeInfoPlayer(self.player) #salvando dados do jogador
        else:
            #encerrando musica da fase1 e reproduzindo musica da tela de game over
            pyxel.playm(2, loop=True)
            utilities.writeInfoPlayer(self.player) #salvando dados do jogador em um arquivo a parte
            return "game over"
        #chance de gerar comidas randomicas a cada 3 segundos em locais vazios do mapa
        if (pyxel.frame_count%180 == 0):
            posXrandom = random.randint(0, 127)
            posYrandom = random.randint(0, 127)
            self.world.addItem(posXrandom, posYrandom, WorldItem_SNAKE.COMIDA)

    def draw(self, game):
        pyxel.cls(0)
        if (not self.GAME_OVER):
            self.world.loadSnakeOnTilemap() #atualizando valores do jogador no tilemap
            #desenhando mapa
            for y in range(self.world.ALTURA):
                for x in range(self.world.LARGURA):
                    worldItem = self.world.world_map[y][x]
                    self.world.draw_worldItens(pyxel, x, y, 0, worldItem)
            #desenhando informacoes do jogador (pontuacao e vidas)
            pyxel.text(80, 130, "POINTS:{}".format(self.player.pontos), pyxel.COLOR_WHITE)
            pyxel.text(2, 130, "LIFE: ", pyxel.COLOR_WHITE)
            for vidas in range(self.player.vidas):
                if (vidas == 5):
                    pyxel.text(71, 129, "+{}".format(self.player.vidas-vidas), pyxel.COLOR_WHITE) #finalizando impressao de coracoes caso > 5
                    break
                pyxel.blt(21+(vidas*10), 128, 0, 32, 16, 8, 8) #desenhando icones de coracao  