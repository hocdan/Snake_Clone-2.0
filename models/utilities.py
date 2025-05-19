'''
    COMPILADO DE FUNCOES UTEIS DIVERSAS

    - draw_text_with_border() -> desenha textos com fontes customizaveis com bordas coloridas nas letras

'''
import pyxel
import os

#FUNCAO USADA PARA CHECAR COLISAO DE UM PONTO (x, y) COM UM RETANGULO (x, y, largura, altura)
def checkPointOnRec(posX, posY, recX, recY, largura, altura):
    #checando se ponto de coordenada (X, Y) se encontra dentro de retangulo com as dimensoes passadas
    if ( posX >= recX and posX <= recX+largura and posY >= recY and posY <= recY+altura):
        return True
    else:
        return False
    
'''
Funcao usada para:
    -> ARMAZENAR dados basicos do jogador (vidas, pontuacao e tamanho) em um arquivo separado
    -> local de armazenamento do arquivo: /Assets/info_player.txt
    -> valor da primeira linha: vidas do jogador atual
    -> valor da segunda linha: pontuacao final atingida pelo jogador atual
    -> valor da terceira linha: tamanho final atingido pelo jogador atual
'''
def writeInfoPlayer(SNAKE):
    localArquivo = os.path.join(os.getcwd() + '/PLAYER_INFO/player01.txt')
    print("Criando arquivo para armazenar info do jogador...")
    #abrindo arquivo para escrita
    with open(localArquivo, 'w') as arquivo:
        arquivo.write(str(SNAKE.vidas) + "\n")
        arquivo.write(str(SNAKE.pontos) + "\n")
        arquivo.write(str(len(SNAKE.corpo)) + "\n")
    print("Arquivo salvo com sucesso!!!")

'''
Funcao usada para:
    -> LER dados basicos do jogador (vidas, pontuacao e tamanho) em um arquivo separado
    -> local de armazenamento do arquivo: /Assets/info_player.txt
    -> valor da primeira linha: vidas do jogador atual
    -> valor da segunda linha: pontuacao final atingida pelo jogador atual
    -> valor da terceira linha: tamanho final atingido pelo jogador atual
'''
def readInfoPlayer():
    info = []
    #abrindo arquivo para leitura
    localArquivo = os.path.join(os.getcwd() + '/PLAYER_INFO/player01.txt')
    print("Lendo arquivo do jogador...")
    with open(localArquivo, 'r+') as arquivo:
        #lendo cada linha de maneira individual
        for linha in arquivo:
            info.append(int(linha.strip())) #convertendo string em inteiro (info do jogador)
    print(info)
    return info #devolvendo conjunto de dados [vidas, pontuacao, tamanho]
    
'''
Funcao usada para:
    -> apagar arquivo contendo informacoes (vidas, pontuacao, tamanho) do jogador

    OBS: essa funcao deve sempre ser usada ao sair de alguma fase e regressar ao menu!!!
'''
def removeInfoPlayer():
    localArquivo = os.path.join(os.getcwd() + '/PLAYER_INFO/player01.txt')
    if os.path.isfile(localArquivo):
        #limpando conteudo do arquivo
        with open(localArquivo, 'w') as arquivo:
            print("Apagando info do jogador...")
    else:
        print("Erro ao apagar info do jogador!!!")

'''
Funcao usada para: 
    -> desenhar bordas nas letras de uma palavra "S" de letras
    -> dar coloracao "col" para as letras e coloracao "bcol" para a borda
    -> gerar palavra final de acordo com a fonte "font"
'''
def draw_text_with_border(x, y, s, col, bcol, font):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                pyxel.text(
                    x + dx,
                    y + dy,
                    s,
                    bcol, #valor para colorir a borda das letras
                    font, #arquivo da fonte para as letras
                )
    pyxel.text(x, y, s, col, font)
