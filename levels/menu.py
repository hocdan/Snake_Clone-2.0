'''

    PROGRAMA AUXILIAR RESPONSAVEL POR MOSTRAR O MENU INICIAL DO JOGO SNAKE 2.0

    -> Conta com tres opcoes basicas:

    1. Jogar (inicia a fase 1)
    2. Tutorial (carrega janela Tutorial)
    3. Sair (finaliza o jogo)
'''

from models import utilities
from models import world
from levels import State
import pyxel

#CODIGO PRINCIPAL
class Menu(State):

    def onEnter(self, game):
        #inicializando janela
        pyxel.mouse(True)
        #carregando icones do jogo
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/SNAKE_2.0/Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/SNAKE_2.0/Assets/Fonts/VictoriaBold-8.bdf")
        #declarando tilemap para decoracao da tela tutorial
        self.decoration = world.World_SNAKE(pyxel.tilemaps[2], largura=16, altura=17, tamanho=8)

        #declarando e inicializando retangulos do menu (para colisao e display de mensagens)
        self.recJogar = [45, 35, 40, 20, pyxel.COLOR_GREEN]
        self.recTutorial = [45, 65, 40, 20, pyxel.COLOR_YELLOW]
        self.recSair = [45, 95, 40, 20, pyxel.COLOR_RED]
        #declarando flags de controle das opcoes do menu
        self.mouseOnJogar = False
        self.mouseOnTutorial = False
        self.mouseOnSair = False

        #tocando musica de fundo em um loop infinito
        pyxel.playm(1, loop=True)

    def update(self, game):
        #checando se usuario esta com o mouse posicionado nas opcoes do menu
        if ( utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recJogar[0], self.recJogar[1], self.recJogar[2], self.recJogar[3])):
            self.mouseOnJogar = True
        elif ( utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recTutorial[0], self.recTutorial[1], self.recTutorial[2], self.recTutorial[3])):
            self.mouseOnTutorial = True
        elif ( utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3])):
            self.mouseOnSair = True
        else:
            self.mouseOnJogar = False
            self.mouseOnTutorial = False
            self.mouseOnSair = False

        #realizando opcoes de acordo com o clique do usuario
        if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, hold=30)):
            if (self.mouseOnJogar):
                pyxel.play(0, 5) #reproduzindo sound[5] no channel[0] para efeito CLIQUE
                #encerrando musica do menu e iniciando musica da fase1
                pyxel.playm(0, loop=True)
                return "fase1"
            elif (self.mouseOnTutorial):
                pyxel.play(0, 5) #reproduzindo sound[5] no channel[0] para efeito CLIQUE
                return "tutorial"
            elif (self.mouseOnSair):
                pyxel.play(0, 5) #reproduzindo sound[5] no channel[0] para efeito CLIQUE
                pyxel.quit() #finalizando janela

    def draw(self, game):
        pyxel.cls(0) #limpando tela
        #desenhando tilemap
        for y in range(self.decoration.ALTURA):
            for x in range(self.decoration.LARGURA):
                worldItem = self.decoration.world_map[y][x]
                self.decoration.draw_worldItens(pyxel, x, y, 0, worldItem)
        #desenhando menu
        pyxel.text(50, 15, "MENU", pyxel.COLOR_WHITE, self.fonte)
        pyxel.rect(self.recJogar[0], self.recJogar[1], self.recJogar[2], self.recJogar[3], self.recJogar[4])
        pyxel.text(self.recJogar[0]+13, self.recJogar[1]+8, "PLAY", pyxel.COLOR_WHITE)
        pyxel.rect(self.recTutorial[0], self.recTutorial[1], self.recTutorial[2], self.recTutorial[3], self.recTutorial[4])
        pyxel.text(self.recTutorial[0]+4, self.recTutorial[1]+8, "TUTORIAL", pyxel.COLOR_WHITE)
        pyxel.rect(self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3], self.recSair[4])
        pyxel.text(self.recSair[0]+13, self.recSair[1]+7, "EXIT", pyxel.COLOR_WHITE)
        #desenhando contorno nos botoes do menu caso o mouse esteja em cima deles
        if (self.mouseOnJogar):
            pyxel.rectb(self.recJogar[0], self.recJogar[1], self.recJogar[2], self.recJogar[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnTutorial):
            pyxel.rectb(self.recTutorial[0], self.recTutorial[1], self.recTutorial[2], self.recTutorial[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnSair):
            pyxel.rectb(self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3], pyxel.COLOR_WHITE)
