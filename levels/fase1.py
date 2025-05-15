'''

    LEVEL 1 - arquivo que carrega a primeira fase do jogo 

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
class Fase1(State):

    def onEnter(self, game):
        pyxel.mouse(True)
        pyxel.load("Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("Assets/Fonts/VictoriaBold-8.bdf")

        #carregando componentes do jogo (mundo e jogador)
        self.player = Snake(posX=8, posY=24, dir='s', Dx=8, vidas=5, pontos=100, tipo="planta")
        self.world = World_SNAKE(pyxel.tilemaps[0], largura=16, altura=16, tamanho=8, SNAKE=self.player)
        self.INPUT = 's' #flag de controle para a direcao passiva da cobra (movimento inicial)
        self.GAME_OVER = False 
        #guardando dados do jogador para mostrar na janela GAME OVER
        utilities.writeInfoPlayer(self.player)
        

    def update(self, game):
        #checando se jogador ja utilizou todas as vidas ao jogar
        if (self.player.vidas <= 0):
            self.GAME_OVER = True
        if (not self.GAME_OVER):
            #checando tamanho do jogador, se atingir 30 entao gerar portais para avancar de fase
            if ( len(self.player.corpo) == 5):
                self.world.change_worldItens(15, 7, WorldItem_SNAKE.PORTAL)
                self.world.change_worldItens(15, 8, WorldItem_SNAKE.PORTAL)
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
            #atualizando mudanca de movimento a cada 0.5 segundos
            if (pyxel.frame_count%20 == 0):
                if ( self.world.checkCollision(self.INPUT) == "comida"):
                    pyxel.play(0, 0) #reproduzindo sound[0] no channel[0] (efeito COMIDA)
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                    self.player.pontos += 200
                    if (self.world.checkCollision(self.INPUT) not in self.world.obstaculos):
                        self.world.grow()
                elif ( self.world.checkCollision(self.INPUT) == "fogo"):
                    pyxel.play(0, 3) #reproduzindo sound[3] no channel[0] (efeito FOGO)
                    self.player.vidas -= 1
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "vida"):
                    pyxel.play(0, 4) #reproduzindo sound[4] no channel[0] (efeito VIDA)
                    self.player.vidas += 1
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "moeda"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    self.player.pontos += 500
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "cristal"):
                    pyxel.play(0, 1) #reproduzindo sound[1] no channel[0] (efeito PONTOS)
                    self.player.pontos += 2000
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "portal"):
                    utilities.writeInfoPlayer(self.player) #salvando dados do jogador em um arquivo a parte
                    return "fase2"
                elif ( self.world.checkCollision(self.INPUT) not in self.world.obstaculos):
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) in self.world.obstaculos):
                    self.player.vidas -= 1
                    pyxel.play(0, 2) #reproduzindo sound[1] no channel[0] (efeito OBSTACULO)
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

