'''

'''
from levels import State
from models import utilities
import pyxel

class GameOver(State):

    def __init__(self):
        #inicializando janela
        pyxel.mouse(True)
        #carregando icones do jogo
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/SNAKE_2.0/Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/SNAKE_2.0/Assets/Fonts/VictoriaBold-8.bdf")
        #carregando dados do jogador para mostrar na janela GAME OVER
        self.infoPlayer = utilities.readInfoPlayer() # devolve [vidas, pontuacao, tamanho]

    def update(self, game):
        #atualizando dados do jogador para mostrar na janela GAME OVER
        self.infoPlayer = utilities.readInfoPlayer() # devolve [vidas, pontuacao, tamanho]
        #checando se usuario ira querer reiniciar jogo
        if (pyxel.btn(pyxel.KEY_R) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A)):
            pyxel.play(0, 5) #reproduzindo sound[5] no channel[0] para efeito CLIQUE
            #encerrando musica da tela de game over e reproduzindo musica da fase1
            pyxel.stop(3) #fechando canal 3 para nao continuar ativo em cima das outras musicas
            pyxel.playm(0, loop=True)
            #apagando dados antigos do jogador
            utilities.removeInfoPlayer()
            return "fase1"
        elif (pyxel.btn(pyxel.KEY_M) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B)):
            #devolvendo controle para carregar arquivo "menu.py"
            pyxel.play(0, 5) #reproduzindo sound[5] no channel[0] para efeito CLIQUE
            #encerrando musica da fase1 e reproduzindo musica do menu
            pyxel.stop(3) #fechando canal 3 para nao continuar ativo em cima das outras musicas
            pyxel.playm(1, loop=True)
            #apagando dados antigos do jogador
            utilities.removeInfoPlayer()
            return "menu"

    def draw(self, game):
        pyxel.cls(0)
        #desenhando tela de fim de jogo
        pyxel.rectb(26, 10, 77, 11, pyxel.COLOR_WHITE) #desenhando bordas do quadro game over
        pyxel.text(28, 12, "GAME OVER", pyxel.COLOR_WHITE, self.fonte)
        pyxel.rectb(5, 35, 118, 30, pyxel.COLOR_WHITE) #desenhando bordas do quadro de status do jogador
        pyxel.text(10, 40, "You scored {} points!".format(self.infoPlayer[1]), pyxel.COLOR_WHITE)
        pyxel.text(10, 55, "Your lenght was: {} meters!".format(self.infoPlayer[2]), pyxel.COLOR_WHITE)
        pyxel.text(8, 91, "> Press R to restart game", pyxel.COLOR_WHITE)
        pyxel.text(8, 101, "> Press M to go back to menu", pyxel.COLOR_WHITE)
        pyxel.text(8, 111, "> Press ESC to exit game", pyxel.COLOR_WHITE)
        pyxel.text(16, 126, "A game made by Daniel SG", pyxel.COLOR_WHITE) #creditos
        pyxel.line(13, 133, 113, 133, pyxel.COLOR_WHITE)
        #desenhando decoracoes da tela de game over
        pyxel.blt(5, 10, 0, 0, 24, 8, 8) #desenhando tijolo 1
        pyxel.blt(5, 18, 0, 0, 24, 8, 8) #desenhando tijolo 2
        pyxel.blt(13, 18, 0, 16, 16, 8, 8) #desenhando moeda
        pyxel.blt(115, 10, 0, 8, 24, 8, 8) #desenhando caixa 1
        pyxel.blt(115, 18, 0, 8, 24, 8, 8) #desenhando caixa 2
        pyxel.blt(107, 18, 0, 24, 16, 8, 8) #desenhando cristal
        pyxel.blt(35, 75, 0, 0, 0, 8, 8) #cabeca virada para a esquerda
        for i in range(6):
            pyxel.blt(43+(i*8), 75, 0, 0, 8, 8, 8) #6 segmentos de corpo virado para a esquerda
        pyxel.blt(91, 75, 0, 72, 0, 8, 8) #rabo virado para a esquerda
        pyxel.blt(13, 75, 0, 0, 16, 8, 8) #desenhando comida
        pyxel.blt(110, 75, 0, 24, 24, 8, 8) #desenhando fogo