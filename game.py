import pyxel
from levels.menu import Menu
from levels.fase1 import Fase1
from levels.fase2 import Fase2
from levels.fase3 import Fase3
from levels.fase4 import Fase4
from levels.the_end import Final
from levels.tutorial import Tutorial
from levels.game_over import GameOver

class Game:
    def __init__(self):
        pyxel.init(128, 136, "SNAKE 2.0", fps=60)
        self.states = {
            "menu": Menu(),
            "fase1": Fase1(),
            "fase2": Fase2(),
            "fase3": Fase3(),
            "fase4": Fase4(),
            "the end": Final(),
            "tutorial": Tutorial(),
            "game over": GameOver()
        }
        self.currentState = self.states["menu"]
        self.currentState.onEnter(self)
        pyxel.run(self.update, self.draw)
    
    def changeState(self, stateName):
        self.currentState.onExit(self)
        self.currentState = self.states[stateName]
        self.currentState.onEnter(self)

    def update(self):
        nextState = self.currentState.update(self)
        if nextState:
            self.changeState(nextState)
    
    def draw(self):
        self.currentState.draw(self)